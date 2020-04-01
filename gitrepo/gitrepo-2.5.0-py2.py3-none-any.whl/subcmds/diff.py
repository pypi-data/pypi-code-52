# -*- coding:utf-8 -*-
#
# Copyright (C) 2008 The Android Open Source Project
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

from repo.command import PagedCommand


class Diff(PagedCommand):
  common = True
  helpSummary = "Show changes between commit and working tree"
  helpUsage = """
%prog [<project>...]

The -u option causes '%prog' to generate diff output with file paths
relative to the repository root, so the output can be applied
to the Unix 'patch' command.
"""

  def _Options(self, p):
    p.add_option('-u', '--absolute',
                 dest='absolute', action='store_true',
                 help='Paths are relative to the repository root')

  def Execute(self, opt, args):
    ret = 0
    for project in self.GetProjects(args):
      if not project.PrintWorkTreeDiff(opt.absolute):
        ret = 1
    return ret
