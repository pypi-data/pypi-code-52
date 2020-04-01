"""Honeybee_energy configurations.

Import this into every module where access configurations are needed.

Usage:

.. code-block:: python

    from honeybee_energy.config import folders
    print(folders.energyplus_path)
    print(folders.openstudio_path)
    folders.energyplus_path = "C:/EnergyPlusV9-0-1"
"""
import ladybug.config as lb_config
import honeybee.config as hb_config

import os
import platform
import json
import pkgutil

# Matrix matching OpenStudio version to EnergyPlus + Radiance version
# https://github.com/NREL/OpenStudio/wiki/OpenStudio-Version-Compatibility-Matrix
OPENSTUDIO_VERSIONS = {
    (2, 9, 1): (9, 2, 0),
    (2, 9, 0): (9, 2, 0),
    (2, 8, 1): (9, 1, 0),
    (2, 8, 0): (9, 1, 0),
    (2, 7, 1): (9, 0, 1),
    (2, 7, 0): (9, 0, 1),
    (2, 6, 1): (8, 9, 0),
    (2, 6, 0): (8, 9, 0),
    (2, 5, 2): (8, 9, 0),
    (2, 5, 1): (8, 9, 0),
    (2, 5, 0): (8, 9, 0),
    (2, 4, 3): (8, 9, 0),
    (2, 4, 1): (8, 8, 0),
    (2, 4, 0): (8, 8, 0),
    (2, 3, 1): (8, 8, 0),
    (2, 3, 0): (8, 8, 0),
    (2, 2, 2): (8, 8, 0),
    (2, 2, 1): (8, 7, 0),
    (2, 2, 0): (8, 7, 0),
    (2, 1, 2): (8, 7, 0),
    (2, 1, 1): (8, 7, 0),
    (2, 1, 0): (8, 7, 0),
    (2, 0, 5): (8, 7, 0),
    (2, 0, 4): (8, 6, 0),
    (2, 0, 3): (8, 6, 0),
    (2, 0, 2): (8, 6, 0),
    (2, 0, 1): (8, 6, 0),
    (2, 0, 0): (8, 6, 0)
}


