# coding: utf-8

"""
A Python client package for accessing data from an API that uses the Consumer Data Standards.

Generated using the Swagger-Codegen CLI from a Swagger specification file of the Consumer Data Standards. 

NOT part of the official Consumer Data Standards' Project, nor any API implementation of the Standards. 
"""


import pprint
import re  # noqa: F401

import six


class BankingInternationalPayee(object):
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
        'beneficiary_details': 'BankingInternationalPayeeBeneficiaryDetails',
        'bank_details': 'BankingInternationalPayeeBankDetails'
    }

    attribute_map = {
        'beneficiary_details': 'beneficiaryDetails',
        'bank_details': 'bankDetails'
    }

    def __init__(self, beneficiary_details=None, bank_details=None):  # noqa: E501
        """BankingInternationalPayee - a model defined in Swagger"""  # noqa: E501

        self._beneficiary_details = None
        self._bank_details = None
        self.discriminator = None

        self.beneficiary_details = beneficiary_details
        self.bank_details = bank_details

    @property
    def beneficiary_details(self):
        """Gets the beneficiary_details of this BankingInternationalPayee.  # noqa: E501


        :return: The beneficiary_details of this BankingInternationalPayee.  # noqa: E501
        :rtype: BankingInternationalPayeeBeneficiaryDetails
        """
        return self._beneficiary_details

    @beneficiary_details.setter
    def beneficiary_details(self, beneficiary_details):
        """Sets the beneficiary_details of this BankingInternationalPayee.


        :param beneficiary_details: The beneficiary_details of this BankingInternationalPayee.  # noqa: E501
        :type: BankingInternationalPayeeBeneficiaryDetails
        """
        if beneficiary_details is None:
            raise ValueError("Invalid value for `beneficiary_details`, must not be `None`")  # noqa: E501

        self._beneficiary_details = beneficiary_details

    @property
    def bank_details(self):
        """Gets the bank_details of this BankingInternationalPayee.  # noqa: E501


        :return: The bank_details of this BankingInternationalPayee.  # noqa: E501
        :rtype: BankingInternationalPayeeBankDetails
        """
        return self._bank_details

    @bank_details.setter
    def bank_details(self, bank_details):
        """Sets the bank_details of this BankingInternationalPayee.


        :param bank_details: The bank_details of this BankingInternationalPayee.  # noqa: E501
        :type: BankingInternationalPayeeBankDetails
        """
        if bank_details is None:
            raise ValueError("Invalid value for `bank_details`, must not be `None`")  # noqa: E501

        self._bank_details = bank_details

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
        if issubclass(BankingInternationalPayee, dict):
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
        if not isinstance(other, BankingInternationalPayee):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
