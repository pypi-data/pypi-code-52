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

class GreetingMediaInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        GreetingMediaInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'media_file_uri': 'str',
            'media_image_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'media_file_uri': 'mediaFileUri',
            'media_image_uri': 'mediaImageUri'
        }

        self._id = None
        self._media_file_uri = None
        self._media_image_uri = None

    @property
    def id(self):
        """
        Gets the id of this GreetingMediaInfo.
        The globally unique identifier for the object.

        :return: The id of this GreetingMediaInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this GreetingMediaInfo.
        The globally unique identifier for the object.

        :param id: The id of this GreetingMediaInfo.
        :type: str
        """
        
        self._id = id

    @property
    def media_file_uri(self):
        """
        Gets the media_file_uri of this GreetingMediaInfo.


        :return: The media_file_uri of this GreetingMediaInfo.
        :rtype: str
        """
        return self._media_file_uri

    @media_file_uri.setter
    def media_file_uri(self, media_file_uri):
        """
        Sets the media_file_uri of this GreetingMediaInfo.


        :param media_file_uri: The media_file_uri of this GreetingMediaInfo.
        :type: str
        """
        
        self._media_file_uri = media_file_uri

    @property
    def media_image_uri(self):
        """
        Gets the media_image_uri of this GreetingMediaInfo.


        :return: The media_image_uri of this GreetingMediaInfo.
        :rtype: str
        """
        return self._media_image_uri

    @media_image_uri.setter
    def media_image_uri(self, media_image_uri):
        """
        Sets the media_image_uri of this GreetingMediaInfo.


        :param media_image_uri: The media_image_uri of this GreetingMediaInfo.
        :type: str
        """
        
        self._media_image_uri = media_image_uri

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

