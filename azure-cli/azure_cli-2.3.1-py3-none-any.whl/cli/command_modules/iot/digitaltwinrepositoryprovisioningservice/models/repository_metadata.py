# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: skip-file
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RepositoryMetadata(Model):
    """RepositoryMetadata.

    :param id:
    :type id: str
    :param name:
    :type name: str
    :param type:
    :type type: str
    :param properties:
    :type properties:
     ~digitaltwinrepositoryprovisioningservice.models.RepositoryMetadataProperties
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'RepositoryMetadataProperties'},
    }

    def __init__(self, id=None, name=None, type=None, properties=None):
        super(RepositoryMetadata, self).__init__()
        self.id = id
        self.name = name
        self.type = type
        self.properties = properties
