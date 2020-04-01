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


class MePro(object):
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
        'level': 'str',
        'since': 'str',
        'until': 'str',
        'payment': 'MeProPayment',
        'trial': 'MeProTrial',
        'remaining_credit': 'float'
    }

    attribute_map = {
        'level': 'level',
        'since': 'since',
        'until': 'until',
        'payment': 'payment',
        'trial': 'trial',
        'remaining_credit': 'remaining_credit'
    }

    def __init__(self, level=None, since=None, until=None, payment=None, trial=None, remaining_credit=None):  # noqa: E501
        """MePro - a model defined in Swagger"""  # noqa: E501

        self._level = None
        self._since = None
        self._until = None
        self._payment = None
        self._trial = None
        self._remaining_credit = None
        self.discriminator = None

        if level is not None:
            self.level = level
        if since is not None:
            self.since = since
        if until is not None:
            self.until = until
        if payment is not None:
            self.payment = payment
        if trial is not None:
            self.trial = trial
        if remaining_credit is not None:
            self.remaining_credit = remaining_credit

    @property
    def level(self):
        """Gets the level of this MePro.  # noqa: E501


        :return: The level of this MePro.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this MePro.


        :param level: The level of this MePro.  # noqa: E501
        :type: str
        """

        self._level = level

    @property
    def since(self):
        """Gets the since of this MePro.  # noqa: E501


        :return: The since of this MePro.  # noqa: E501
        :rtype: str
        """
        return self._since

    @since.setter
    def since(self, since):
        """Sets the since of this MePro.


        :param since: The since of this MePro.  # noqa: E501
        :type: str
        """

        self._since = since

    @property
    def until(self):
        """Gets the until of this MePro.  # noqa: E501


        :return: The until of this MePro.  # noqa: E501
        :rtype: str
        """
        return self._until

    @until.setter
    def until(self, until):
        """Sets the until of this MePro.


        :param until: The until of this MePro.  # noqa: E501
        :type: str
        """

        self._until = until

    @property
    def payment(self):
        """Gets the payment of this MePro.  # noqa: E501


        :return: The payment of this MePro.  # noqa: E501
        :rtype: MeProPayment
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this MePro.


        :param payment: The payment of this MePro.  # noqa: E501
        :type: MeProPayment
        """

        self._payment = payment

    @property
    def trial(self):
        """Gets the trial of this MePro.  # noqa: E501


        :return: The trial of this MePro.  # noqa: E501
        :rtype: MeProTrial
        """
        return self._trial

    @trial.setter
    def trial(self, trial):
        """Sets the trial of this MePro.


        :param trial: The trial of this MePro.  # noqa: E501
        :type: MeProTrial
        """

        self._trial = trial

    @property
    def remaining_credit(self):
        """Gets the remaining_credit of this MePro.  # noqa: E501


        :return: The remaining_credit of this MePro.  # noqa: E501
        :rtype: float
        """
        return self._remaining_credit

    @remaining_credit.setter
    def remaining_credit(self, remaining_credit):
        """Sets the remaining_credit of this MePro.


        :param remaining_credit: The remaining_credit of this MePro.  # noqa: E501
        :type: float
        """

        self._remaining_credit = remaining_credit

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
        if issubclass(MePro, dict):
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
        if not isinstance(other, MePro):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