class Folders(object):
    """Honeybee_energy folders.

    Args:
        config_file: The path to the config.json file from which folders are loaded.
            If None, the config.json module included in this package will be used.
            Default: None.
        mute: If False, the paths to the various folders will be printed as they
            are found. If True, no printing will occur upon initialization of this
            class. Default: True.

    Properties:
        * openstudio_path
        * openstudio_exe
        * openstudio_version
        * energyplus_path
        * energyplus_exe
        * energyplus_version
        * energy_model_measure_path
        * standards_data_folder
        * construction_lib
        * constructionset_lib
        * schedule_lib
        * programtype_lib
        * standards_extension_folders
        * config_file
        * mute
    """

    def __init__(self, config_file=None, mute=True):
        self.mute = bool(mute)  # set the mute value
        self.config_file  = config_file  # load paths from the config JSON file

    @property
    def openstudio_path(self):
        """Get or set the path to OpenStudio installation folder.

        This is the "bin" directory for OpenStudio installation (the one that
        contains the openstudio executable file).
        """
        return self._openstudio_path

    @openstudio_path.setter
    def openstudio_path(self, path):
        if not path:  # check the default installation location
            path = self._find_openstudio_folder()
        exe_name = 'openstudio.exe' if os.name == 'nt'  else 'openstudio'
        os_exe_file = os.path.join(path, exe_name) if path is not None else None

        if path:  # check that the OpenStudio executable exists in the path
            assert os.path.isfile(os_exe_file), \
                '{} is not a valid path to an openstudio installation.'.format(path)

        #set the openstudio_path
        self._openstudio_path = path
        self._openstudio_exe = os_exe_file
        self._openstudio_version = self._os_version_from_path(path)
        if path and not self.mute:
            print("Path to OpenStudio is set to: %s" % path)

    @property
    def openstudio_exe(self):
        """Get the path to the executable openstudio file."""
        return self._openstudio_exe
    
    @property
    def openstudio_version(self):
        """Get a tuple for the version of openstudio (eg. (2, 9, 1)).

        This will be None if the version could not be sensed or if no OpenStudio
        installation was found.
        """
        return self._openstudio_version

    @property
    def energyplus_path(self):
        """Get or set the path to EnergyPlus installation folder."""
        return self._energyplus_path

    @energyplus_path.setter
    def energyplus_path(self, path):
        self._energyplus_version = None
        if not path:  # check the default installation location
            path = self._find_energyplus_folder()
        exe_name = 'energyplus.exe' if os.name == 'nt'  else 'energyplus'
        ep_exe_file = os.path.join(path, exe_name) if path is not None else None

        if path:  # check that the Energyplus executable exists in the installation
            assert os.path.isfile(ep_exe_file), \
                '{} is not a valid path to an energyplus installation.'.format(path)

        # set the energyplus_path
        self._energyplus_path = path
        self._energyplus_exe = ep_exe_file
        if path and not self.mute:
            print("Path to EnergyPlus is set to: %s" % self._energyplus_path)

    @property
    def energyplus_exe(self):
        """Get the path to the executable energyplus file."""
        return self._energyplus_exe

    @property
    def energyplus_version(self):
        """Get a tuple for the version of energyplus (eg. (9, 2, 0)).

        This will be None if the version could not be sensed or if no EnergyPlus
        installation was found.
        """
        return self._energyplus_version

    @property
    def energy_model_measure_path(self):
        """Get or set the path to the energy_model_measure translating to OpenStudio.

        This folder must have the following sub-folders in order to be valid:

        * from_honeybee - ruby library with modules for model translation to OpenStudio.
        * measures - folder with the actual measures that run the translation.
        * files - folder containing the openapi schemas
        """
        return self._energy_model_measure_path

    @energy_model_measure_path.setter
    def energy_model_measure_path(self, path):
        if not path:  # check the default locations of the energy_model_measure
            path = self._find_energy_model_measure_path()

        # check that the library's sub-folders exist
        if path:
            assert os.path.isdir(os.path.join(path, 'from_honeybee')), '{} lacks a ' \
                '"from_honeybee" folder for the translation ruby library.'.format(path)
            assert os.path.isdir(os.path.join(path, 'measures')), \
                '{} lacks a "measures" folder.'.format(path)

        # set the energy_model_measure_path
        self._energy_model_measure_path = path
        if path and not self.mute:
            print('Path to the energy_model_measure is set to: '
                    '{}'.format(self._energy_model_measure_path))

    @property
    def standards_data_folder(self):
        """Get or set the path to the library of standards loaded to honeybee_energy.lib.

        This folder must have the following sub-folders in order to be valid:

        * constructions - folder with IDF files for materials + constructions.
        * constructionsets - folder with JSON files of abridged ConstructionSets.
        * schedules - folder with IDF files for schedules.
        * programtypes - folder with JSON files of abridged ProgramTypes.
        """
        return self._standards_data_folder

    @standards_data_folder.setter
    def standards_data_folder(self, path):
        if not path:  # check the default locations of the template library
            path = self._find_standards_data_folder()

        # gather all of the sub folders underneath the master folder
        self._construction_lib, self._constructionset_lib, self._schedule_lib, \
            self._programtype_lib = self._check_standards_folder(path)

        # set the standards_data_folder
        self._standards_data_folder = path
        if path and not self.mute:
            print('Path to the standards_data_folder is set to: '
                    '{}'.format(self._standards_data_folder))

    @property
    def standards_extension_folders(self):
        """Get or set an array of paths to standards extensions loaded to the lib.

        Each extension folder folder must have the following sub-folders:

        * constructions - folder with honeybee JSON files for materials + constructions.
            It should have the following 4 JSON files:
            opaque_material, opaque_construction, window_material, window_construction.
        * constructionsets - folder with honeybee JSON files of abridged ConstructionSets.
        * schedules - folder with honeybee JSON files for schedules.
        * programtypes - folder with honeybee JSON files of abridged ProgramTypes.
        """
        return tuple(self._standards_extension_folders)

    @standards_extension_folders.setter
    def standards_extension_folders(self, folders):
        if not folders:  # check the default locations
            folders = self._find_standards_extension_folders()

        # check that any extensions have the proper sub-folders
        for path in folders:
            self._check_standards_folder(path)
            if not self.mute:
                print('Standards extension folder found: {}'.format(path))

        # set the standards_data_folder
        self._standards_extension_folders = folders

    @property
    def construction_lib(self):
        """Get the path to the construction library in the standards_data_folder."""
        return self._construction_lib

    @property
    def constructionset_lib(self):
        """Get the path to the constructionset library in the standards_data_folder."""
        return self._constructionset_lib

    @property
    def schedule_lib(self):
        """Get the path to the schedule library in the standards_data_folder."""
        return self._schedule_lib

    @property
    def programtype_lib(self):
        """Get the path to the programtype library in the standards_data_folder."""
        return self._programtype_lib

    @property
    def config_file(self):
        """Get or set the path to the config.json file from which folders are loaded.

        Setting this to None will result in using the config.json module included
        in this package.
        """
        return self._config_file

    @config_file.setter
    def config_file(self, cfg):
        if cfg is None:
            cfg = os.path.join(os.path.dirname(__file__), 'config.json')
        self._load_from_file(cfg)
        self._config_file = cfg

    def _load_from_file(self, file_path):
        """Set all of the the properties of this object from a config JSON file.

        Args:
            file_path: Path to a JSON file containing the file paths. A sample of this
                JSON is the config.json file within this package.
        """
        # check the default file path
        assert os.path.isfile(str(file_path)), \
            ValueError('No file found at {}'.format(file_path))

        # set the default paths to be all blank
        default_path = {
            "energyplus_path": r'',
            "openstudio_path": r'',
            "energy_model_measure_path": r'',
            "standards_data_folder": r'',
            "standards_extension_folders": []
        }

        with open(file_path, 'r') as cfg:
            try:
                paths = json.load(cfg)
            except Exception as e:
                print('Failed to load paths from {}.\n{}'.format(file_path, e))
            else:
                for key, p in paths.items():
                    if isinstance(key, list) or not key.startswith('__'):
                        try:
                            default_path[key] = p.strip()
                        except AttributeError:
                            default_path[key] = p

        # set paths for energyplus and openstudio installations
        self.openstudio_path = default_path["openstudio_path"]
        self.energyplus_path = default_path["energyplus_path"]

        # set the paths for the energy_model_measure
        self.energy_model_measure_path = default_path["energy_model_measure_path"]

        # set path for the standards_data_folder
        self.standards_data_folder = default_path["standards_data_folder"]

        # set path for the standards_extension_folders
        self.standards_extension_folders = default_path["standards_extension_folders"]

    def _find_energy_model_measure_path(self):
        """Find the energy_model_measure_path in its default location.

        First, the OpenStudio installation will be checked to see if there is a
        compatible version of the measure installed for that version of OpenStudio.
        If nothing is found there, the root of the ladybug_tools folder will be
        checked for an energy_model_measure directory.
        """
        # first check if there's a version installed in the OpenStudio folder
        if self.openstudio_path:
            os_root = os.path.split(self.openstudio_path)[0]
            measure_path = os.path.join(os_root, 'energy_model_measure', 'lib')
            if os.path.isdir(measure_path):
                return measure_path

        # then, check the root of the ladybug_tools folder
        lb_install = lb_config.folders.ladybug_tools_folder
        if os.path.isdir(lb_install):
            measure_path = os.path.join(lb_install, 'energy_model_measure', 'lib')
            if os.path.isdir(measure_path):
                return measure_path

        return None  # No energy model measure is installed

    def _find_energyplus_folder(self):
        """Find the most recent EnergyPlus installation in its default location.

        This method will first attempt to return the path of the EnergyPlus that
        installs with OpenStudio and, if none are found, it will search for a
        standalone installation of EnergyPlus.

        Returns:
            File directory and full path to executable in case of success.
            None in case of failure.
        """
        def getversion(energyplus_path):
            """Get digits for the version of EnergyPlus."""
            ver = ''.join(s for s in energyplus_path if (s.isdigit() or s == '-'))
            return sum(int(d) * (10 ** i) for i, d in enumerate(reversed(ver.split('-'))))

        # first check for the EnergyPlus that comes with OpenStudio
        ep_path = None
        if self.openstudio_path is not None and os.path.isdir(os.path.join(
                os.path.split(self.openstudio_path)[0], 'EnergyPlus')):
            ep_path = os.path.join(os.path.split(self.openstudio_path)[0], 'EnergyPlus')
            if self.openstudio_version:
                try:
                    self._energyplus_version = OPENSTUDIO_VERSIONS[self.openstudio_version]
                except KeyError:
                    pass  # Newer version and matrix hasn't been updated

        # then check the default location where standalone EnergyPlus is installed
        elif os.name == 'nt':  # search the C:/ drive on Windows
            ep_folders = ['C:\\{}'.format(f) for f in os.listdir('C:\\')
                          if (f.lower().startswith('energyplus') and
                              os.path.isdir('C:\\{}'.format(f)))]
        elif platform.system() == 'Darwin':  # search the Applications folder on Mac
            ep_folders = ['/Applications/{}'.format(f) for f in os.listdir('/Applications/')
                          if (f.lower().startswith('energyplus') and
                              os.path.isdir('/Applications/{}'.format(f)))]
        elif platform.system() == 'Linux':  # search the usr/local folder
            ep_folders = ['/usr/local/{}'.format(f) for f in os.listdir('/usr/local/')
                          if (f.lower().startswith('energyplus') and
                              os.path.isdir('/usr/local/{}'.format(f)))]
        else:  # unknown operating system
            ep_folders = None

        if not ep_path and not ep_folders:  # No EnergyPlus installations were found
            return None
        elif not ep_path: # get the most recent version of energyplus that was found
            ep_path = sorted(ep_folders, key=getversion, reverse=True)[0]
            self._energyplus_version = self._ep_version_from_path(ep_path)
        return ep_path

    @staticmethod
    def _ep_version_from_path(ep_path):
        """Extract a tuple for the version of EnergyPlus from the path.

        Args:
            ep_path: File directory to EnergyPlus.

        Returns:
            Tuple of integers for the version in case of success.
            None, None in case of failure.
        """
        if not ep_path:
            return None
        ver = ''.join(s for s in ep_path if (s.isdigit() or s == '-'))
        if ver:  # version was found in the file path name
            return tuple(int(d) for d in ver.split('-'))
        return None

    @staticmethod
    def _find_openstudio_folder():
        """Find the most recent OpenStudio installation in its default location.

        Returns:
            File directory and full path to executable in case of success.
            None in case of failure.
        """
        def getversion(openstudio_path):
            """Get digits for the version of OpenStudio."""
            ver = ''.join(s for s in openstudio_path if (s.isdigit() or s == '.'))
            return sum(int(d) * (10 ** i) for i, d in enumerate(reversed(ver.split('.'))))

        # first check if there's a version installed in the ladybug_tools folder
        lb_install = lb_config.folders.ladybug_tools_folder
        os_folders = []
        if os.path.isdir(lb_install):
            os_folders = [os.path.join(lb_install, f) for f in os.listdir(lb_install)
                          if (f.lower().startswith('openstudio') and
                              os.path.isdir(os.path.join(lb_install, f)))]

        # then check the default installation folders
        if len(os_folders) != 0:
            pass  # we found a version of openstudio in the ladybug_tools folder
        elif os.name == 'nt':  # search the C:/ drive on Windows
            os_folders = ['C:\\{}'.format(f) for f in os.listdir('C:\\')
                          if (f.lower().startswith('openstudio') and
                              os.path.isdir('C:\\{}'.format(f)))]
        elif platform.system() == 'Darwin':  # search the Applications folder on Mac
            os_folders = ['/Applications/{}'.format(f) for f in os.listdir('/Applications/')
                          if (f.lower().startswith('openstudio') and
                              os.path.isdir('/Applications/{}'.format(f)))]
        elif platform.system() == 'Linux':  # search the usr/local folder
            os_folders = ['/usr/local/{}'.format(f) for f in os.listdir('/usr/local/')
                          if (f.lower().startswith('openstudio') and
                              os.path.isdir('/usr/local/{}'.format(f)))]
        else:  # unknown operating system
            os_folders = None

        if not os_folders:  # No Openstudio installations were found
            return None

        # get the most recent version of OpenStudio that was found
        os_path = sorted(os_folders, key=getversion, reverse=True)[0]

        return os.path.join(os_path, 'bin')

    @staticmethod
    def _os_version_from_path(os_path):
        """Extract a tuple for the version of OpenStudio from the path.

        Args:
            os_path: File directory to OpenStudio.

        Returns:
            Tuple of integers for the version in case of success.
            None, None in case of failure.
        """
        if not os_path:
            return None
        ver = ''.join(s for s in os_path if (s.isdigit() or s == '.'))
        if ver:  # version was found in the file path name
            return tuple(int(d) for d in ver.split('.'))
        return None

    @staticmethod
    def _find_standards_data_folder():
        """Find the user template library in its default location.

        The ladybug_tools/resources/standards/honeybee_standards folder will be
        checked first, which can conatain libraries that are not overwritten
        with the update of the honeybee_energy package. If no such folder is found,
        this method defaults to the lib/library/ folder within this package.
        """
        # first check the ladybug_tools installation folder were permanent lib is
        lb_install = lb_config.folders.ladybug_tools_folder
        if os.path.isdir(lb_install):
            lib_folder = os.path.join(
                lb_install, 'resources', 'standards', 'honeybee_standards')
            if os.path.isdir(lib_folder):
                return lib_folder

        # default to the library folder that installs with this Python package
        return os.path.join(os.path.dirname(__file__), 'lib', 'data')

    @staticmethod
    def _find_standards_extension_folders():
        """Find the standards extension folders in their default locations.

        Extension folders are expected to start with the words "honeybee_energy"
        and end with the words "standards" (eg. honeybee_energy_cibse_standards).

        The ladybug_tools/resources/standards folder will be checked first, which
        can conatain libraries that are not overwritten with the update of the
        honeybee_energy package.
        If no folders are found, this method will look for any Python packages
        sitting next to honeybee_energy that follow the naming criteria above.
        """
        standards_extensions = []
        # first check the ladybug_tools installation folder were permanent lib is
        lb_install = lb_config.folders.ladybug_tools_folder
        std_folder = os.path.join(lb_install, 'resources', 'standards')
        if os.path.isdir(std_folder):
            for folder in os.listdir(std_folder):
                if folder.endswith('standards') and folder.startswith('honeybee_energy'):
                    lib_folder = os.path.join(std_folder, folder)
                    if os.path.isdir(lib_folder):
                        standards_extensions.append(lib_folder)
        # then check next to the Python library
        if len(standards_extensions) == 0:
            for finder, name, ispkg in pkgutil.iter_modules():
                if name.endswith('standards') and name.startswith('honeybee_energy'):
                    lib_folder = os.path.join(finder.path, name, 'data')
                    if os.path.isdir(lib_folder):
                        standards_extensions.append(lib_folder)
        return standards_extensions

    @staticmethod
    def _check_standards_folder(path):
        """Check that a standards data sub-folders exist."""
        if not path:  # first check that a path exists
            return [None] * 4

        # gather all of the sub folders underneath the master folder
        _construction_lib = os.path.join(path, 'constructions') if path else None
        _constructionset_lib = os.path.join(path, 'constructionsets') if path else None
        _schedule_lib = os.path.join(path, 'schedules') if path else None
        _programtype_lib = os.path.join(path, 'programtypes') if path else None

        if path:
            assert os.path.isdir(_construction_lib), \
                '{} lacks a "constructions" folder.'.format(path)
            assert os.path.isdir(_constructionset_lib), \
                '{} lacks a "constructionsets" folder.'.format(path)
            assert os.path.isdir(_schedule_lib), \
                '{} lacks a "schedules" folder.'.format(path)
            assert os.path.isdir(_programtype_lib), \
                '{} lacks a "programtypes" folder.'.format(path)

        return _construction_lib, _constructionset_lib, _schedule_lib, _programtype_lib


"""Object possesing all key folders within the configuration."""
folders = Folders(mute=True)
