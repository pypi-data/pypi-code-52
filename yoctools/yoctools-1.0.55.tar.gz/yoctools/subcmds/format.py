# -*- coding:utf-8 -*-
#
# Copyright (C) 2019-2020 Alibaba Group Holding Limited


from __future__ import print_function

from yoctools import *


class Format(Command):
    common = True
    helpSummary = "Format component package.yaml file"
    helpUsage = """
%prog [<component>...]
"""
    helpDescription = """
Format component package.yaml file
"""

    def Execute(self, opt, args):
        yoc = YoC()

        count = len(args)
        for component in yoc.components:
            if count == 0 or component.name in args:
                put_string("formating package: %s" % component.name)
                component.load_package()
                component.pack.save()
