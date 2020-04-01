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


class CurrencyPlanPrice(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, currency_code=None, currency_symbol=None, per_seat_price=None, supported_card_types=None, support_incident_fee=None, support_plan_fee=None):
        """
        CurrencyPlanPrice - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'currency_code': 'str',
            'currency_symbol': 'str',
            'per_seat_price': 'str',
            'supported_card_types': 'CreditCardTypes',
            'support_incident_fee': 'str',
            'support_plan_fee': 'str'
        }

        self.attribute_map = {
            'currency_code': 'currencyCode',
            'currency_symbol': 'currencySymbol',
            'per_seat_price': 'perSeatPrice',
            'supported_card_types': 'supportedCardTypes',
            'support_incident_fee': 'supportIncidentFee',
            'support_plan_fee': 'supportPlanFee'
        }

        self._currency_code = currency_code
        self._currency_symbol = currency_symbol
        self._per_seat_price = per_seat_price
        self._supported_card_types = supported_card_types
        self._support_incident_fee = support_incident_fee
        self._support_plan_fee = support_plan_fee

    @property
    def currency_code(self):
        """
        Gets the currency_code of this CurrencyPlanPrice.
        Specifies the ISO currency code for the account.

        :return: The currency_code of this CurrencyPlanPrice.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """
        Sets the currency_code of this CurrencyPlanPrice.
        Specifies the ISO currency code for the account.

        :param currency_code: The currency_code of this CurrencyPlanPrice.
        :type: str
        """

        self._currency_code = currency_code

    @property
    def currency_symbol(self):
        """
        Gets the currency_symbol of this CurrencyPlanPrice.
        Specifies the currency symbol for the account.

        :return: The currency_symbol of this CurrencyPlanPrice.
        :rtype: str
        """
        return self._currency_symbol

    @currency_symbol.setter
    def currency_symbol(self, currency_symbol):
        """
        Sets the currency_symbol of this CurrencyPlanPrice.
        Specifies the currency symbol for the account.

        :param currency_symbol: The currency_symbol of this CurrencyPlanPrice.
        :type: str
        """

        self._currency_symbol = currency_symbol

    @property
    def per_seat_price(self):
        """
        Gets the per_seat_price of this CurrencyPlanPrice.
        

        :return: The per_seat_price of this CurrencyPlanPrice.
        :rtype: str
        """
        return self._per_seat_price

    @per_seat_price.setter
    def per_seat_price(self, per_seat_price):
        """
        Sets the per_seat_price of this CurrencyPlanPrice.
        

        :param per_seat_price: The per_seat_price of this CurrencyPlanPrice.
        :type: str
        """

        self._per_seat_price = per_seat_price

    @property
    def supported_card_types(self):
        """
        Gets the supported_card_types of this CurrencyPlanPrice.

        :return: The supported_card_types of this CurrencyPlanPrice.
        :rtype: CreditCardTypes
        """
        return self._supported_card_types

    @supported_card_types.setter
    def supported_card_types(self, supported_card_types):
        """
        Sets the supported_card_types of this CurrencyPlanPrice.

        :param supported_card_types: The supported_card_types of this CurrencyPlanPrice.
        :type: CreditCardTypes
        """

        self._supported_card_types = supported_card_types

    @property
    def support_incident_fee(self):
        """
        Gets the support_incident_fee of this CurrencyPlanPrice.
        The support incident fee charged for each support incident.

        :return: The support_incident_fee of this CurrencyPlanPrice.
        :rtype: str
        """
        return self._support_incident_fee

    @support_incident_fee.setter
    def support_incident_fee(self, support_incident_fee):
        """
        Sets the support_incident_fee of this CurrencyPlanPrice.
        The support incident fee charged for each support incident.

        :param support_incident_fee: The support_incident_fee of this CurrencyPlanPrice.
        :type: str
        """

        self._support_incident_fee = support_incident_fee

    @property
    def support_plan_fee(self):
        """
        Gets the support_plan_fee of this CurrencyPlanPrice.
        The support plan fee charged for this plan.

        :return: The support_plan_fee of this CurrencyPlanPrice.
        :rtype: str
        """
        return self._support_plan_fee

    @support_plan_fee.setter
    def support_plan_fee(self, support_plan_fee):
        """
        Sets the support_plan_fee of this CurrencyPlanPrice.
        The support plan fee charged for this plan.

        :param support_plan_fee: The support_plan_fee of this CurrencyPlanPrice.
        :type: str
        """

        self._support_plan_fee = support_plan_fee

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
