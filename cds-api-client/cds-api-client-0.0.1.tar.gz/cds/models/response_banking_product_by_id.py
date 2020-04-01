# coding: utf-8

"""
A Python client package for accessing data from an API that uses the Consumer Data Standards.

Generated using the Swagger-Codegen CLI from a Swagger specification file of the Consumer Data Standards. 

NOT part of the official Consumer Data Standards' Project, nor any API implementation of the Standards. 
"""


import pprint
import re  # noqa: F401

import six


class ResponseBankingProductById(object):
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
        'data': 'BankingProductDetail',
        'links': 'Links',
        'meta': 'Meta'
    }

    attribute_map = {
        'data': 'data',
        'links': 'links',
        'meta': 'meta'
    }

    def __init__(self, data=None, links=None, meta=None):  # noqa: E501
        """ResponseBankingProductById - a model defined in Swagger"""  # noqa: E501

        self._data = None
        self._links = None
        self._meta = None
        self.discriminator = None

        self.data = data
        self.links = links
        if meta is not None:
            self.meta = meta

    @property
    def data(self):
        """Gets the data of this ResponseBankingProductById.  # noqa: E501


        :return: The data of this ResponseBankingProductById.  # noqa: E501
        :rtype: BankingProductDetail
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ResponseBankingProductById.


        :param data: The data of this ResponseBankingProductById.  # noqa: E501
        :type: BankingProductDetail
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def links(self):
        """Gets the links of this ResponseBankingProductById.  # noqa: E501


        :return: The links of this ResponseBankingProductById.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ResponseBankingProductById.


        :param links: The links of this ResponseBankingProductById.  # noqa: E501
        :type: Links
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def meta(self):
        """Gets the meta of this ResponseBankingProductById.  # noqa: E501


        :return: The meta of this ResponseBankingProductById.  # noqa: E501
        :rtype: Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this ResponseBankingProductById.


        :param meta: The meta of this ResponseBankingProductById.  # noqa: E501
        :type: Meta
        """

        self._meta = meta

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
        if issubclass(ResponseBankingProductById, dict):
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
        if not isinstance(other, ResponseBankingProductById):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
