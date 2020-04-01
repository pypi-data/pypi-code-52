# coding: utf-8

"""
    Toshl

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MeProPayment(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'provider': 'str',
        'next': 'str',
        'trial': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'provider': 'provider',
        'next': 'next',
        'trial': 'trial'
    }

    def __init__(self, id=None, provider=None, next=None, trial=None):  # noqa: E501
        """MeProPayment - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._provider = None
        self._next = None
        self._trial = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if provider is not None:
            self.provider = provider
        if next is not None:
            self.next = next
        if trial is not None:
            self.trial = trial

    @property
    def id(self):
        """Gets the id of this MeProPayment.  # noqa: E501


        :return: The id of this MeProPayment.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MeProPayment.


        :param id: The id of this MeProPayment.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def provider(self):
        """Gets the provider of this MeProPayment.  # noqa: E501


        :return: The provider of this MeProPayment.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this MeProPayment.


        :param provider: The provider of this MeProPayment.  # noqa: E501
        :type: str
        """

        self._provider = provider

    @property
    def next(self):
        """Gets the next of this MeProPayment.  # noqa: E501


        :return: The next of this MeProPayment.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this MeProPayment.


        :param next: The next of this MeProPayment.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def trial(self):
        """Gets the trial of this MeProPayment.  # noqa: E501


        :return: The trial of this MeProPayment.  # noqa: E501
        :rtype: bool
        """
        return self._trial

    @trial.setter
    def trial(self, trial):
        """Sets the trial of this MeProPayment.


        :param trial: The trial of this MeProPayment.  # noqa: E501
        :type: bool
        """

        self._trial = trial

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(MeProPayment, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MeProPayment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
