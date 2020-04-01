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


class AccountBillingPlanResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, billing_address=None, billing_address_is_credit_card_address=None, billing_plan=None, credit_card_information=None, payment_processor_information=None, referral_information=None, successor_plans=None):
        """
        AccountBillingPlanResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'billing_address': 'AccountAddress',
            'billing_address_is_credit_card_address': 'str',
            'billing_plan': 'AccountBillingPlan',
            'credit_card_information': 'CreditCardInformation',
            'payment_processor_information': 'PaymentProcessorInformation',
            'referral_information': 'ReferralInformation',
            'successor_plans': 'list[BillingPlan]'
        }

        self.attribute_map = {
            'billing_address': 'billingAddress',
            'billing_address_is_credit_card_address': 'billingAddressIsCreditCardAddress',
            'billing_plan': 'billingPlan',
            'credit_card_information': 'creditCardInformation',
            'payment_processor_information': 'paymentProcessorInformation',
            'referral_information': 'referralInformation',
            'successor_plans': 'successorPlans'
        }

        self._billing_address = billing_address
        self._billing_address_is_credit_card_address = billing_address_is_credit_card_address
        self._billing_plan = billing_plan
        self._credit_card_information = credit_card_information
        self._payment_processor_information = payment_processor_information
        self._referral_information = referral_information
        self._successor_plans = successor_plans

    @property
    def billing_address(self):
        """
        Gets the billing_address of this AccountBillingPlanResponse.

        :return: The billing_address of this AccountBillingPlanResponse.
        :rtype: AccountAddress
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """
        Sets the billing_address of this AccountBillingPlanResponse.

        :param billing_address: The billing_address of this AccountBillingPlanResponse.
        :type: AccountAddress
        """

        self._billing_address = billing_address

    @property
    def billing_address_is_credit_card_address(self):
        """
        Gets the billing_address_is_credit_card_address of this AccountBillingPlanResponse.
        When set to **true**, the credit card address information is the same as that returned as the billing address. If false, then the billing address is considered a billing contact address, and the credit card address can be different.

        :return: The billing_address_is_credit_card_address of this AccountBillingPlanResponse.
        :rtype: str
        """
        return self._billing_address_is_credit_card_address

    @billing_address_is_credit_card_address.setter
    def billing_address_is_credit_card_address(self, billing_address_is_credit_card_address):
        """
        Sets the billing_address_is_credit_card_address of this AccountBillingPlanResponse.
        When set to **true**, the credit card address information is the same as that returned as the billing address. If false, then the billing address is considered a billing contact address, and the credit card address can be different.

        :param billing_address_is_credit_card_address: The billing_address_is_credit_card_address of this AccountBillingPlanResponse.
        :type: str
        """

        self._billing_address_is_credit_card_address = billing_address_is_credit_card_address

    @property
    def billing_plan(self):
        """
        Gets the billing_plan of this AccountBillingPlanResponse.

        :return: The billing_plan of this AccountBillingPlanResponse.
        :rtype: AccountBillingPlan
        """
        return self._billing_plan

    @billing_plan.setter
    def billing_plan(self, billing_plan):
        """
        Sets the billing_plan of this AccountBillingPlanResponse.

        :param billing_plan: The billing_plan of this AccountBillingPlanResponse.
        :type: AccountBillingPlan
        """

        self._billing_plan = billing_plan

    @property
    def credit_card_information(self):
        """
        Gets the credit_card_information of this AccountBillingPlanResponse.

        :return: The credit_card_information of this AccountBillingPlanResponse.
        :rtype: CreditCardInformation
        """
        return self._credit_card_information

    @credit_card_information.setter
    def credit_card_information(self, credit_card_information):
        """
        Sets the credit_card_information of this AccountBillingPlanResponse.

        :param credit_card_information: The credit_card_information of this AccountBillingPlanResponse.
        :type: CreditCardInformation
        """

        self._credit_card_information = credit_card_information

    @property
    def payment_processor_information(self):
        """
        Gets the payment_processor_information of this AccountBillingPlanResponse.

        :return: The payment_processor_information of this AccountBillingPlanResponse.
        :rtype: PaymentProcessorInformation
        """
        return self._payment_processor_information

    @payment_processor_information.setter
    def payment_processor_information(self, payment_processor_information):
        """
        Sets the payment_processor_information of this AccountBillingPlanResponse.

        :param payment_processor_information: The payment_processor_information of this AccountBillingPlanResponse.
        :type: PaymentProcessorInformation
        """

        self._payment_processor_information = payment_processor_information

    @property
    def referral_information(self):
        """
        Gets the referral_information of this AccountBillingPlanResponse.

        :return: The referral_information of this AccountBillingPlanResponse.
        :rtype: ReferralInformation
        """
        return self._referral_information

    @referral_information.setter
    def referral_information(self, referral_information):
        """
        Sets the referral_information of this AccountBillingPlanResponse.

        :param referral_information: The referral_information of this AccountBillingPlanResponse.
        :type: ReferralInformation
        """

        self._referral_information = referral_information

    @property
    def successor_plans(self):
        """
        Gets the successor_plans of this AccountBillingPlanResponse.
        

        :return: The successor_plans of this AccountBillingPlanResponse.
        :rtype: list[BillingPlan]
        """
        return self._successor_plans

    @successor_plans.setter
    def successor_plans(self, successor_plans):
        """
        Sets the successor_plans of this AccountBillingPlanResponse.
        

        :param successor_plans: The successor_plans of this AccountBillingPlanResponse.
        :type: list[BillingPlan]
        """

        self._successor_plans = successor_plans

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
