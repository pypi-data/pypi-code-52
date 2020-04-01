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


class TemplateNotificationRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, expirations=None, password=None, reminders=None, use_account_defaults=None):
        """
        TemplateNotificationRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'expirations': 'Expirations',
            'password': 'str',
            'reminders': 'Reminders',
            'use_account_defaults': 'str'
        }

        self.attribute_map = {
            'expirations': 'expirations',
            'password': 'password',
            'reminders': 'reminders',
            'use_account_defaults': 'useAccountDefaults'
        }

        self._expirations = expirations
        self._password = password
        self._reminders = reminders
        self._use_account_defaults = use_account_defaults

    @property
    def expirations(self):
        """
        Gets the expirations of this TemplateNotificationRequest.

        :return: The expirations of this TemplateNotificationRequest.
        :rtype: Expirations
        """
        return self._expirations

    @expirations.setter
    def expirations(self, expirations):
        """
        Sets the expirations of this TemplateNotificationRequest.

        :param expirations: The expirations of this TemplateNotificationRequest.
        :type: Expirations
        """

        self._expirations = expirations

    @property
    def password(self):
        """
        Gets the password of this TemplateNotificationRequest.
        

        :return: The password of this TemplateNotificationRequest.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this TemplateNotificationRequest.
        

        :param password: The password of this TemplateNotificationRequest.
        :type: str
        """

        self._password = password

    @property
    def reminders(self):
        """
        Gets the reminders of this TemplateNotificationRequest.

        :return: The reminders of this TemplateNotificationRequest.
        :rtype: Reminders
        """
        return self._reminders

    @reminders.setter
    def reminders(self, reminders):
        """
        Sets the reminders of this TemplateNotificationRequest.

        :param reminders: The reminders of this TemplateNotificationRequest.
        :type: Reminders
        """

        self._reminders = reminders

    @property
    def use_account_defaults(self):
        """
        Gets the use_account_defaults of this TemplateNotificationRequest.
        When set to **true**, the account default notification settings are used for the envelope.

        :return: The use_account_defaults of this TemplateNotificationRequest.
        :rtype: str
        """
        return self._use_account_defaults

    @use_account_defaults.setter
    def use_account_defaults(self, use_account_defaults):
        """
        Sets the use_account_defaults of this TemplateNotificationRequest.
        When set to **true**, the account default notification settings are used for the envelope.

        :param use_account_defaults: The use_account_defaults of this TemplateNotificationRequest.
        :type: str
        """

        self._use_account_defaults = use_account_defaults

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
