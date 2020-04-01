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


class NotaryJournalCredibleWitness(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, address=None, name=None, signature_image=None):
        """
        NotaryJournalCredibleWitness - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'address': 'str',
            'name': 'str',
            'signature_image': 'str'
        }

        self.attribute_map = {
            'address': 'address',
            'name': 'name',
            'signature_image': 'signatureImage'
        }

        self._address = address
        self._name = name
        self._signature_image = signature_image

    @property
    def address(self):
        """
        Gets the address of this NotaryJournalCredibleWitness.
        

        :return: The address of this NotaryJournalCredibleWitness.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this NotaryJournalCredibleWitness.
        

        :param address: The address of this NotaryJournalCredibleWitness.
        :type: str
        """

        self._address = address

    @property
    def name(self):
        """
        Gets the name of this NotaryJournalCredibleWitness.
        

        :return: The name of this NotaryJournalCredibleWitness.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this NotaryJournalCredibleWitness.
        

        :param name: The name of this NotaryJournalCredibleWitness.
        :type: str
        """

        self._name = name

    @property
    def signature_image(self):
        """
        Gets the signature_image of this NotaryJournalCredibleWitness.
        

        :return: The signature_image of this NotaryJournalCredibleWitness.
        :rtype: str
        """
        return self._signature_image

    @signature_image.setter
    def signature_image(self, signature_image):
        """
        Sets the signature_image of this NotaryJournalCredibleWitness.
        

        :param signature_image: The signature_image of this NotaryJournalCredibleWitness.
        :type: str
        """

        self._signature_image = signature_image

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
