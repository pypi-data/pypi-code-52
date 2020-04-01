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


class BillingPayment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, amount=None, invoice_id=None, payment_id=None):
        """
        BillingPayment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'amount': 'str',
            'invoice_id': 'str',
            'payment_id': 'str'
        }

        self.attribute_map = {
            'amount': 'amount',
            'invoice_id': 'invoiceId',
            'payment_id': 'paymentId'
        }

        self._amount = amount
        self._invoice_id = invoice_id
        self._payment_id = payment_id

    @property
    def amount(self):
        """
        Gets the amount of this BillingPayment.
        Reserved: TBD

        :return: The amount of this BillingPayment.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this BillingPayment.
        Reserved: TBD

        :param amount: The amount of this BillingPayment.
        :type: str
        """

        self._amount = amount

    @property
    def invoice_id(self):
        """
        Gets the invoice_id of this BillingPayment.
        Reserved: TBD

        :return: The invoice_id of this BillingPayment.
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """
        Sets the invoice_id of this BillingPayment.
        Reserved: TBD

        :param invoice_id: The invoice_id of this BillingPayment.
        :type: str
        """

        self._invoice_id = invoice_id

    @property
    def payment_id(self):
        """
        Gets the payment_id of this BillingPayment.
        

        :return: The payment_id of this BillingPayment.
        :rtype: str
        """
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        """
        Sets the payment_id of this BillingPayment.
        

        :param payment_id: The payment_id of this BillingPayment.
        :type: str
        """

        self._payment_id = payment_id

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
