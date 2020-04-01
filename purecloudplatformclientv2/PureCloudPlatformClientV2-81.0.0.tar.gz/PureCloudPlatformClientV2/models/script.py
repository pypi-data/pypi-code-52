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

class Script(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Script - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'version_id': 'str',
            'created_date': 'datetime',
            'modified_date': 'datetime',
            'published_date': 'datetime',
            'version_date': 'datetime',
            'start_page_id': 'str',
            'start_page_name': 'str',
            'features': 'object',
            'variables': 'object',
            'custom_actions': 'object',
            'pages': 'list[Page]',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'version_id': 'versionId',
            'created_date': 'createdDate',
            'modified_date': 'modifiedDate',
            'published_date': 'publishedDate',
            'version_date': 'versionDate',
            'start_page_id': 'startPageId',
            'start_page_name': 'startPageName',
            'features': 'features',
            'variables': 'variables',
            'custom_actions': 'customActions',
            'pages': 'pages',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._version_id = None
        self._created_date = None
        self._modified_date = None
        self._published_date = None
        self._version_date = None
        self._start_page_id = None
        self._start_page_name = None
        self._features = None
        self._variables = None
        self._custom_actions = None
        self._pages = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this Script.
        The globally unique identifier for the object.

        :return: The id of this Script.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Script.
        The globally unique identifier for the object.

        :param id: The id of this Script.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Script.


        :return: The name of this Script.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Script.


        :param name: The name of this Script.
        :type: str
        """
        
        self._name = name

    @property
    def version_id(self):
        """
        Gets the version_id of this Script.


        :return: The version_id of this Script.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """
        Sets the version_id of this Script.


        :param version_id: The version_id of this Script.
        :type: str
        """
        
        self._version_id = version_id

    @property
    def created_date(self):
        """
        Gets the created_date of this Script.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The created_date of this Script.
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """
        Sets the created_date of this Script.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param created_date: The created_date of this Script.
        :type: datetime
        """
        
        self._created_date = created_date

    @property
    def modified_date(self):
        """
        Gets the modified_date of this Script.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The modified_date of this Script.
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """
        Sets the modified_date of this Script.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param modified_date: The modified_date of this Script.
        :type: datetime
        """
        
        self._modified_date = modified_date

    @property
    def published_date(self):
        """
        Gets the published_date of this Script.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The published_date of this Script.
        :rtype: datetime
        """
        return self._published_date

    @published_date.setter
    def published_date(self, published_date):
        """
        Sets the published_date of this Script.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param published_date: The published_date of this Script.
        :type: datetime
        """
        
        self._published_date = published_date

    @property
    def version_date(self):
        """
        Gets the version_date of this Script.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :return: The version_date of this Script.
        :rtype: datetime
        """
        return self._version_date

    @version_date.setter
    def version_date(self, version_date):
        """
        Sets the version_date of this Script.
        Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss.SSSZ

        :param version_date: The version_date of this Script.
        :type: datetime
        """
        
        self._version_date = version_date

    @property
    def start_page_id(self):
        """
        Gets the start_page_id of this Script.


        :return: The start_page_id of this Script.
        :rtype: str
        """
        return self._start_page_id

    @start_page_id.setter
    def start_page_id(self, start_page_id):
        """
        Sets the start_page_id of this Script.


        :param start_page_id: The start_page_id of this Script.
        :type: str
        """
        
        self._start_page_id = start_page_id

    @property
    def start_page_name(self):
        """
        Gets the start_page_name of this Script.


        :return: The start_page_name of this Script.
        :rtype: str
        """
        return self._start_page_name

    @start_page_name.setter
    def start_page_name(self, start_page_name):
        """
        Sets the start_page_name of this Script.


        :param start_page_name: The start_page_name of this Script.
        :type: str
        """
        
        self._start_page_name = start_page_name

    @property
    def features(self):
        """
        Gets the features of this Script.


        :return: The features of this Script.
        :rtype: object
        """
        return self._features

    @features.setter
    def features(self, features):
        """
        Sets the features of this Script.


        :param features: The features of this Script.
        :type: object
        """
        
        self._features = features

    @property
    def variables(self):
        """
        Gets the variables of this Script.


        :return: The variables of this Script.
        :rtype: object
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """
        Sets the variables of this Script.


        :param variables: The variables of this Script.
        :type: object
        """
        
        self._variables = variables

    @property
    def custom_actions(self):
        """
        Gets the custom_actions of this Script.


        :return: The custom_actions of this Script.
        :rtype: object
        """
        return self._custom_actions

    @custom_actions.setter
    def custom_actions(self, custom_actions):
        """
        Sets the custom_actions of this Script.


        :param custom_actions: The custom_actions of this Script.
        :type: object
        """
        
        self._custom_actions = custom_actions

    @property
    def pages(self):
        """
        Gets the pages of this Script.


        :return: The pages of this Script.
        :rtype: list[Page]
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """
        Sets the pages of this Script.


        :param pages: The pages of this Script.
        :type: list[Page]
        """
        
        self._pages = pages

    @property
    def self_uri(self):
        """
        Gets the self_uri of this Script.
        The URI for this object

        :return: The self_uri of this Script.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this Script.
        The URI for this object

        :param self_uri: The self_uri of this Script.
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

