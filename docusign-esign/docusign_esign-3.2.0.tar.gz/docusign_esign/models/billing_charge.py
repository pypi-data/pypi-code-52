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


class BillingCharge(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, allowed_quantity=None, blocked=None, charge_name=None, charge_type=None, charge_unit_of_measure=None, discounts=None, first_effective_date=None, included_quantity=None, incremental_quantity=None, last_effective_date=None, prices=None, unit_price=None, used_quantity=None):
        """
        BillingCharge - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'allowed_quantity': 'str',
            'blocked': 'str',
            'charge_name': 'str',
            'charge_type': 'str',
            'charge_unit_of_measure': 'str',
            'discounts': 'list[BillingDiscount]',
            'first_effective_date': 'str',
            'included_quantity': 'str',
            'incremental_quantity': 'str',
            'last_effective_date': 'str',
            'prices': 'list[BillingPrice]',
            'unit_price': 'str',
            'used_quantity': 'str'
        }

        self.attribute_map = {
            'allowed_quantity': 'allowedQuantity',
            'blocked': 'blocked',
            'charge_name': 'chargeName',
            'charge_type': 'chargeType',
            'charge_unit_of_measure': 'chargeUnitOfMeasure',
            'discounts': 'discounts',
            'first_effective_date': 'firstEffectiveDate',
            'included_quantity': 'includedQuantity',
            'incremental_quantity': 'incrementalQuantity',
            'last_effective_date': 'lastEffectiveDate',
            'prices': 'prices',
            'unit_price': 'unitPrice',
            'used_quantity': 'usedQuantity'
        }

        self._allowed_quantity = allowed_quantity
        self._blocked = blocked
        self._charge_name = charge_name
        self._charge_type = charge_type
        self._charge_unit_of_measure = charge_unit_of_measure
        self._discounts = discounts
        self._first_effective_date = first_effective_date
        self._included_quantity = included_quantity
        self._incremental_quantity = incremental_quantity
        self._last_effective_date = last_effective_date
        self._prices = prices
        self._unit_price = unit_price
        self._used_quantity = used_quantity

    @property
    def allowed_quantity(self):
        """
        Gets the allowed_quantity of this BillingCharge.
        Reserved: TBD

        :return: The allowed_quantity of this BillingCharge.
        :rtype: str
        """
        return self._allowed_quantity

    @allowed_quantity.setter
    def allowed_quantity(self, allowed_quantity):
        """
        Sets the allowed_quantity of this BillingCharge.
        Reserved: TBD

        :param allowed_quantity: The allowed_quantity of this BillingCharge.
        :type: str
        """

        self._allowed_quantity = allowed_quantity

    @property
    def blocked(self):
        """
        Gets the blocked of this BillingCharge.
        Reserved: TBD

        :return: The blocked of this BillingCharge.
        :rtype: str
        """
        return self._blocked

    @blocked.setter
    def blocked(self, blocked):
        """
        Sets the blocked of this BillingCharge.
        Reserved: TBD

        :param blocked: The blocked of this BillingCharge.
        :type: str
        """

        self._blocked = blocked

    @property
    def charge_name(self):
        """
        Gets the charge_name of this BillingCharge.
        Provides information on what services the charge item is for.  The following table provides a description of the different chargeName values available at this time.  | chargeName | Description | | --- | --- | | id_check | IDÃÂ Check Charge | | in_person_signing | In Person Signing charge | | envelopes Included | Sent Envelopes for the account | | age_verify | Age verification check | | ofac | OFAC Check | | id_confirm | ID confirmation check | | student_authentication | STAN PIN authentication check | | wet_sign_fax | Pages for returning signed documents by fax | | attachment_fax | Pages for returning attachments by fax | | phone_authentication | Phone authentication charge | | powerforms | PowerForm envelopes sent | | signer_payments | Payment processing charge | | outbound_fax | Send by fax charge | | bulk_recipient_envelopes | Bulk Recipient Envelopes sent | | sms_authentications | SMS authentication charge | | saml_authentications | SAML authentication charge | | express_signer_certificate | DocuSign Express Certificate charge | | personal_signer_certificate | Personal Signer Certificate charge | | safe_certificate | SAFE BioPharma Signer Certificate charge | | seats | Included active seats charge | | open_trust_certificate | OpenTrust Signer Certificate charge |

        :return: The charge_name of this BillingCharge.
        :rtype: str
        """
        return self._charge_name

    @charge_name.setter
    def charge_name(self, charge_name):
        """
        Sets the charge_name of this BillingCharge.
        Provides information on what services the charge item is for.  The following table provides a description of the different chargeName values available at this time.  | chargeName | Description | | --- | --- | | id_check | IDÃÂ Check Charge | | in_person_signing | In Person Signing charge | | envelopes Included | Sent Envelopes for the account | | age_verify | Age verification check | | ofac | OFAC Check | | id_confirm | ID confirmation check | | student_authentication | STAN PIN authentication check | | wet_sign_fax | Pages for returning signed documents by fax | | attachment_fax | Pages for returning attachments by fax | | phone_authentication | Phone authentication charge | | powerforms | PowerForm envelopes sent | | signer_payments | Payment processing charge | | outbound_fax | Send by fax charge | | bulk_recipient_envelopes | Bulk Recipient Envelopes sent | | sms_authentications | SMS authentication charge | | saml_authentications | SAML authentication charge | | express_signer_certificate | DocuSign Express Certificate charge | | personal_signer_certificate | Personal Signer Certificate charge | | safe_certificate | SAFE BioPharma Signer Certificate charge | | seats | Included active seats charge | | open_trust_certificate | OpenTrust Signer Certificate charge |

        :param charge_name: The charge_name of this BillingCharge.
        :type: str
        """

        self._charge_name = charge_name

    @property
    def charge_type(self):
        """
        Gets the charge_type of this BillingCharge.
        Reserved: TBD

        :return: The charge_type of this BillingCharge.
        :rtype: str
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """
        Sets the charge_type of this BillingCharge.
        Reserved: TBD

        :param charge_type: The charge_type of this BillingCharge.
        :type: str
        """

        self._charge_type = charge_type

    @property
    def charge_unit_of_measure(self):
        """
        Gets the charge_unit_of_measure of this BillingCharge.
        Reserved: TBD

        :return: The charge_unit_of_measure of this BillingCharge.
        :rtype: str
        """
        return self._charge_unit_of_measure

    @charge_unit_of_measure.setter
    def charge_unit_of_measure(self, charge_unit_of_measure):
        """
        Sets the charge_unit_of_measure of this BillingCharge.
        Reserved: TBD

        :param charge_unit_of_measure: The charge_unit_of_measure of this BillingCharge.
        :type: str
        """

        self._charge_unit_of_measure = charge_unit_of_measure

    @property
    def discounts(self):
        """
        Gets the discounts of this BillingCharge.
        

        :return: The discounts of this BillingCharge.
        :rtype: list[BillingDiscount]
        """
        return self._discounts

    @discounts.setter
    def discounts(self, discounts):
        """
        Sets the discounts of this BillingCharge.
        

        :param discounts: The discounts of this BillingCharge.
        :type: list[BillingDiscount]
        """

        self._discounts = discounts

    @property
    def first_effective_date(self):
        """
        Gets the first_effective_date of this BillingCharge.
        

        :return: The first_effective_date of this BillingCharge.
        :rtype: str
        """
        return self._first_effective_date

    @first_effective_date.setter
    def first_effective_date(self, first_effective_date):
        """
        Sets the first_effective_date of this BillingCharge.
        

        :param first_effective_date: The first_effective_date of this BillingCharge.
        :type: str
        """

        self._first_effective_date = first_effective_date

    @property
    def included_quantity(self):
        """
        Gets the included_quantity of this BillingCharge.
        

        :return: The included_quantity of this BillingCharge.
        :rtype: str
        """
        return self._included_quantity

    @included_quantity.setter
    def included_quantity(self, included_quantity):
        """
        Sets the included_quantity of this BillingCharge.
        

        :param included_quantity: The included_quantity of this BillingCharge.
        :type: str
        """

        self._included_quantity = included_quantity

    @property
    def incremental_quantity(self):
        """
        Gets the incremental_quantity of this BillingCharge.
        Reserved: TBD

        :return: The incremental_quantity of this BillingCharge.
        :rtype: str
        """
        return self._incremental_quantity

    @incremental_quantity.setter
    def incremental_quantity(self, incremental_quantity):
        """
        Sets the incremental_quantity of this BillingCharge.
        Reserved: TBD

        :param incremental_quantity: The incremental_quantity of this BillingCharge.
        :type: str
        """

        self._incremental_quantity = incremental_quantity

    @property
    def last_effective_date(self):
        """
        Gets the last_effective_date of this BillingCharge.
        

        :return: The last_effective_date of this BillingCharge.
        :rtype: str
        """
        return self._last_effective_date

    @last_effective_date.setter
    def last_effective_date(self, last_effective_date):
        """
        Sets the last_effective_date of this BillingCharge.
        

        :param last_effective_date: The last_effective_date of this BillingCharge.
        :type: str
        """

        self._last_effective_date = last_effective_date

    @property
    def prices(self):
        """
        Gets the prices of this BillingCharge.
        

        :return: The prices of this BillingCharge.
        :rtype: list[BillingPrice]
        """
        return self._prices

    @prices.setter
    def prices(self, prices):
        """
        Sets the prices of this BillingCharge.
        

        :param prices: The prices of this BillingCharge.
        :type: list[BillingPrice]
        """

        self._prices = prices

    @property
    def unit_price(self):
        """
        Gets the unit_price of this BillingCharge.
        Reserved: TBD

        :return: The unit_price of this BillingCharge.
        :rtype: str
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """
        Sets the unit_price of this BillingCharge.
        Reserved: TBD

        :param unit_price: The unit_price of this BillingCharge.
        :type: str
        """

        self._unit_price = unit_price

    @property
    def used_quantity(self):
        """
        Gets the used_quantity of this BillingCharge.
        

        :return: The used_quantity of this BillingCharge.
        :rtype: str
        """
        return self._used_quantity

    @used_quantity.setter
    def used_quantity(self, used_quantity):
        """
        Sets the used_quantity of this BillingCharge.
        

        :param used_quantity: The used_quantity of this BillingCharge.
        :type: str
        """

        self._used_quantity = used_quantity

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
