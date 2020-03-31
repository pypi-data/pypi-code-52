# This file exists within 'dob-bright':
#
#   https://github.com/hotoffthehamster/dob-bright
#
# Copyright © 2019-2020 Landon Bouma. All rights reserved.
#
# This program is free software:  you can redistribute it  and/or  modify it under the
# terms of the GNU General Public License as published by the Free Software Foundation,
# either version 3  of the License,  or  (at your option)  any later version  (GPLv3+).
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY;  without even the implied warranty of MERCHANTABILITY or  FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU  General  Public  License  for  more  details.
#
# If you lost the GNU General Public License that ships with this software
# repository (read the 'LICENSE' file), see <http://www.gnu.org/licenses/>.

import json
import os

from gettext import gettext as _

from config_decorator import ConfigDecorator, KeyChainedValue

from nark.config import ConfigRoot
from nark.config.log_levels import get_log_level_safe, must_verify_log_level
from nark.helpers.parsing import FACT_METADATA_SEPARATORS

from .app_dirs import AppDirs

__all__ = (
    'decorate_config',
    'DobConfigurableDev',
    'DobConfigurableEditor',
    'DobConfigurableFact',
    'DobConfigurableLog',
    'DobConfigurableTerm',
    # PRIVATE:
    # '_styling_file_path',
)


KeyChainedValue._envvar_prefix = 'DOB_'


# ***
# *** Client (dob) Config.
# ***

def _styling_file_path(basename):
    dirname = AppDirs.user_config_dir
    subdir = 'styling'
    # E.g., /home/user/config/.dob/styling/{basename}
    return os.path.join(dirname, subdir, basename)


@ConfigRoot.section('editor')
class DobConfigurableEditor(object):
    """"""

    def __init__(self, *args, **kwargs):
        # See comment in NarkConfigurable:
        #   Cannot super because decorator shenanigans.
        # DEATH: super(DobConfigurableEditor, self).__init__(*args, **kwargs)
        # FIXME/2019-11-30 17:47: Could test again: (lb): I might have fixed issue.
        pass

    # ***

    @property
    @ConfigRoot.setting(
        _("If True, center the interface in the terminal (on `dob edit`)"),
    )
    def centered(self):
        return False

    # ***

    @property
    @ConfigRoot.setting(
        # FIXME/2019-11-29: (lb): Help Docs: Add command to list dob + pygments.lexers.
        _("dob or Pygments lexer. See: https://pygments.org/docs/lexers/"),
    )
    def lexer(self):
        # (lb): I'm a reSTie, personally, so let's just default to that.
        # (Not to dishonor other markups, I'm friends with markdownies,
        # I even LaTeXeD once in my life, and let's not talk about that
        # one time I was into this really weird markup called Textile.)
        # MAYBE/2019-11-29: (lb): Perhaps default to '' (and move this to *my* config).
        return 'RstLexer'

    # ***

    @property
    @ConfigRoot.setting(
        _("UX style: '' or 'default' applies none;"
          "'night', 'light', or 'color' applies builtin;"
          " or name your own (see: styles_fpath)."),
    )
    def styling(self):
        # Do not specify a style (or specify 'default') so that the UX is not
        # styled, but uses the current terminal color scheme.
        return ''

    # ***

    @property
    @ConfigRoot.setting(
        # FIXME/2019-11-30: Backlog entry: how best to split long help string.
        # - One option: Split here with explicit newlines. Works well for:
        #                 dob config dump -T tabulate
        #               but does not work with -T friendly
        #               - We could default to tabulate...
        #                 or maybe help() callback that customizes
        #                 text based on -T option?
        # - Another option: Truncate after first period '.' on global dob-bright-dump,
        #                    but include complete help on dob-bright-dump-setting (e.g.,)
        _("Path to file containing newline-separated ‘act@gory’ and ‘#tag’\n"
          "names to omit from completions and suggestions (regex-aware)."),
        name='ignore_fpath',
    )
    def ignore_list_path(self):
        # E.g., /home/user/config/.dob/styling/ignore.list
        return _styling_file_path(basename='ignore.list')

    # ***

    @property
    @ConfigRoot.setting(
        _("Path to file containing UX styles used by “editor.styling”."),
        name='styles_fpath',
    )
    def styles_conf_path(self):
        # E.g., /home/user/config/.dob/styling/styles.conf
        return _styling_file_path(basename='styles.conf')

    # ***

    @property
    @ConfigRoot.setting(
        _("Path to file defining object matching used to stylize UX."),
        name='stylit_fpath',
    )
    def stylit_conf_path(self):
        # E.g., /home/user/config/.dob/styling/queries.conf
        return _styling_file_path(basename='stylit.conf')

    # ***


# ***

