#
# Copyright (c) 2019, Neptune Labs Sp. z o.o.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

try:
    import psutil
    PSUTIL_INSTALLED = True
except ImportError:
    PSUTIL_INSTALLED = False


class SystemMonitor(object):
    @staticmethod
    def requirements_installed():
        return PSUTIL_INSTALLED

    @staticmethod
    def cpu_count():
        return psutil.cpu_count()

    @staticmethod
    def cpu_percent():
        return psutil.cpu_percent()

    @staticmethod
    def virtual_memory():
        return psutil.virtual_memory()
