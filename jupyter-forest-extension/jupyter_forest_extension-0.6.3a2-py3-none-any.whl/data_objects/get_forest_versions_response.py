##############################################################################
# Copyright 2019-2020 Rigetti Computing
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
##############################################################################

from dotmap import DotMap

from jupyter_forest_extension.data_objects.forest_docker_versions import ForestDockerVersions
from jupyter_forest_extension.data_objects.forest_versions import ForestVersions
from jupyter_forest_extension.data_objects.serializable import Serializable


class GetForestVersionsResponse(Serializable['GetForestVersionsResponse']):
    @classmethod
    def build_from_serialized(cls, serialized_obj: DotMap) -> 'GetForestVersionsResponse':
        forest_docker_versions = ForestDockerVersions.build_from_serialized(serialized_obj.forest_docker_versions)

        forest_versions = ForestVersions.build_from_serialized(serialized_obj.forest_versions)

        return GetForestVersionsResponse(forest_versions, forest_docker_versions)

    def __init__(self, forest_versions: ForestVersions, forest_docker_versions: ForestDockerVersions):
        self._forest_versions = forest_versions
        self._forest_docker_versions = forest_docker_versions

    @property
    def forest_versions(self) -> ForestVersions:
        return self._forest_versions

    @property
    def forest_docker_versions(self) -> ForestDockerVersions:
        return self._forest_docker_versions
