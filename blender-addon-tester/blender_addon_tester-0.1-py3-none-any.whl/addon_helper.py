import os
import sys
import re
import time
import zipfile
import shutil
import bpy


def zip_addon(addon, addon_dir):
    """ Zips 'addon' dir or '.py' file to 'addon.zip' if not yet zipped, then moves the archive to 'addon_dir'.
    :param addon     Absolute or relative path to a directory to zip or a .zip file.
    :param addon_dir Path to Blender's addon directory to move the zipped archive to.
    :return (bpy_module, zip_file) Tuple of strings - an importable module name, an addon zip file path.
    """
    already_zipped = False

    addon_path = os.path.realpath(addon)
    addon_basename = os.path.basename(addon_path)

    if addon_basename.endswith(".zip"):
        already_zipped = True

    if os.path.isdir(addon_dir):
        shutil.rmtree(addon_dir)
    os.mkdir(addon_dir)

    print("Addon dir is - {0}".format(os.path.realpath(addon_dir)))
    if not already_zipped:
        bpy_module = re.sub(".py", "", addon_basename)
        zfile = os.path.realpath(bpy_module + ".zip")

        print("Future zip path is - {0}".format(zfile))

        print("Zipping addon - {0}".format(bpy_module))

        zf = zipfile.ZipFile(zfile, "w")
        if os.path.isdir(addon):
            for dirname, subdirs, files in os.walk(addon):
                zf.write(dirname)
                for filename in files:
                    zf.write(os.path.join(dirname, filename))
        else:
            zf.write(addon)
        zf.close()
    else:
        zfile = addon_path
        print("Detected zip path is - {0}. No need to zip the addon beforehand.".format(zfile))

        bpy_module = addon_basename.split(".zip")[0]

    return (bpy_module, zfile)


def change_addon_dir(bpy_module, zfile, addon_dir):
    print("Change addon dir - {0}".format(addon_dir))

    if (2, 80, 0) < bpy.app.version:
        bpy.context.preferences.filepaths.script_directory = addon_dir
        bpy.utils.refresh_script_paths()
        bpy.ops.preferences.addon_install(overwrite=True, filepath=zfile)
        bpy.ops.preferences.addon_enable(module=bpy_module)
    else:
        bpy.context.user_preferences.filepaths.script_directory = addon_dir
        bpy.utils.refresh_script_paths()
        bpy.ops.wm.addon_install(overwrite=True, filepath=zfile)
        bpy.ops.wm.addon_enable(module=bpy_module)


def cleanup(addon, bpy_module, addon_dir):
    print("Cleaning up - {}".format(bpy_module))
    if (2, 80, 0) < bpy.app.version:
        bpy.ops.preferences.addon_disable(module=bpy_module)
    else:
        bpy.ops.wm.addon_disable(module=bpy_module)
    if os.path.isdir(addon_dir):
        shutil.rmtree(addon_dir)


def get_version(bpy_module):
    mod = sys.modules[bpy_module]
    return mod.bl_info.get("version", (-1, -1, -1))
