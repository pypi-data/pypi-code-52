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


class ExternalClaim(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, acquired_time=None, claim_name=None, provider=None, value=None):
        """
        ExternalClaim - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'acquired_time': 'str',
            'claim_name': 'str',
            'provider': 'str',
            'value': 'str'
        }

        self.attribute_map = {
            'acquired_time': 'acquiredTime',
            'claim_name': 'claimName',
            'provider': 'provider',
            'value': 'value'
        }

        self._acquired_time = acquired_time
        self._claim_name = claim_name
        self._provider = provider
        self._value = value

    @property
    def acquired_time(self):
        """
        Gets the acquired_time of this ExternalClaim.
        

        :return: The acquired_time of this ExternalClaim.
        :rtype: str
        """
        return self._acquired_time

    @acquired_time.setter
    def acquired_time(self, acquired_time):
        """
        Sets the acquired_time of this ExternalClaim.
        

        :param acquired_time: The acquired_time of this ExternalClaim.
        :type: str
        """

        self._acquired_time = acquired_time

    @property
    def claim_name(self):
        """
        Gets the claim_name of this ExternalClaim.
        

        :return: The claim_name of this ExternalClaim.
        :rtype: str
        """
        return self._claim_name

    @claim_name.setter
    def claim_name(self, claim_name):
        """
        Sets the claim_name of this ExternalClaim.
        

        :param claim_name: The claim_name of this ExternalClaim.
        :type: str
        """

        self._claim_name = claim_name

    @property
    def provider(self):
        """
        Gets the provider of this ExternalClaim.
        

        :return: The provider of this ExternalClaim.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """
        Sets the provider of this ExternalClaim.
        

        :param provider: The provider of this ExternalClaim.
        :type: str
        """

        self._provider = provider

    @property
    def value(self):
        """
        Gets the value of this ExternalClaim.
        Specifies the value of the tab. 

        :return: The value of this ExternalClaim.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this ExternalClaim.
        Specifies the value of the tab. 

        :param value: The value of this ExternalClaim.
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
