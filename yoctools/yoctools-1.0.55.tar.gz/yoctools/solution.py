# -*- coding:utf-8 -*-
#
# Copyright (C) 2019-2020 Alibaba Group Holding Limited


from __future__ import print_function
import os
import re

from .log import logger
from .tools import *
from .package import *
from .component import *


class Variables:
    def __init__(self):
        self.vars = {}
        pass

    def set(self, k, v, lower=False):
        self.vars[k] = v
        if lower:
            self.vars[k.lower()] = v.lower()

    def get(self, var):
        if var in self.vars:
            return self.vars[var]

    def convert(self, var):
        v = var.split('?')
        if len(v) > 1:
            x = re.search('<(.+?)>', v[1], re.M | re.I)
            if x:
                x = self.get(x.group(1))
                if str(x) not in ['y', 'yes', 't', 'true', '1']:
                    return None
                var = v[0].strip()

        x = re.findall('<(.+?)>', var)
        for key in x:
            value = self.get(key)
            if value != None:
                var = var.replace('<'+key+'>', self.vars[key])
            else:
                put_string('not found variable:', var)

        return var

    def items(self):
        return self.vars.items()


class Solution:
    def __init__(self, components):
        self.variables = Variables()
        self.solution_component = None       # 当前 solution 组件
        self.board_component = None          # 当前开发板组件
        self.chip_component = None           # 当前芯片组件
        self.components = components         # 使用到的组件
        self.global_includes = []
        self.libs = []
        self.libpath = []
        self.depend_libs = []
        self.defines = {}
        self.ASFLAGS = []
        self.CCFLAGS = []
        self.CXXFLAGS = []
        self.LINKFLAGS = []
        self.ld_script = ''
        self.ld_script_component = None
        self.cpu_name = ''
        self.toolchain_prefix = ''

        # find current solution & board component
        for component in self.components:
            if component.path == os.getcwd() and component.type == 'solution':
                self.solution_component = component
                if self.solution_component.hw_info.board_name:
                    self.board_component = self.components.get(
                        self.solution_component.hw_info.board_name)
                    if not self.board_component:
                        put_string("Not found in `%s` components that the current project depends on. " %
                                   self.solution_component.hw_info.board_name)
                        exit(-1)

                    self.chip_component = self.components.get(
                        self.board_component.hw_info.chip_name)
                    if not self.chip_component:
                        put_string("Not found in `%s` components that the current project depends on. " %
                                   self.board_component.hw_info.chip_name)
                        exit(-1)
                break

        if not self.solution_component:
            put_string('The current directory is not a solution directory.')
            exit(-1)

        if (not self.board_component) and (not self.solution_component.hw_info.cpu_name) and (not self.solution_component.hw_info.ld_script):
            for name in self.solution_component.depends:
                component = self.components.get(name)
                if component:
                    if component.type == 'board':
                        self.board_component = component
                        self.solution_component.hw_info.board_name = self.board_component.name
                        self.chip_component = self.components.get(
                            self.board_component.hw_info.chip_name)
                        if self.chip_component:
                            self.solution_component.hw_info.chip_name = self.chip_component.name
                        else:
                            put_string("Not found chip component: " +
                                       self.board_component.hw_info.chip_name)
                            exit(-1)
                        break
                else:
                    put_string("`%s` not found, please install it: yoc install %s" %
                               (name, name))
                    exit(-1)
            if not self.board_component:
                logger.warning(
                    'Not found board component in depends')

        if self.board_component:
            self.board_component.need_build = True
        if self.chip_component:
            self.chip_component.need_build = True

        components = ComponentGroup()
        for component in self.components:
            if component.need_build:
                components.add(component)
        self.components = components

        def cpu_set_variable(cpu, arch):
            self.cpu_name = cpu
            self.variables.set('CPU', cpu.upper(), True)
            if cpu.lower() == 'rv32emc':
                self.variables.set('cpu_num', 'rv32')
                self.variables.set('arch', 'RISCV', True)
            # elif cpu.lower() == 'ck803ef':
            #     self.variables.set('cpu_num', '803ef')
            #     self.variables.set('ARCH', 'CSKY', True)
            else:
                if arch == '' or arch.upper() == 'CSKY':
                    self.variables.set('cpu_num', cpu_id(cpu))
                    self.variables.set('ARCH', 'CSKY', True)
                elif arch == 'arm':
                    self.variables.set('cpu_num', arm_cpu_id(cpu))
                    self.variables.set('ARCH', arch, True)
                else:
                    logger.error("not support arch:%s yet" % arch)

        for component in self.components:
            # defines
            for k, v in component.defconfig.items():
                self.variables.set(k, v)
                self.defines[k] = v

        solution_hw_info = HardwareInfo({})
        for component in [self.chip_component, self.board_component, self.solution_component]:
            if component:
                solution_hw_info.merge(component.hw_info)

                for c in component.build_config.cflag.split():
                    self.CCFLAGS.append(c)
                for c in component.build_config.asmflag.split():
                    self.ASFLAGS.append(c)
                for c in component.build_config.cxxflag.split():
                    self.CXXFLAGS.append(c)
                for c in component.build_config.ldflag.split():
                    self.LINKFLAGS.append(c)

        # 根据 cpu_id 加载配置
        if solution_hw_info.cpu_id in solution_hw_info.cpu_list:
            for k, v in solution_hw_info.cpu_list[solution_hw_info.cpu_id].items():
                solution_hw_info.__dict__[k] = v

        # soution 的hw_info 优先
        solution_hw_info.merge(self.solution_component.hw_info, True)

        if solution_hw_info.cpu_name == '':
            logger.error("not found cpu_id, please set cpu_id")
            exit(-1)

        if solution_hw_info.cpu_name:
            cpu_set_variable(solution_hw_info.cpu_name,
                             solution_hw_info.arch_name)

        if solution_hw_info.cpu_id:
            self.variables.set(solution_hw_info.cpu_id.upper(), 1)

        if solution_hw_info.vendor_name:
            self.variables.set(
                'VENDOR', solution_hw_info.vendor_name.upper(), True)

        if solution_hw_info.chip_name:
            self.variables.set(
                'CHIP', solution_hw_info.chip_name.upper(), True)

        if solution_hw_info.board_name:
            self.variables.set(
                'BOARD', solution_hw_info.board_name.upper(), True)

        if self.chip_component:
            self.variables.set('CHIP_PATH', self.chip_component.path)

        if self.board_component:
            self.variables.set('BOARD_PATH', self.board_component.path)

        self.variables.set('SOLUTION_PATH', self.solution_component.path)
        self.yoc_path = os.path.join(self.solution_component.path, 'yoc_sdk')
        self.lib_path = os.path.join(self.yoc_path, 'lib')
        self.libpath.append(self.lib_path)

        self.global_includes.append(os.path.join(
            self.solution_component.path, 'include'))

        for component in self.components:
            if len(component.source_files) > 0 and component.type != 'solution' and component.name not in self.libs:
                self.libs.append(component.name)
                self.depend_libs.append(os.path.join(
                    self.lib_path, 'lib' + component.name + '.a'))

            component.variable_convert(self.variables)

            # include
            for path in component.build_config.include:
                if path not in self.global_includes:
                    self.global_includes.append(path)

            # libpath
            for path in component.build_config.libpath:
                if path not in self.libpath:
                    self.libpath.append(path)

            # libs
            for lib in component.build_config.libs:
                if lib not in self.libs:
                    self.libs.append(lib)

        if self.solution_component.hw_info.ld_script:
            self.ld_script = self.solution_component.hw_info.ld_script
            self.ld_script_component = self.solution_component
        elif self.board_component and self.board_component.hw_info.ld_script:
            self.ld_script = self.board_component.hw_info.ld_script
            self.ld_script_component = self.board_component
        elif self.chip_component and self.chip_component.hw_info.ld_script:
            self.ld_script = self.chip_component.hw_info.ld_script
            self.ld_script_component = self.chip_component
        else:
            logger.error("not found LD script file, please set ld_script")
            exit(-1)

        self.toolchain_prefix = solution_hw_info.toolchain_prefix
        self.ld_script = self.variables.convert(self.ld_script)

    def install(self):
        for component in self.components:
            component.install(self.yoc_path)

    def show(self, show_component=True, show_libs=True, show_include=True, show_define=True, show_veriable=True, show_flags=True):
        if show_component:
            put_string("[component]")
            for c in self.components:
                c.show(4)

            put_string()
            if self.solution_component:
                put_string("    solution component: " +
                           self.solution_component.name)
            if self.board_component:
                put_string("    board component   : " +
                           self.board_component.name)
            if self.chip_component:
                put_string("    chip component    : " +
                           self.chip_component.name)

        if show_libs:
            put_string("[libs]")
            for v in self.libs:
                put_string('    ' + v)

            put_string("[libpath]")
            for v in self.libpath:
                put_string('    ' + v)

        if show_include:
            put_string("[global_includes]")
            for v in self.global_includes:
                put_string('    ' + v)

        if show_define:
            put_string("[defines]")
            for k, v in self.defines.items():
                put_string('    ', k, '=', v)

        if show_veriable:
            put_string("[variables]")
            for k, v in self.variables.items():
                put_string('    %s = %s' % (k, v))

        if show_flags:
            put_string("ASFLAGS   :" + ' '.join(self.ASFLAGS))
            put_string("CCFLAGS   :" + ' '.join(self.CCFLAGS))
            put_string("CXXFLAGS  :" + ' '.join(self.CXXFLAGS))
            put_string("LINKFLAGS :" + ' '.join(self.LINKFLAGS))
            put_string('ld_script : ' + self.ld_script)
            put_string('toolchain : ' + self.toolchain_prefix)


def cpu_id(s):
    s += 'z'
    ids = ''
    for c in s:
        if ord(c) >= ord('0') and ord(c) <= ord('9'):
            ids += c
        elif ids:
            return ids


def arm_cpu_id(s):
    if s.startswith('arm'):
        return s[3:]
    else:
        arr = s.split('-')
        if len(arr) > 1:
            return arr[1]
