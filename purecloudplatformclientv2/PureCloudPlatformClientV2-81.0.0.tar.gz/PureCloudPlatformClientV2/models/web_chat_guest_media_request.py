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

class WebChatGuestMediaRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        WebChatGuestMediaRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'types': 'list[str]',
            'state': 'str',
            'communication_id': 'str',
            'security_key': 'str',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'types': 'types',
            'state': 'state',
            'communication_id': 'communicationId',
            'security_key': 'securityKey',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._types = None
        self._state = None
        self._communication_id = None
        self._security_key = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this WebChatGuestMediaRequest.
        The globally unique identifier for the object.

        :return: The id of this WebChatGuestMediaRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WebChatGuestMediaRequest.
        The globally unique identifier for the object.

        :param id: The id of this WebChatGuestMediaRequest.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this WebChatGuestMediaRequest.


        :return: The name of this WebChatGuestMediaRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this WebChatGuestMediaRequest.


        :param name: The name of this WebChatGuestMediaRequest.
        :type: str
        """
        
        self._name = name

    @property
    def types(self):
        """
        Gets the types of this WebChatGuestMediaRequest.
        The types of media being requested.

        :return: The types of this WebChatGuestMediaRequest.
        :rtype: list[str]
        """
        return self._types

    @types.setter
    def types(self, types):
        """
        Sets the types of this WebChatGuestMediaRequest.
        The types of media being requested.

        :param types: The types of this WebChatGuestMediaRequest.
        :type: list[str]
        """
        
        self._types = types

    @property
    def state(self):
        """
        Gets the state of this WebChatGuestMediaRequest.
        The state of the media request, one of PENDING|ACCEPTED|DECLINED|TIMEDOUT|CANCELLED|ERRORED.

        :return: The state of this WebChatGuestMediaRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this WebChatGuestMediaRequest.
        The state of the media request, one of PENDING|ACCEPTED|DECLINED|TIMEDOUT|CANCELLED|ERRORED.

        :param state: The state of this WebChatGuestMediaRequest.
        :type: str
        """
        allowed_values = ["PENDING", "ACCEPTED", "DECLINED", "TIMEDOUT", "CANCELLED", "ERRORED"]
        if state.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for state -> " + state
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def communication_id(self):
        """
        Gets the communication_id of this WebChatGuestMediaRequest.
        The ID of the new media communication, if applicable.

        :return: The communication_id of this WebChatGuestMediaRequest.
        :rtype: str
        """
        return self._communication_id

    @communication_id.setter
    def communication_id(self, communication_id):
        """
        Sets the communication_id of this WebChatGuestMediaRequest.
        The ID of the new media communication, if applicable.

        :param communication_id: The communication_id of this WebChatGuestMediaRequest.
        :type: str
        """
        
        self._communication_id = communication_id

    @property
    def security_key(self):
        """
        Gets the security_key of this WebChatGuestMediaRequest.
        The security information related to a media request.

        :return: The security_key of this WebChatGuestMediaRequest.
        :rtype: str
        """
        return self._security_key

    @security_key.setter
    def security_key(self, security_key):
        """
        Sets the security_key of this WebChatGuestMediaRequest.
        The security information related to a media request.

        :param security_key: The security_key of this WebChatGuestMediaRequest.
        :type: str
        """
        
        self._security_key = security_key

    @property
    def self_uri(self):
        """
        Gets the self_uri of this WebChatGuestMediaRequest.
        The URI for this object

        :return: The self_uri of this WebChatGuestMediaRequest.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this WebChatGuestMediaRequest.
        The URI for this object

        :param self_uri: The self_uri of this WebChatGuestMediaRequest.
        :type: str
        """
        
        self._self_uri = self_uri

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

