# coding: utf-8

"""
A Python client package for accessing data from an API that uses the Consumer Data Standards.

Generated using the Swagger-Codegen CLI from a Swagger specification file of the Consumer Data Standards. 

NOT part of the official Consumer Data Standards' Project, nor any API implementation of the Standards. 
"""


import pprint
import re  # noqa: F401

import six


class BankingProductDepositRate(object):
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
        'deposit_rate_type': 'str',
        'rate': 'str',
        'calculation_frequency': 'str',
        'application_frequency': 'str',
        'tiers': 'list[BankingProductRateTier]',
        'additional_value': 'str',
        'additional_info': 'str',
        'additional_info_uri': 'str'
    }

    attribute_map = {
        'deposit_rate_type': 'depositRateType',
        'rate': 'rate',
        'calculation_frequency': 'calculationFrequency',
        'application_frequency': 'applicationFrequency',
        'tiers': 'tiers',
        'additional_value': 'additionalValue',
        'additional_info': 'additionalInfo',
        'additional_info_uri': 'additionalInfoUri'
    }

    def __init__(self, deposit_rate_type=None, rate=None, calculation_frequency=None, application_frequency=None, tiers=None, additional_value=None, additional_info=None, additional_info_uri=None):  # noqa: E501
        """BankingProductDepositRate - a model defined in Swagger"""  # noqa: E501

        self._deposit_rate_type = None
        self._rate = None
        self._calculation_frequency = None
        self._application_frequency = None
        self._tiers = None
        self._additional_value = None
        self._additional_info = None
        self._additional_info_uri = None
        self.discriminator = None

        self.deposit_rate_type = deposit_rate_type
        self.rate = rate
        if calculation_frequency is not None:
            self.calculation_frequency = calculation_frequency
        if application_frequency is not None:
            self.application_frequency = application_frequency
        if tiers is not None:
            self.tiers = tiers
        if additional_value is not None:
            self.additional_value = additional_value
        if additional_info is not None:
            self.additional_info = additional_info
        if additional_info_uri is not None:
            self.additional_info_uri = additional_info_uri

    @property
    def deposit_rate_type(self):
        """Gets the deposit_rate_type of this BankingProductDepositRate.  # noqa: E501

        The type of rate (base, bonus, etc). See the next section for an overview of valid values and their meaning  # noqa: E501

        :return: The deposit_rate_type of this BankingProductDepositRate.  # noqa: E501
        :rtype: str
        """
        return self._deposit_rate_type

    @deposit_rate_type.setter
    def deposit_rate_type(self, deposit_rate_type):
        """Sets the deposit_rate_type of this BankingProductDepositRate.

        The type of rate (base, bonus, etc). See the next section for an overview of valid values and their meaning  # noqa: E501

        :param deposit_rate_type: The deposit_rate_type of this BankingProductDepositRate.  # noqa: E501
        :type: str
        """
        if deposit_rate_type is None:
            raise ValueError("Invalid value for `deposit_rate_type`, must not be `None`")  # noqa: E501
        allowed_values = ["FIXED", "BONUS", "BUNDLE_BONUS", "VARIABLE", "INTRODUCTORY", "FLOATING", "MARKET_LINKED"]  # noqa: E501
        if deposit_rate_type not in allowed_values:
            raise ValueError(
                "Invalid value for `deposit_rate_type` ({0}), must be one of {1}"  # noqa: E501
                .format(deposit_rate_type, allowed_values)
            )

        self._deposit_rate_type = deposit_rate_type

    @property
    def rate(self):
        """Gets the rate of this BankingProductDepositRate.  # noqa: E501

        The rate to be applied  # noqa: E501

        :return: The rate of this BankingProductDepositRate.  # noqa: E501
        :rtype: str
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this BankingProductDepositRate.

        The rate to be applied  # noqa: E501

        :param rate: The rate of this BankingProductDepositRate.  # noqa: E501
        :type: str
        """
        if rate is None:
            raise ValueError("Invalid value for `rate`, must not be `None`")  # noqa: E501

        self._rate = rate

    @property
    def calculation_frequency(self):
        """Gets the calculation_frequency of this BankingProductDepositRate.  # noqa: E501

        The period after which the rate is applied to the balance to calculate the amount due for the period. Calculation of the amount is often daily (as balances may change) but accumulated until the total amount is 'applied' to the account (see applicationFrequency). Formatted according to [ISO 8601 Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations) (excludes recurrence syntax)  # noqa: E501

        :return: The calculation_frequency of this BankingProductDepositRate.  # noqa: E501
        :rtype: str
        """
        return self._calculation_frequency

    @calculation_frequency.setter
    def calculation_frequency(self, calculation_frequency):
        """Sets the calculation_frequency of this BankingProductDepositRate.

        The period after which the rate is applied to the balance to calculate the amount due for the period. Calculation of the amount is often daily (as balances may change) but accumulated until the total amount is 'applied' to the account (see applicationFrequency). Formatted according to [ISO 8601 Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations) (excludes recurrence syntax)  # noqa: E501

        :param calculation_frequency: The calculation_frequency of this BankingProductDepositRate.  # noqa: E501
        :type: str
        """

        self._calculation_frequency = calculation_frequency

    @property
    def application_frequency(self):
        """Gets the application_frequency of this BankingProductDepositRate.  # noqa: E501

        The period after which the calculated amount(s) (see calculationFrequency) are 'applied' (i.e. debited or credited) to the account. Formatted according to [ISO 8601 Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations) (excludes recurrence syntax)  # noqa: E501

        :return: The application_frequency of this BankingProductDepositRate.  # noqa: E501
        :rtype: str
        """
        return self._application_frequency

    @application_frequency.setter
    def application_frequency(self, application_frequency):
        """Sets the application_frequency of this BankingProductDepositRate.

        The period after which the calculated amount(s) (see calculationFrequency) are 'applied' (i.e. debited or credited) to the account. Formatted according to [ISO 8601 Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations) (excludes recurrence syntax)  # noqa: E501

        :param application_frequency: The application_frequency of this BankingProductDepositRate.  # noqa: E501
        :type: str
        """

        self._application_frequency = application_frequency

    @property
    def tiers(self):
        """Gets the tiers of this BankingProductDepositRate.  # noqa: E501

        Rate tiers applicable for this rate  # noqa: E501

        :return: The tiers of this BankingProductDepositRate.  # noqa: E501
        :rtype: list[BankingProductRateTier]
        """
        return self._tiers

    @tiers.setter
    def tiers(self, tiers):
        """Sets the tiers of this BankingProductDepositRate.

        Rate tiers applicable for this rate  # noqa: E501

        :param tiers: The tiers of this BankingProductDepositRate.  # noqa: E501
        :type: list[BankingProductRateTier]
        """

        self._tiers = tiers

    @property
    def additional_value(self):
        """Gets the additional_value of this BankingProductDepositRate.  # noqa: E501

        Generic field containing additional information relevant to the [depositRateType](#tocSproductdepositratetypedoc) specified. Whether mandatory or not is dependent on the value of [depositRateType](#tocSproductdepositratetypedoc)  # noqa: E501

        :return: The additional_value of this BankingProductDepositRate.  # noqa: E501
        :rtype: str
        """
        return self._additional_value

    @additional_value.setter
    def additional_value(self, additional_value):
        """Sets the additional_value of this BankingProductDepositRate.

        Generic field containing additional information relevant to the [depositRateType](#tocSproductdepositratetypedoc) specified. Whether mandatory or not is dependent on the value of [depositRateType](#tocSproductdepositratetypedoc)  # noqa: E501

        :param additional_value: The additional_value of this BankingProductDepositRate.  # noqa: E501
        :type: str
        """

        self._additional_value = additional_value

    @property
    def additional_info(self):
        """Gets the additional_info of this BankingProductDepositRate.  # noqa: E501

        Display text providing more information on the rate  # noqa: E501

        :return: The additional_info of this BankingProductDepositRate.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this BankingProductDepositRate.

        Display text providing more information on the rate  # noqa: E501

        :param additional_info: The additional_info of this BankingProductDepositRate.  # noqa: E501
        :type: str
        """

        self._additional_info = additional_info

    @property
    def additional_info_uri(self):
        """Gets the additional_info_uri of this BankingProductDepositRate.  # noqa: E501

        Link to a web page with more information on this rate  # noqa: E501

        :return: The additional_info_uri of this BankingProductDepositRate.  # noqa: E501
        :rtype: str
        """
        return self._additional_info_uri

    @additional_info_uri.setter
    def additional_info_uri(self, additional_info_uri):
        """Sets the additional_info_uri of this BankingProductDepositRate.

        Link to a web page with more information on this rate  # noqa: E501

        :param additional_info_uri: The additional_info_uri of this BankingProductDepositRate.  # noqa: E501
        :type: str
        """

        self._additional_info_uri = additional_info_uri

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
        if issubclass(BankingProductDepositRate, dict):
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
        if not isinstance(other, BankingProductDepositRate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
