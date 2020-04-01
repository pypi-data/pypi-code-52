# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class NameValue(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, error_details=None, name=None, original_value=None, value=None):
        """
        NameValue - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'error_details': 'ErrorDetails',
            'name': 'str',
            'original_value': 'str',
            'value': 'str'
        }

        self.attribute_map = {
            'error_details': 'errorDetails',
            'name': 'name',
            'original_value': 'originalValue',
            'value': 'value'
        }

        self._error_details = error_details
        self._name = name
        self._original_value = original_value
        self._value = value

    @property
    def error_details(self):
        """
        Gets the error_details of this NameValue.

        :return: The error_details of this NameValue.
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """
        Sets the error_details of this NameValue.

        :param error_details: The error_details of this NameValue.
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def name(self):
        """
        Gets the name of this NameValue.
        The name or key of a name/value pair.

        :return: The name of this NameValue.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this NameValue.
        The name or key of a name/value pair.

        :param name: The name of this NameValue.
        :type: str
        """

        self._name = name

    @property
    def original_value(self):
        """
        Gets the original_value of this NameValue.
        The initial value of the tab when it was sent to the recipient. 

        :return: The original_value of this NameValue.
        :rtype: str
        """
        return self._original_value

    @original_value.setter
    def original_value(self, original_value):
        """
        Sets the original_value of this NameValue.
        The initial value of the tab when it was sent to the recipient. 

        :param original_value: The original_value of this NameValue.
        :type: str
        """

        self._original_value = original_value

    @property
    def value(self):
        """
        Gets the value of this NameValue.
        The value field of a name/value pair.

        :return: The value of this NameValue.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this NameValue.
        The value field of a name/value pair.

        :param value: The value of this NameValue.
        :type: str
        """

        self._value = value

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
