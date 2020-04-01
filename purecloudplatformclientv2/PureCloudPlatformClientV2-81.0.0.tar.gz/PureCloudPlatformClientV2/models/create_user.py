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

class CreateUser(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CreateUser - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'department': 'str',
            'email': 'str',
            'addresses': 'list[Contact]',
            'title': 'str',
            'password': 'str',
            'division_id': 'str',
            'state': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'department': 'department',
            'email': 'email',
            'addresses': 'addresses',
            'title': 'title',
            'password': 'password',
            'division_id': 'divisionId',
            'state': 'state'
        }

        self._name = None
        self._department = None
        self._email = None
        self._addresses = None
        self._title = None
        self._password = None
        self._division_id = None
        self._state = None

    @property
    def name(self):
        """
        Gets the name of this CreateUser.
        User's full name

        :return: The name of this CreateUser.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateUser.
        User's full name

        :param name: The name of this CreateUser.
        :type: str
        """
        
        self._name = name

    @property
    def department(self):
        """
        Gets the department of this CreateUser.


        :return: The department of this CreateUser.
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department):
        """
        Sets the department of this CreateUser.


        :param department: The department of this CreateUser.
        :type: str
        """
        
        self._department = department

    @property
    def email(self):
        """
        Gets the email of this CreateUser.
        User's email and username

        :return: The email of this CreateUser.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this CreateUser.
        User's email and username

        :param email: The email of this CreateUser.
        :type: str
        """
        
        self._email = email

    @property
    def addresses(self):
        """
        Gets the addresses of this CreateUser.
        Email addresses and phone numbers for this user

        :return: The addresses of this CreateUser.
        :rtype: list[Contact]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """
        Sets the addresses of this CreateUser.
        Email addresses and phone numbers for this user

        :param addresses: The addresses of this CreateUser.
        :type: list[Contact]
        """
        
        self._addresses = addresses

    @property
    def title(self):
        """
        Gets the title of this CreateUser.


        :return: The title of this CreateUser.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this CreateUser.


        :param title: The title of this CreateUser.
        :type: str
        """
        
        self._title = title

    @property
    def password(self):
        """
        Gets the password of this CreateUser.
        User's password

        :return: The password of this CreateUser.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this CreateUser.
        User's password

        :param password: The password of this CreateUser.
        :type: str
        """
        
        self._password = password

    @property
    def division_id(self):
        """
        Gets the division_id of this CreateUser.
        The division to which this user will belong

        :return: The division_id of this CreateUser.
        :rtype: str
        """
        return self._division_id

    @division_id.setter
    def division_id(self, division_id):
        """
        Sets the division_id of this CreateUser.
        The division to which this user will belong

        :param division_id: The division_id of this CreateUser.
        :type: str
        """
        
        self._division_id = division_id

    @property
    def state(self):
        """
        Gets the state of this CreateUser.
        Optional initialized state of the user. If not specified, state will be Active if invites are sent, otherwise Inactive.

        :return: The state of this CreateUser.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this CreateUser.
        Optional initialized state of the user. If not specified, state will be Active if invites are sent, otherwise Inactive.

        :param state: The state of this CreateUser.
        :type: str
        """
        allowed_values = ["active", "inactive", "deleted"]
        if state.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for state -> " + state
            self._state = "outdated_sdk_version"
        else:
            self._state = state

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

