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


class EmailSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, bcc_email_addresses=None, reply_email_address_override=None, reply_email_name_override=None):
        """
        EmailSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'bcc_email_addresses': 'list[BccEmailAddress]',
            'reply_email_address_override': 'str',
            'reply_email_name_override': 'str'
        }

        self.attribute_map = {
            'bcc_email_addresses': 'bccEmailAddresses',
            'reply_email_address_override': 'replyEmailAddressOverride',
            'reply_email_name_override': 'replyEmailNameOverride'
        }

        self._bcc_email_addresses = bcc_email_addresses
        self._reply_email_address_override = reply_email_address_override
        self._reply_email_name_override = reply_email_name_override

    @property
    def bcc_email_addresses(self):
        """
        Gets the bcc_email_addresses of this EmailSettings.
        A list of email addresses that receive a copy of all email communications for an envelope. You can use this for archiving purposes.

        :return: The bcc_email_addresses of this EmailSettings.
        :rtype: list[BccEmailAddress]
        """
        return self._bcc_email_addresses

    @bcc_email_addresses.setter
    def bcc_email_addresses(self, bcc_email_addresses):
        """
        Sets the bcc_email_addresses of this EmailSettings.
        A list of email addresses that receive a copy of all email communications for an envelope. You can use this for archiving purposes.

        :param bcc_email_addresses: The bcc_email_addresses of this EmailSettings.
        :type: list[BccEmailAddress]
        """

        self._bcc_email_addresses = bcc_email_addresses

    @property
    def reply_email_address_override(self):
        """
        Gets the reply_email_address_override of this EmailSettings.
        

        :return: The reply_email_address_override of this EmailSettings.
        :rtype: str
        """
        return self._reply_email_address_override

    @reply_email_address_override.setter
    def reply_email_address_override(self, reply_email_address_override):
        """
        Sets the reply_email_address_override of this EmailSettings.
        

        :param reply_email_address_override: The reply_email_address_override of this EmailSettings.
        :type: str
        """

        self._reply_email_address_override = reply_email_address_override

    @property
    def reply_email_name_override(self):
        """
        Gets the reply_email_name_override of this EmailSettings.
        

        :return: The reply_email_name_override of this EmailSettings.
        :rtype: str
        """
        return self._reply_email_name_override

    @reply_email_name_override.setter
    def reply_email_name_override(self, reply_email_name_override):
        """
        Sets the reply_email_name_override of this EmailSettings.
        

        :param reply_email_name_override: The reply_email_name_override of this EmailSettings.
        :type: str
        """

        self._reply_email_name_override = reply_email_name_override

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
