# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class MobileNotifierConfiguration(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, device_id=None, error_details=None, platform=None):
        """
        MobileNotifierConfiguration - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'device_id': 'str',
            'error_details': 'ErrorDetails',
            'platform': 'str'
        }

        self.attribute_map = {
            'device_id': 'deviceId',
            'error_details': 'errorDetails',
            'platform': 'platform'
        }

        self._device_id = device_id
        self._error_details = error_details
        self._platform = platform

    @property
    def device_id(self):
        """
        Gets the device_id of this MobileNotifierConfiguration.
        

        :return: The device_id of this MobileNotifierConfiguration.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """
        Sets the device_id of this MobileNotifierConfiguration.
        

        :param device_id: The device_id of this MobileNotifierConfiguration.
        :type: str
        """

        self._device_id = device_id

    @property
    def error_details(self):
        """
        Gets the error_details of this MobileNotifierConfiguration.

        :return: The error_details of this MobileNotifierConfiguration.
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """
        Sets the error_details of this MobileNotifierConfiguration.

        :param error_details: The error_details of this MobileNotifierConfiguration.
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def platform(self):
        """
        Gets the platform of this MobileNotifierConfiguration.
        

        :return: The platform of this MobileNotifierConfiguration.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """
        Sets the platform of this MobileNotifierConfiguration.
        

        :param platform: The platform of this MobileNotifierConfiguration.
        :type: str
        """

        self._platform = platform

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
