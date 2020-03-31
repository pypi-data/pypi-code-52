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

from intrinio_sdk.models.security_summary import SecuritySummary  # noqa: F401,E501


class DividendRecord(object):
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
        'ex_dividend': 'float',
        'currency': 'str',
        'announcement_date': 'date',
        'record_date': 'date',
        'pay_date': 'date',
        'frequency': 'str',
        'status': 'str',
        'forward_yield': 'float',
        'forward_rate': 'float',
        'last_ex_dividend_date': 'date',
        'security': 'SecuritySummary'
    }

    attribute_map = {
        'ex_dividend': 'ex_dividend',
        'currency': 'currency',
        'announcement_date': 'announcement_date',
        'record_date': 'record_date',
        'pay_date': 'pay_date',
        'frequency': 'frequency',
        'status': 'status',
        'forward_yield': 'forward_yield',
        'forward_rate': 'forward_rate',
        'last_ex_dividend_date': 'last_ex_dividend_date',
        'security': 'security'
    }

    def __init__(self, ex_dividend=None, currency=None, announcement_date=None, record_date=None, pay_date=None, frequency=None, status=None, forward_yield=None, forward_rate=None, last_ex_dividend_date=None, security=None):  # noqa: E501
        """DividendRecord - a model defined in Swagger"""  # noqa: E501

        self._ex_dividend = None
        self._currency = None
        self._announcement_date = None
        self._record_date = None
        self._pay_date = None
        self._frequency = None
        self._status = None
        self._forward_yield = None
        self._forward_rate = None
        self._last_ex_dividend_date = None
        self._security = None
        self.discriminator = None

        if ex_dividend is not None:
            self.ex_dividend = ex_dividend
        if currency is not None:
            self.currency = currency
        if announcement_date is not None:
            self.announcement_date = announcement_date
        if record_date is not None:
            self.record_date = record_date
        if pay_date is not None:
            self.pay_date = pay_date
        if frequency is not None:
            self.frequency = frequency
        if status is not None:
            self.status = status
        if forward_yield is not None:
            self.forward_yield = forward_yield
        if forward_rate is not None:
            self.forward_rate = forward_rate
        if last_ex_dividend_date is not None:
            self.last_ex_dividend_date = last_ex_dividend_date
        if security is not None:
            self.security = security

    @property
    def ex_dividend(self):
        """Gets the ex_dividend of this DividendRecord.  # noqa: E501

        Amount of dividend in US dollars  # noqa: E501

        :return: The ex_dividend of this DividendRecord.  # noqa: E501
        :rtype: float
        """
        return self._ex_dividend
        
    @property
    def ex_dividend_dict(self):
        """Gets the ex_dividend of this DividendRecord.  # noqa: E501

        Amount of dividend in US dollars as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The ex_dividend of this DividendRecord.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.ex_dividend
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
            result = { 'ex_dividend': value }

        
        return result
        

    @ex_dividend.setter
    def ex_dividend(self, ex_dividend):
        """Sets the ex_dividend of this DividendRecord.

        Amount of dividend in US dollars  # noqa: E501

        :param ex_dividend: The ex_dividend of this DividendRecord.  # noqa: E501
        :type: float
        """

        self._ex_dividend = ex_dividend

    @property
    def currency(self):
        """Gets the currency of this DividendRecord.  # noqa: E501

        The 3-digit currency code the dividend amount was reported in  # noqa: E501

        :return: The currency of this DividendRecord.  # noqa: E501
        :rtype: str
        """
        return self._currency
        
    @property
    def currency_dict(self):
        """Gets the currency of this DividendRecord.  # noqa: E501

        The 3-digit currency code the dividend amount was reported in as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The currency of this DividendRecord.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.currency
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
            result = { 'currency': value }

        
        return result
        

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this DividendRecord.

        The 3-digit currency code the dividend amount was reported in  # noqa: E501

        :param currency: The currency of this DividendRecord.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def announcement_date(self):
        """Gets the announcement_date of this DividendRecord.  # noqa: E501

        Date dividend was announced  # noqa: E501

        :return: The announcement_date of this DividendRecord.  # noqa: E501
        :rtype: date
        """
        return self._announcement_date
        
    @property
    def announcement_date_dict(self):
        """Gets the announcement_date of this DividendRecord.  # noqa: E501

        Date dividend was announced as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The announcement_date of this DividendRecord.  # noqa: E501
        :rtype: date
        """

        result = None

        value = self.announcement_date
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
            result = { 'announcement_date': value }

        
        return result
        

    @announcement_date.setter
    def announcement_date(self, announcement_date):
        """Sets the announcement_date of this DividendRecord.

        Date dividend was announced  # noqa: E501

        :param announcement_date: The announcement_date of this DividendRecord.  # noqa: E501
        :type: date
        """

        self._announcement_date = announcement_date

    @property
    def record_date(self):
        """Gets the record_date of this DividendRecord.  # noqa: E501

        Date before which holders-of-record will receive the dividend  # noqa: E501

        :return: The record_date of this DividendRecord.  # noqa: E501
        :rtype: date
        """
        return self._record_date
        
    @property
    def record_date_dict(self):
        """Gets the record_date of this DividendRecord.  # noqa: E501

        Date before which holders-of-record will receive the dividend as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The record_date of this DividendRecord.  # noqa: E501
        :rtype: date
        """

        result = None

        value = self.record_date
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
            result = { 'record_date': value }

        
        return result
        

    @record_date.setter
    def record_date(self, record_date):
        """Sets the record_date of this DividendRecord.

        Date before which holders-of-record will receive the dividend  # noqa: E501

        :param record_date: The record_date of this DividendRecord.  # noqa: E501
        :type: date
        """

        self._record_date = record_date

    @property
    def pay_date(self):
        """Gets the pay_date of this DividendRecord.  # noqa: E501

        Date the divdiend was paid  # noqa: E501

        :return: The pay_date of this DividendRecord.  # noqa: E501
        :rtype: date
        """
        return self._pay_date
        
    @property
    def pay_date_dict(self):
        """Gets the pay_date of this DividendRecord.  # noqa: E501

        Date the divdiend was paid as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The pay_date of this DividendRecord.  # noqa: E501
        :rtype: date
        """

        result = None

        value = self.pay_date
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
            result = { 'pay_date': value }

        
        return result
        

    @pay_date.setter
    def pay_date(self, pay_date):
        """Sets the pay_date of this DividendRecord.

        Date the divdiend was paid  # noqa: E501

        :param pay_date: The pay_date of this DividendRecord.  # noqa: E501
        :type: date
        """

        self._pay_date = pay_date

    @property
    def frequency(self):
        """Gets the frequency of this DividendRecord.  # noqa: E501

        Identifies payment frequency of announced dividend  # noqa: E501

        :return: The frequency of this DividendRecord.  # noqa: E501
        :rtype: str
        """
        return self._frequency
        
    @property
    def frequency_dict(self):
        """Gets the frequency of this DividendRecord.  # noqa: E501

        Identifies payment frequency of announced dividend as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The frequency of this DividendRecord.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.frequency
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
            result = { 'frequency': value }

        
        return result
        

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this DividendRecord.

        Identifies payment frequency of announced dividend  # noqa: E501

        :param frequency: The frequency of this DividendRecord.  # noqa: E501
        :type: str
        """

        self._frequency = frequency

    @property
    def status(self):
        """Gets the status of this DividendRecord.  # noqa: E501

        Status of the dividend  # noqa: E501

        :return: The status of this DividendRecord.  # noqa: E501
        :rtype: str
        """
        return self._status
        
    @property
    def status_dict(self):
        """Gets the status of this DividendRecord.  # noqa: E501

        Status of the dividend as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The status of this DividendRecord.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.status
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
            result = { 'status': value }

        
        return result
        

    @status.setter
    def status(self, status):
        """Sets the status of this DividendRecord.

        Status of the dividend  # noqa: E501

        :param status: The status of this DividendRecord.  # noqa: E501
        :type: str
        """
        allowed_values = ["P", "X", "S", "R"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def forward_yield(self):
        """Gets the forward_yield of this DividendRecord.  # noqa: E501

        The forward dividend yield  # noqa: E501

        :return: The forward_yield of this DividendRecord.  # noqa: E501
        :rtype: float
        """
        return self._forward_yield
        
    @property
    def forward_yield_dict(self):
        """Gets the forward_yield of this DividendRecord.  # noqa: E501

        The forward dividend yield as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The forward_yield of this DividendRecord.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.forward_yield
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
            result = { 'forward_yield': value }

        
        return result
        

    @forward_yield.setter
    def forward_yield(self, forward_yield):
        """Sets the forward_yield of this DividendRecord.

        The forward dividend yield  # noqa: E501

        :param forward_yield: The forward_yield of this DividendRecord.  # noqa: E501
        :type: float
        """

        self._forward_yield = forward_yield

    @property
    def forward_rate(self):
        """Gets the forward_rate of this DividendRecord.  # noqa: E501

        The forward dividend rate  # noqa: E501

        :return: The forward_rate of this DividendRecord.  # noqa: E501
        :rtype: float
        """
        return self._forward_rate
        
    @property
    def forward_rate_dict(self):
        """Gets the forward_rate of this DividendRecord.  # noqa: E501

        The forward dividend rate as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The forward_rate of this DividendRecord.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.forward_rate
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
            result = { 'forward_rate': value }

        
        return result
        

    @forward_rate.setter
    def forward_rate(self, forward_rate):
        """Sets the forward_rate of this DividendRecord.

        The forward dividend rate  # noqa: E501

        :param forward_rate: The forward_rate of this DividendRecord.  # noqa: E501
        :type: float
        """

        self._forward_rate = forward_rate

    @property
    def last_ex_dividend_date(self):
        """Gets the last_ex_dividend_date of this DividendRecord.  # noqa: E501

        The last reported day the stock starts trading without the value of its next dividend payment  # noqa: E501

        :return: The last_ex_dividend_date of this DividendRecord.  # noqa: E501
        :rtype: date
        """
        return self._last_ex_dividend_date
        
    @property
    def last_ex_dividend_date_dict(self):
        """Gets the last_ex_dividend_date of this DividendRecord.  # noqa: E501

        The last reported day the stock starts trading without the value of its next dividend payment as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The last_ex_dividend_date of this DividendRecord.  # noqa: E501
        :rtype: date
        """

        result = None

        value = self.last_ex_dividend_date
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
            result = { 'last_ex_dividend_date': value }

        
        return result
        

    @last_ex_dividend_date.setter
    def last_ex_dividend_date(self, last_ex_dividend_date):
        """Sets the last_ex_dividend_date of this DividendRecord.

        The last reported day the stock starts trading without the value of its next dividend payment  # noqa: E501

        :param last_ex_dividend_date: The last_ex_dividend_date of this DividendRecord.  # noqa: E501
        :type: date
        """

        self._last_ex_dividend_date = last_ex_dividend_date

    @property
    def security(self):
        """Gets the security of this DividendRecord.  # noqa: E501


        :return: The security of this DividendRecord.  # noqa: E501
        :rtype: SecuritySummary
        """
        return self._security
        
    @property
    def security_dict(self):
        """Gets the security of this DividendRecord.  # noqa: E501


        :return: The security of this DividendRecord.  # noqa: E501
        :rtype: SecuritySummary
        """

        result = None

        value = self.security
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
            result = { 'security': value }

        
        return result
        

    @security.setter
    def security(self, security):
        """Sets the security of this DividendRecord.


        :param security: The security of this DividendRecord.  # noqa: E501
        :type: SecuritySummary
        """

        self._security = security

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
        if not isinstance(other, DividendRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
