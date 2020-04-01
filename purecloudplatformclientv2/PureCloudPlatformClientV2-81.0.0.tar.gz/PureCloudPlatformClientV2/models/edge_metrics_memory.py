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

class EdgeMetricsMemory(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        EdgeMetricsMemory - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'available_bytes': 'float',
            'type': 'str',
            'total_bytes': 'float'
        }

        self.attribute_map = {
            'available_bytes': 'availableBytes',
            'type': 'type',
            'total_bytes': 'totalBytes'
        }

        self._available_bytes = None
        self._type = None
        self._total_bytes = None

    @property
    def available_bytes(self):
        """
        Gets the available_bytes of this EdgeMetricsMemory.
        Available memory in bytes.

        :return: The available_bytes of this EdgeMetricsMemory.
        :rtype: float
        """
        return self._available_bytes

    @available_bytes.setter
    def available_bytes(self, available_bytes):
        """
        Sets the available_bytes of this EdgeMetricsMemory.
        Available memory in bytes.

        :param available_bytes: The available_bytes of this EdgeMetricsMemory.
        :type: float
        """
        
        self._available_bytes = available_bytes

    @property
    def type(self):
        """
        Gets the type of this EdgeMetricsMemory.
        Type of memory. Virtual or physical.

        :return: The type of this EdgeMetricsMemory.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this EdgeMetricsMemory.
        Type of memory. Virtual or physical.

        :param type: The type of this EdgeMetricsMemory.
        :type: str
        """
        
        self._type = type

    @property
    def total_bytes(self):
        """
        Gets the total_bytes of this EdgeMetricsMemory.
        Total memory in bytes.

        :return: The total_bytes of this EdgeMetricsMemory.
        :rtype: float
        """
        return self._total_bytes

    @total_bytes.setter
    def total_bytes(self, total_bytes):
        """
        Sets the total_bytes of this EdgeMetricsMemory.
        Total memory in bytes.

        :param total_bytes: The total_bytes of this EdgeMetricsMemory.
        :type: float
        """
        
        self._total_bytes = total_bytes

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

