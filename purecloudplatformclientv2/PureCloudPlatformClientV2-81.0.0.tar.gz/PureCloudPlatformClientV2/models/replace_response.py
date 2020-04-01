# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re
import json

from ..utils import sanitize_for_serialization

class ReplaceResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ReplaceResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'change_number': 'int',
            'upload_status': 'DomainEntityRef',
            'upload_destination_uri': 'str',
            'upload_method': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'change_number': 'changeNumber',
            'upload_status': 'uploadStatus',
            'upload_destination_uri': 'uploadDestinationUri',
            'upload_method': 'uploadMethod'
        }

        self._id = None
        self._name = None
        self._change_number = None
        self._upload_status = None
        self._upload_destination_uri = None
        self._upload_method = None

    @property
    def id(self):
        """
        Gets the id of this ReplaceResponse.


        :return: The id of this ReplaceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ReplaceResponse.


        :param id: The id of this ReplaceResponse.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this ReplaceResponse.


        :return: The name of this ReplaceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ReplaceResponse.


        :param name: The name of this ReplaceResponse.
        :type: str
        """
        
        self._name = name

    @property
    def change_number(self):
        """
        Gets the change_number of this ReplaceResponse.


        :return: The change_number of this ReplaceResponse.
        :rtype: int
        """
        return self._change_number

    @change_number.setter
    def change_number(self, change_number):
        """
        Sets the change_number of this ReplaceResponse.


        :param change_number: The change_number of this ReplaceResponse.
        :type: int
        """
        
        self._change_number = change_number

    @property
    def upload_status(self):
        """
        Gets the upload_status of this ReplaceResponse.


        :return: The upload_status of this ReplaceResponse.
        :rtype: DomainEntityRef
        """
        return self._upload_status

    @upload_status.setter
    def upload_status(self, upload_status):
        """
        Sets the upload_status of this ReplaceResponse.


        :param upload_status: The upload_status of this ReplaceResponse.
        :type: DomainEntityRef
        """
        
        self._upload_status = upload_status

    @property
    def upload_destination_uri(self):
        """
        Gets the upload_destination_uri of this ReplaceResponse.


        :return: The upload_destination_uri of this ReplaceResponse.
        :rtype: str
        """
        return self._upload_destination_uri

    @upload_destination_uri.setter
    def upload_destination_uri(self, upload_destination_uri):
        """
        Sets the upload_destination_uri of this ReplaceResponse.


        :param upload_destination_uri: The upload_destination_uri of this ReplaceResponse.
        :type: str
        """
        
        self._upload_destination_uri = upload_destination_uri

    @property
    def upload_method(self):
        """
        Gets the upload_method of this ReplaceResponse.


        :return: The upload_method of this ReplaceResponse.
        :rtype: str
        """
        return self._upload_method

    @upload_method.setter
    def upload_method(self, upload_method):
        """
        Sets the upload_method of this ReplaceResponse.


        :param upload_method: The upload_method of this ReplaceResponse.
        :type: str
        """
        allowed_values = ["SINGLE_PUT", "MULTIPART_POST"]
        if upload_method.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for upload_method -> " + upload_method
            self._upload_method = "outdated_sdk_version"
        else:
            self._upload_method = upload_method

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_json(self):
        """
        Returns the model as raw JSON
        """
        return json.dumps(sanitize_for_serialization(self.to_dict()))

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