@ConfigRoot.section('fact')
class DobConfigurableFact(object):
    """"""

    def __init__(self, *args, **kwargs):
        pass

    # ***

    @property
    @ConfigRoot.setting(
        _("Acceptable separator(s) to delimit Fact meta data from description."),
    )
    def separators(self):
        # Rather than `return ''` and act like there are no separators, show
        # the default value that nark uses, so that user are better educated.
        # FYI: json.dumps([",", ":"]) → '[",", ":"]'
        return json.dumps(FACT_METADATA_SEPARATORS)


# ***

@ConfigRoot.section('dev')
class DobConfigurableDev(object):
    """"""

    def __init__(self, *args, **kwargs):
        pass

    # ***

    @property
    @ConfigRoot.setting(
        _("The log level for frontend (dob) squaller"
          " (using Python logging library levels)"),
        validate=must_verify_log_level,
        conform=get_log_level_safe,
    )
    def cli_log_level(self):
        return 'WARNING'

    # ***

    @property
    @ConfigRoot.setting(
        _("If True, enables features for developing dob"
          " (e.g., stop at REPL on affirm faults)."),
    )
    def catch_errors(self):
        return False


# ***

@ConfigRoot.section('log')
class DobConfigurableLog(object):
    """"""

    def __init__(self, *args, **kwargs):
        pass

    # ***

    # MAYBE/2019-11-29: (lb): I'm not sure utility of setting logfile name,
    # but not the path. Perhaps add log.dirname option.
    # - Or
    @property
    @ConfigRoot.setting(
        # MAYBE/2019-11-29: Resolve appdirs path -- or somehow show user full log path.
        # Or, if (hypothetical) log.dirname option added, substitute in help text here.
        _("Filename of dob log under AppDirs.user_log_dir"),
    )
    def filename(self):
        return 'dob.log'

    # ***

    # User should not set logfile_path in config, because it's
    # generated, but we make it a pseudo-setting so the code can
    # access just the same as other settings (and the value depends
    # on another config value, the log_filename, so it sorta is a
    # config value, just a derived one).
    @property
    @ConfigRoot.setting(
        _('Generated value.'),
        ephemeral=True,
    )
    def filepath(self):
        if self is None:
            # If called on class definition, before kcv._section set, return
            # empty string, which indicates the value type. However, because
            # ephemeral=True, _deduce_value_type won't call this method with
            # self set to None -- meaning, this return statement technically
            # unreachable. But we'll still keep it, for completeness.
            return ''
        log_dir = AppDirs.user_log_dir
        # Note that self is the root ConfigDecorator, not the DobConfigurableLog.
        log_filename = self['filename']
        return os.path.join(log_dir, log_filename)

    # ***

    @property
    @ConfigRoot.setting(
        _("If True, use color in log files (useful if tailing logs in terminal)"),
    )
    def use_color(self):
        return False

    # ***

    @property
    @ConfigRoot.setting(
        _("If True, send logs to the console, not the file"),
    )
    def use_console(self):
        return True


# ***

@ConfigRoot.section('term')
class DobConfigurableTerm(object):
    """"""

    def __init__(self, *args, **kwargs):
        pass

    # ***

    @property
    @ConfigRoot.setting(
        _("Path to directory where export files are created"),

        # FIXME/2019-11-17 00:56: Nothing uses export_path.
        #   So hidden for now. Delete later, or implement.
        hidden=True,
    )
    def export_path(self):
        """
        Return path to save exports to.
        File extension will be added by export method.
        """
        # FIXME: Not sure who this'll be used... maybe two separate config
        #        values, one editable and one generated, like log_filename
        #        and logfile_path. But first, we need a feature that exports!
        #        Until then... either keep this setting hidden, or delete it!
        return os.path.join(AppDirs.user_data_dir, 'export')

    # ***

    @property
    @ConfigRoot.setting(
        _("The filename suffix to tell EDITOR so it can determine highlighting"),
    )
    def editor_suffix(self):
        return ''

    # ***

    @property
    @ConfigRoot.setting(
        _("If True, show copyright greeting before every command."),
    )
    def show_greeting(self):
        return False

    # ***

    @property
    @ConfigRoot.setting(
        _("If True, use color and font ornamentation in output."),
    )
    def use_color(self):
        return True

    # ***

    @property
    @ConfigRoot.setting(
        _("If True, send application output to terminal pager."),
    )
    def use_pager(self):
        return False


# ***

def decorate_config(config):
    """Wraps or ensures the supplied config dict is a nark config decorator.

    Note: This is mostly for the ``nark/tests``, as the dob client will
    explicitly prepare a decorated config and pass that to nark. But to
    make it easier to write fixtures for ``nark/tests``, this method
    accepts a dictionary and returns a decorated config.
    """
    if isinstance(config, ConfigDecorator):
        return config
    # Caution: Remember that ConfigRoot is a weird Singleton.
    # FIXME/2020-01-07: (lb): Can probably put ConfigRoot et al in a getter
    #                         so that it doesn't have to be a module global.
    config_root = ConfigRoot
    config_root.forget_config_values()
    config_root.update(config)
    return config_root

