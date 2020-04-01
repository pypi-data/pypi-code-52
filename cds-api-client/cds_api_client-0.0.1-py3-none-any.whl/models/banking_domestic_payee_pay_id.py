# coding: utf-8

"""
A Python client package for accessing data from an API that uses the Consumer Data Standards.

Generated using the Swagger-Codegen CLI from a Swagger specification file of the Consumer Data Standards. 

NOT part of the official Consumer Data Standards' Project, nor any API implementation of the Standards. 
"""


import pprint
import re  # noqa: F401

import six


class BankingDomesticPayeePayId(object):
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
        'name': 'str',
        'identifier': 'str',
        'type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'identifier': 'identifier',
        'type': 'type'
    }

    def __init__(self, name=None, identifier=None, type=None):  # noqa: E501
        """BankingDomesticPayeePayId - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._identifier = None
        self._type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.identifier = identifier
        self.type = type

    @property
    def name(self):
        """Gets the name of this BankingDomesticPayeePayId.  # noqa: E501

        The name assigned to the PayID by the owner of the PayID  # noqa: E501

        :return: The name of this BankingDomesticPayeePayId.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BankingDomesticPayeePayId.

        The name assigned to the PayID by the owner of the PayID  # noqa: E501

        :param name: The name of this BankingDomesticPayeePayId.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def identifier(self):
        """Gets the identifier of this BankingDomesticPayeePayId.  # noqa: E501

        The identifier of the PayID (dependent on type)  # noqa: E501

        :return: The identifier of this BankingDomesticPayeePayId.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this BankingDomesticPayeePayId.

        The identifier of the PayID (dependent on type)  # noqa: E501

        :param identifier: The identifier of this BankingDomesticPayeePayId.  # noqa: E501
        :type: str
        """
        if identifier is None:
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def type(self):
        """Gets the type of this BankingDomesticPayeePayId.  # noqa: E501

        The type of the PayID  # noqa: E501

        :return: The type of this BankingDomesticPayeePayId.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BankingDomesticPayeePayId.

        The type of the PayID  # noqa: E501

        :param type: The type of this BankingDomesticPayeePayId.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["EMAIL", "TELEPHONE", "ABN", "ORG_IDENTIFIER"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(BankingDomesticPayeePayId, dict):
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
        if not isinstance(other, BankingDomesticPayeePayId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
