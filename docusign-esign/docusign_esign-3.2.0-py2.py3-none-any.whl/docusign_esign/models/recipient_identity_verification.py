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


class RecipientIdentityVerification(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, input_options=None, workflow_id=None):
        """
        RecipientIdentityVerification - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'input_options': 'list[RecipientIdentityInputOption]',
            'workflow_id': 'str'
        }

        self.attribute_map = {
            'input_options': 'inputOptions',
            'workflow_id': 'workflowId'
        }

        self._input_options = input_options
        self._workflow_id = workflow_id

    @property
    def input_options(self):
        """
        Gets the input_options of this RecipientIdentityVerification.
        

        :return: The input_options of this RecipientIdentityVerification.
        :rtype: list[RecipientIdentityInputOption]
        """
        return self._input_options

    @input_options.setter
    def input_options(self, input_options):
        """
        Sets the input_options of this RecipientIdentityVerification.
        

        :param input_options: The input_options of this RecipientIdentityVerification.
        :type: list[RecipientIdentityInputOption]
        """

        self._input_options = input_options

    @property
    def workflow_id(self):
        """
        Gets the workflow_id of this RecipientIdentityVerification.
        

        :return: The workflow_id of this RecipientIdentityVerification.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """
        Sets the workflow_id of this RecipientIdentityVerification.
        

        :param workflow_id: The workflow_id of this RecipientIdentityVerification.
        :type: str
        """

        self._workflow_id = workflow_id

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
