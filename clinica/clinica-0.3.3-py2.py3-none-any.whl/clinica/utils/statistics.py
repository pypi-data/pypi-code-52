# coding: utf8


def statistics_on_atlas(in_normalized_map, in_atlas, out_file=None):
    """
    Compute statistics of a map on an atlas.

    Given an atlas image with a set of ROIs, this function computes the mean of
    a normalized map (e.g. GM segmentation, FA map from DTI, etc.) on each ROI.

    Args:
        in_normalized_map (str): File containing a scalar image registered
            on the atlas.
        in_atlas (:obj: AbstractClass): An atlas with a set of ROI. These ROI
            are used to compute statistics.
        out_file (Optional[str]): Name of the output file.

    Returns:
        out_file (str): TSV file containing the statistics (content of the
            columns: label, mean scalar, std of the scalar', number of voxels).
    """
    from clinica.utils.atlas import AtlasAbstract
    import nibabel as nib
    import numpy as np
    import pandas
    import os.path as op
    from clinica.utils.stream import cprint

    if not isinstance(in_atlas, AtlasAbstract):
        raise Exception("Atlas element must be an AtlasAbstract type")

    if out_file is None:
        fname, ext = op.splitext(op.basename(in_normalized_map))
        if ext == ".gz":
            fname, ext2 = op.splitext(fname)
            ext = ext2 + ext
        out_file = op.abspath("%s_statistics_%s.tsv"
                              % (fname, in_atlas.get_name_atlas()))

    atlas_labels = nib.load(in_atlas.get_atlas_labels())
    atlas_labels_data = atlas_labels.get_data()

    img = nib.load(in_normalized_map)
    img_data = img.get_data()

    atlas_correspondance = pandas.io.parsers.read_csv(in_atlas.get_tsv_roi(), sep='\t')
    label_name = list(atlas_correspondance.roi_name)
    label_value = list(atlas_correspondance.roi_value)  # TODO create roi_value column in lut_*.txt and remove irrelevant RGB information

    mean_signal_value = []
    for label in label_value:
        current_mask_label = atlas_labels_data == label
        masked_data = np.array(img_data, copy=True)
        masked_data[np.invert(current_mask_label)] = 0
        mean_signal_value.append(np.sum(masked_data) / np.sum(current_mask_label))

    try:
        data = pandas.DataFrame({'label_name': label_name,
                                 'mean_scalar': mean_signal_value
                                 })
        data.to_csv(out_file, sep='\t', index=True, encoding='utf-8')
    except Exception as e:
        cprint("Impossible to save %s with pandas" % out_file)
        raise e

    return out_file
