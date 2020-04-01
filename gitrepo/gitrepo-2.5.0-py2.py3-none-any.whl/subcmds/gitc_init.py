# -*- coding:utf-8 -*-
#
# Copyright (C) 2015 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function
import os
import sys

from repo import gitc_utils
from repo.command import GitcAvailableCommand
from repo.manifest_xml import GitcManifest
from repo.subcmds import init
from repo import wrapper


class GitcInit(init.Init, GitcAvailableCommand):
  common = True
  helpSummary = "Initialize a GITC Client."
  helpUsage = """
%prog [options] [client name]
"""
  helpDescription = """
The '%prog' command is ran to initialize a new GITC client for use
with the GITC file system.

This command will setup the client directory, initialize repo, just
like repo init does, and then downloads the manifest collection
and installs it in the .repo/directory of the GITC client.

Once this is done, a GITC manifest is generated by pulling the HEAD
SHA for each project and generates the properly formatted XML file
and installs it as .manifest in the GITC client directory.

The -c argument is required to specify the GITC client name.

The optional -f argument can be used to specify the manifest file to
use for this GITC client.
"""

  def _Options(self, p):
    super(GitcInit, self)._Options(p, gitc_init=True)
    g = p.add_option_group('GITC options')
    g.add_option('-f', '--manifest-file',
                 dest='manifest_file',
                 help='Optional manifest file to use for this GITC client.')
    g.add_option('-c', '--gitc-client',
                 dest='gitc_client',
                 help='The name of the gitc_client instance to create or modify.')

  def Execute(self, opt, args):
    gitc_client = gitc_utils.parse_clientdir(os.getcwd())
    if not gitc_client or (opt.gitc_client and gitc_client != opt.gitc_client):
      print('fatal: Please update your repo command. See go/gitc for instructions.',
            file=sys.stderr)
      sys.exit(1)
    self.client_dir = os.path.join(gitc_utils.get_gitc_manifest_dir(),
                                   gitc_client)
    super(GitcInit, self).Execute(opt, args)

    manifest_file = self.manifest.manifestFile
    if opt.manifest_file:
      if not os.path.exists(opt.manifest_file):
        print('fatal: Specified manifest file %s does not exist.' %
              opt.manifest_file)
        sys.exit(1)
      manifest_file = opt.manifest_file

    manifest = GitcManifest(self.repodir, gitc_client)
    manifest.Override(manifest_file)
    gitc_utils.generate_gitc_manifest(None, manifest)
    print('Please run `cd %s` to view your GITC client.' %
          os.path.join(wrapper.Wrapper().GITC_FS_ROOT_DIR, gitc_client))
