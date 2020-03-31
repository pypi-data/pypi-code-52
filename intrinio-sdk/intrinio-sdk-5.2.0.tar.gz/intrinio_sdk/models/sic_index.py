# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SICIndex(object):
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
        'symbol': 'str',
        'name': 'str',
        'continent': 'str',
        'country': 'str'
    }

    attribute_map = {
        'id': 'id',
        'symbol': 'symbol',
        'name': 'name',
        'continent': 'continent',
        'country': 'country'
    }

    def __init__(self, id=None, symbol=None, name=None, continent=None, country=None):  # noqa: E501
        """SICIndex - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._symbol = None
        self._name = None
        self._continent = None
        self._country = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if symbol is not None:
            self.symbol = symbol
        if name is not None:
            self.name = name
        if continent is not None:
            self.continent = continent
        if country is not None:
            self.country = country

    @property
    def id(self):
        """Gets the id of this SICIndex.  # noqa: E501

        Intrinio ID for the Index  # noqa: E501

        :return: The id of this SICIndex.  # noqa: E501
        :rtype: str
        """
        return self._id
        
    @property
    def id_dict(self):
        """Gets the id of this SICIndex.  # noqa: E501

        Intrinio ID for the Index as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The id of this SICIndex.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.id
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'id': value }

        
        return result
        

    @id.setter
    def id(self, id):
        """Sets the id of this SICIndex.

        Intrinio ID for the Index  # noqa: E501

        :param id: The id of this SICIndex.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def symbol(self):
        """Gets the symbol of this SICIndex.  # noqa: E501

        The symbol used to identify the Index  # noqa: E501

        :return: The symbol of this SICIndex.  # noqa: E501
        :rtype: str
        """
        return self._symbol
        
    @property
    def symbol_dict(self):
        """Gets the symbol of this SICIndex.  # noqa: E501

        The symbol used to identify the Index as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The symbol of this SICIndex.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.symbol
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'symbol': value }

        
        return result
        

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this SICIndex.

        The symbol used to identify the Index  # noqa: E501

        :param symbol: The symbol of this SICIndex.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def name(self):
        """Gets the name of this SICIndex.  # noqa: E501

        The name of the Index  # noqa: E501

        :return: The name of this SICIndex.  # noqa: E501
        :rtype: str
        """
        return self._name
        
    @property
    def name_dict(self):
        """Gets the name of this SICIndex.  # noqa: E501

        The name of the Index as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The name of this SICIndex.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.name
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'name': value }

        
        return result
        

    @name.setter
    def name(self, name):
        """Sets the name of this SICIndex.

        The name of the Index  # noqa: E501

        :param name: The name of this SICIndex.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def continent(self):
        """Gets the continent of this SICIndex.  # noqa: E501

        The continent of the country of focus for the Index  # noqa: E501

        :return: The continent of this SICIndex.  # noqa: E501
        :rtype: str
        """
        return self._continent
        
    @property
    def continent_dict(self):
        """Gets the continent of this SICIndex.  # noqa: E501

        The continent of the country of focus for the Index as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The continent of this SICIndex.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.continent
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'continent': value }

        
        return result
        

    @continent.setter
    def continent(self, continent):
        """Sets the continent of this SICIndex.

        The continent of the country of focus for the Index  # noqa: E501

        :param continent: The continent of this SICIndex.  # noqa: E501
        :type: str
        """

        self._continent = continent

    @property
    def country(self):
        """Gets the country of this SICIndex.  # noqa: E501

        The country of focus for the Index  # noqa: E501

        :return: The country of this SICIndex.  # noqa: E501
        :rtype: str
        """
        return self._country
        
    @property
    def country_dict(self):
        """Gets the country of this SICIndex.  # noqa: E501

        The country of focus for the Index as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The country of this SICIndex.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.country
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'country': value }

        
        return result
        

    @country.setter
    def country(self, country):
        """Sets the country of this SICIndex.

        The country of focus for the Index  # noqa: E501

        :param country: The country of this SICIndex.  # noqa: E501
        :type: str
        """

        self._country = country

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SICIndex):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
