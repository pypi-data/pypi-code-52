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


class BillingPlan(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, app_store_products=None, currency_plan_prices=None, enable_support=None, included_seats=None, other_discount_percent=None, payment_cycle=None, payment_method=None, per_seat_price=None, plan_classification=None, plan_feature_sets=None, plan_id=None, plan_name=None, seat_discounts=None, support_incident_fee=None, support_plan_fee=None):
        """
        BillingPlan - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'app_store_products': 'list[AppStoreProduct]',
            'currency_plan_prices': 'list[CurrencyPlanPrice]',
            'enable_support': 'str',
            'included_seats': 'str',
            'other_discount_percent': 'str',
            'payment_cycle': 'str',
            'payment_method': 'str',
            'per_seat_price': 'str',
            'plan_classification': 'str',
            'plan_feature_sets': 'list[FeatureSet]',
            'plan_id': 'str',
            'plan_name': 'str',
            'seat_discounts': 'list[SeatDiscount]',
            'support_incident_fee': 'str',
            'support_plan_fee': 'str'
        }

        self.attribute_map = {
            'app_store_products': 'appStoreProducts',
            'currency_plan_prices': 'currencyPlanPrices',
            'enable_support': 'enableSupport',
            'included_seats': 'includedSeats',
            'other_discount_percent': 'otherDiscountPercent',
            'payment_cycle': 'paymentCycle',
            'payment_method': 'paymentMethod',
            'per_seat_price': 'perSeatPrice',
            'plan_classification': 'planClassification',
            'plan_feature_sets': 'planFeatureSets',
            'plan_id': 'planId',
            'plan_name': 'planName',
            'seat_discounts': 'seatDiscounts',
            'support_incident_fee': 'supportIncidentFee',
            'support_plan_fee': 'supportPlanFee'
        }

        self._app_store_products = app_store_products
        self._currency_plan_prices = currency_plan_prices
        self._enable_support = enable_support
        self._included_seats = included_seats
        self._other_discount_percent = other_discount_percent
        self._payment_cycle = payment_cycle
        self._payment_method = payment_method
        self._per_seat_price = per_seat_price
        self._plan_classification = plan_classification
        self._plan_feature_sets = plan_feature_sets
        self._plan_id = plan_id
        self._plan_name = plan_name
        self._seat_discounts = seat_discounts
        self._support_incident_fee = support_incident_fee
        self._support_plan_fee = support_plan_fee

    @property
    def app_store_products(self):
        """
        Gets the app_store_products of this BillingPlan.
        Reserved: TBD

        :return: The app_store_products of this BillingPlan.
        :rtype: list[AppStoreProduct]
        """
        return self._app_store_products

    @app_store_products.setter
    def app_store_products(self, app_store_products):
        """
        Sets the app_store_products of this BillingPlan.
        Reserved: TBD

        :param app_store_products: The app_store_products of this BillingPlan.
        :type: list[AppStoreProduct]
        """

        self._app_store_products = app_store_products

    @property
    def currency_plan_prices(self):
        """
        Gets the currency_plan_prices of this BillingPlan.
        Contains the currencyCode and currencySymbol for the alternate currency values for envelopeFee, fixedFee, and seatFee that are configured for this plan feature set.

        :return: The currency_plan_prices of this BillingPlan.
        :rtype: list[CurrencyPlanPrice]
        """
        return self._currency_plan_prices

    @currency_plan_prices.setter
    def currency_plan_prices(self, currency_plan_prices):
        """
        Sets the currency_plan_prices of this BillingPlan.
        Contains the currencyCode and currencySymbol for the alternate currency values for envelopeFee, fixedFee, and seatFee that are configured for this plan feature set.

        :param currency_plan_prices: The currency_plan_prices of this BillingPlan.
        :type: list[CurrencyPlanPrice]
        """

        self._currency_plan_prices = currency_plan_prices

    @property
    def enable_support(self):
        """
        Gets the enable_support of this BillingPlan.
        When set to **true**, then customer support is provided as part of the account plan.

        :return: The enable_support of this BillingPlan.
        :rtype: str
        """
        return self._enable_support

    @enable_support.setter
    def enable_support(self, enable_support):
        """
        Sets the enable_support of this BillingPlan.
        When set to **true**, then customer support is provided as part of the account plan.

        :param enable_support: The enable_support of this BillingPlan.
        :type: str
        """

        self._enable_support = enable_support

    @property
    def included_seats(self):
        """
        Gets the included_seats of this BillingPlan.
        The number of seats (users) included.

        :return: The included_seats of this BillingPlan.
        :rtype: str
        """
        return self._included_seats

    @included_seats.setter
    def included_seats(self, included_seats):
        """
        Sets the included_seats of this BillingPlan.
        The number of seats (users) included.

        :param included_seats: The included_seats of this BillingPlan.
        :type: str
        """

        self._included_seats = included_seats

    @property
    def other_discount_percent(self):
        """
        Gets the other_discount_percent of this BillingPlan.
        

        :return: The other_discount_percent of this BillingPlan.
        :rtype: str
        """
        return self._other_discount_percent

    @other_discount_percent.setter
    def other_discount_percent(self, other_discount_percent):
        """
        Sets the other_discount_percent of this BillingPlan.
        

        :param other_discount_percent: The other_discount_percent of this BillingPlan.
        :type: str
        """

        self._other_discount_percent = other_discount_percent

    @property
    def payment_cycle(self):
        """
        Gets the payment_cycle of this BillingPlan.
         The payment cycle associated with the plan. The possible values are: Monthly or Annually. 

        :return: The payment_cycle of this BillingPlan.
        :rtype: str
        """
        return self._payment_cycle

    @payment_cycle.setter
    def payment_cycle(self, payment_cycle):
        """
        Sets the payment_cycle of this BillingPlan.
         The payment cycle associated with the plan. The possible values are: Monthly or Annually. 

        :param payment_cycle: The payment_cycle of this BillingPlan.
        :type: str
        """

        self._payment_cycle = payment_cycle

    @property
    def payment_method(self):
        """
        Gets the payment_method of this BillingPlan.
        

        :return: The payment_method of this BillingPlan.
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """
        Sets the payment_method of this BillingPlan.
        

        :param payment_method: The payment_method of this BillingPlan.
        :type: str
        """

        self._payment_method = payment_method

    @property
    def per_seat_price(self):
        """
        Gets the per_seat_price of this BillingPlan.
        The per seat price for the plan.

        :return: The per_seat_price of this BillingPlan.
        :rtype: str
        """
        return self._per_seat_price

    @per_seat_price.setter
    def per_seat_price(self, per_seat_price):
        """
        Sets the per_seat_price of this BillingPlan.
        The per seat price for the plan.

        :param per_seat_price: The per_seat_price of this BillingPlan.
        :type: str
        """

        self._per_seat_price = per_seat_price

    @property
    def plan_classification(self):
        """
        Gets the plan_classification of this BillingPlan.
        Identifies the type of plan. Examples include Business, Corporate, Enterprise, Free.

        :return: The plan_classification of this BillingPlan.
        :rtype: str
        """
        return self._plan_classification

    @plan_classification.setter
    def plan_classification(self, plan_classification):
        """
        Sets the plan_classification of this BillingPlan.
        Identifies the type of plan. Examples include Business, Corporate, Enterprise, Free.

        :param plan_classification: The plan_classification of this BillingPlan.
        :type: str
        """

        self._plan_classification = plan_classification

    @property
    def plan_feature_sets(self):
        """
        Gets the plan_feature_sets of this BillingPlan.
        

        :return: The plan_feature_sets of this BillingPlan.
        :rtype: list[FeatureSet]
        """
        return self._plan_feature_sets

    @plan_feature_sets.setter
    def plan_feature_sets(self, plan_feature_sets):
        """
        Sets the plan_feature_sets of this BillingPlan.
        

        :param plan_feature_sets: The plan_feature_sets of this BillingPlan.
        :type: list[FeatureSet]
        """

        self._plan_feature_sets = plan_feature_sets

    @property
    def plan_id(self):
        """
        Gets the plan_id of this BillingPlan.
        

        :return: The plan_id of this BillingPlan.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """
        Sets the plan_id of this BillingPlan.
        

        :param plan_id: The plan_id of this BillingPlan.
        :type: str
        """

        self._plan_id = plan_id

    @property
    def plan_name(self):
        """
        Gets the plan_name of this BillingPlan.
        The name of the Billing Plan.

        :return: The plan_name of this BillingPlan.
        :rtype: str
        """
        return self._plan_name

    @plan_name.setter
    def plan_name(self, plan_name):
        """
        Sets the plan_name of this BillingPlan.
        The name of the Billing Plan.

        :param plan_name: The plan_name of this BillingPlan.
        :type: str
        """

        self._plan_name = plan_name

    @property
    def seat_discounts(self):
        """
        Gets the seat_discounts of this BillingPlan.
        

        :return: The seat_discounts of this BillingPlan.
        :rtype: list[SeatDiscount]
        """
        return self._seat_discounts

    @seat_discounts.setter
    def seat_discounts(self, seat_discounts):
        """
        Sets the seat_discounts of this BillingPlan.
        

        :param seat_discounts: The seat_discounts of this BillingPlan.
        :type: list[SeatDiscount]
        """

        self._seat_discounts = seat_discounts

    @property
    def support_incident_fee(self):
        """
        Gets the support_incident_fee of this BillingPlan.
        The support incident fee charged for each support incident.

        :return: The support_incident_fee of this BillingPlan.
        :rtype: str
        """
        return self._support_incident_fee

    @support_incident_fee.setter
    def support_incident_fee(self, support_incident_fee):
        """
        Sets the support_incident_fee of this BillingPlan.
        The support incident fee charged for each support incident.

        :param support_incident_fee: The support_incident_fee of this BillingPlan.
        :type: str
        """

        self._support_incident_fee = support_incident_fee

    @property
    def support_plan_fee(self):
        """
        Gets the support_plan_fee of this BillingPlan.
        The support plan fee charged for this plan.

        :return: The support_plan_fee of this BillingPlan.
        :rtype: str
        """
        return self._support_plan_fee

    @support_plan_fee.setter
    def support_plan_fee(self, support_plan_fee):
        """
        Sets the support_plan_fee of this BillingPlan.
        The support plan fee charged for this plan.

        :param support_plan_fee: The support_plan_fee of this BillingPlan.
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
