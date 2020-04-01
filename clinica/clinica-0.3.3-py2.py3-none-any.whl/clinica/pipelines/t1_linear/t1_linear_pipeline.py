# -*- coding: utf-8 -*-
import clinica.pipelines.engine as cpe

# Use hash instead of parameters for iterables folder names
# Otherwise path will be too long and generate OSError
from nipype import config
cfg = dict(execution={'parameterize_dirs': False})
config.update_config(cfg)


class T1Linear(cpe.Pipeline):
    """T1 Linear - Affine registration of T1w images to standard space.
    This preprocessing pipeline includes globally three steps:
    1) Bias correction with N4 algorithm from ANTs.
    2) Linear registration to MNI152NLin2009cSym template with
       RegistrationSynQuick from ANTs.
    3) Crop the background (in order to save computational power).

    Returns:
        A clinica pipeline object containing the T1 Linear pipeline.
    """

    def check_custom_dependencies(self):
        """Check dependencies that can not be listed in the `info.json` file.
        """
        pass

    def get_input_fields(self):
        """Specify the list of possible inputs of this pipeline.

        Returns:
            A list of (string) input fields name.
        """

        return ['t1w']

    def get_output_fields(self):
        """Specify the list of possible outputs of this pipeline.

        Returns:
            A list of (string) output fields name.
        """

        return ['image_id']

    def build_input_node(self):
        """Build and connect an input node to the pipeline.
        """
        from os import pardir
        from os.path import dirname, join, abspath, split, exists
        import sys
        import nipype.interfaces.utility as nutil
        import nipype.pipeline.engine as npe
        from clinica.utils.inputs import check_bids_folder
        from clinica.utils.exceptions import ClinicaBIDSError, ClinicaException
        from clinica.utils.inputs import clinica_file_reader
        from clinica.utils.input_files import T1W_NII
        from clinica.utils.inputs import fetch_file
        from clinica.utils.ux import print_images_to_process
        from clinica.utils.stream import cprint

        root = dirname(abspath(join(abspath(__file__), pardir, pardir)))
        path_to_mask = join(root, 'resources', 'masks')
        self.ref_template = join(
                path_to_mask, 'mni_icbm152_t1_tal_nlin_sym_09c.nii')
        self.ref_crop = join(path_to_mask, 'ref_cropped_template.nii.gz')
        url1 = "https://aramislab.paris.inria.fr/files/data/img_t1_linear/ref_cropped_template.nii.gz"
        url2 = "https://aramislab.paris.inria.fr/files/data/img_t1_linear/mni_icbm152_t1_tal_nlin_sym_09c.nii"

        if not(exists(self.ref_template)):
            try:
                fetch_file(url2, self.ref_template)
            except IOError as err:
                cprint('Unable to download required template (mni_icbm152) for processing:', err)

        if not(exists(self.ref_crop)):
            try:
                fetch_file(url1, self.ref_crop)
            except IOError as err:
                cprint('Unable to download required template (ref_crop) for processing:', err)

        # Inputs from anat/ folder
        # ========================
        # T1w file:
        try:
            t1w_files = clinica_file_reader(
                    self.subjects,
                    self.sessions,
                    self.bids_directory,
                    T1W_NII)
        except ClinicaException as e:
            err = 'Clinica faced error(s) while trying to read files in your BIDS directory.\n' + str(e)
            raise ClinicaBIDSError(err)

        if len(self.subjects):
            print_images_to_process(self.subjects, self.sessions)
            cprint('The pipeline will last approximately 6 minutes per image.')

        read_node = npe.Node(
                name="ReadingFiles",
                iterables=[
                    ('t1w', t1w_files),
                    ],
                synchronize=True,
                interface=nutil.IdentityInterface(
                    fields=self.get_input_fields())
                )
        self.connect([
            (read_node, self.input_node, [('t1w', 't1w')]),
            ])

    def build_output_node(self):
        """Build and connect an output node to the pipeline.
        """
        import nipype.interfaces.utility as nutil
        from nipype.interfaces.io import DataSink
        import nipype.pipeline.engine as npe
        from clinica.utils.nipype import fix_join
        from .t1_linear_utils import (container_from_filename, get_substitutions_datasink)

        # Writing node
        write_node = npe.Node(
                name="WriteCaps",
                interface=DataSink()
                )
        write_node.inputs.base_directory = self.caps_directory
        write_node.inputs.parameterization = False

        # Other nodes
        # =====================================
        # Get substitutions to rename files
        get_ids = npe.Node(
                interface=nutil.Function(
                    input_names=['bids_file'],
                    output_names=['image_id_out', 'subst_ls'],
                    function=get_substitutions_datasink),
                name="GetIDs")
        # Find container path from t1w filename
        container_path = npe.Node(
                nutil.Function(
                    input_names=['bids_or_caps_filename'],
                    output_names=['container'],
                    function=container_from_filename),
                name='ContainerPath')
        self.connect([
            (self.input_node, container_path, [('t1w', 'bids_or_caps_filename')]),
            (container_path, write_node, [(('container', fix_join, 't1_linear'), 'container')]),
            (self.output_node, get_ids, [('image_id', 'bids_file')]),
            (get_ids, write_node, [('subst_ls', 'substitutions')]),
            (get_ids, write_node, [('image_id_out', '@image_id')]),
            (self.output_node, write_node, [('outfile_reg', '@outfile_reg')]),
            (self.output_node, write_node, [('affine_mat', '@affine_mat')]),
            ])

        if (self.parameters.get('crop_image')):
            self.connect([
                (self.output_node, write_node, [('outfile_crop', '@outfile_crop')]),
                ])

    def build_core_nodes(self):
        """Build and connect the core nodes of the pipeline.
        """
        import nipype.interfaces.utility as nutil
        import nipype.pipeline.engine as npe
        from clinica.utils.filemanip import get_filename_no_ext
        from nipype.interfaces import ants
        from .t1_linear_utils import crop_nifti

        image_id_node = npe.Node(
                interface=nutil.Function(
                    input_names=['filename'],
                    output_names=['image_id'],
                    function=get_filename_no_ext),
                name='ImageID'
                )

        # The core (processing) nodes
        # =====================================

        # 1. N4biascorrection by ANTS. It uses nipype interface.
        n4biascorrection = npe.Node(
                name='n4biascorrection',
                interface=ants.N4BiasFieldCorrection(
                    dimension=3,
                    save_bias=True,
                    bspline_fitting_distance=600
                    )
                )

        # 2. `RegistrationSynQuick` by *ANTS*. It uses nipype interface.
        ants_registration_node = npe.Node(
                name='antsRegistrationSynQuick',
                interface=ants.RegistrationSynQuick()
                )
        ants_registration_node.inputs.fixed_image = self.ref_template
        ants_registration_node.inputs.transform_type = 'a'
        ants_registration_node.inputs.dimension = 3

        # 3. Crop image (using nifti). It uses custom interface, from utils file

        cropnifti = npe.Node(
                name='cropnifti',
                interface=nutil.Function(
                    function=crop_nifti,
                    input_names=['input_img', 'ref_crop'],
                    output_names=['output_img', 'crop_template']
                    )
                )
        cropnifti.inputs.ref_crop = self.ref_crop

        # Connection
        # ==========
        self.connect([
            (self.input_node, image_id_node, [('t1w', 'filename')]),
            (self.input_node, n4biascorrection, [('t1w', 'input_image')]),
            (n4biascorrection, ants_registration_node, [('output_image', 'moving_image')]),
            (image_id_node , ants_registration_node, [('image_id', 'output_prefix')]),

            # Connect to DataSink
            (image_id_node, self.output_node, [('image_id', 'image_id')]),
            (ants_registration_node, self.output_node, [('out_matrix', 'affine_mat')]),
            (n4biascorrection, self.output_node, [('output_image', 'outfile_corr')]),
            (ants_registration_node, self.output_node, [('warped_image', 'outfile_reg')]),
            ])
        if (self.parameters.get('crop_image')):
            self.connect([
                (ants_registration_node, cropnifti, [('warped_image', 'input_img')]),
                (cropnifti, self.output_node, [('output_img', 'outfile_crop')]),
                ])
