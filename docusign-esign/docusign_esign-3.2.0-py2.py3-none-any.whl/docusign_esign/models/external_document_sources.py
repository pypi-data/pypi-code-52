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


class ExternalDocumentSources(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, boxnet_enabled=None, boxnet_metadata=None, dropbox_enabled=None, dropbox_metadata=None, google_drive_enabled=None, google_drive_metadata=None, one_drive_enabled=None, one_drive_metadata=None, salesforce_enabled=None, salesforce_metadata=None):
        """
        ExternalDocumentSources - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'boxnet_enabled': 'str',
            'boxnet_metadata': 'SettingsMetadata',
            'dropbox_enabled': 'str',
            'dropbox_metadata': 'SettingsMetadata',
            'google_drive_enabled': 'str',
            'google_drive_metadata': 'SettingsMetadata',
            'one_drive_enabled': 'str',
            'one_drive_metadata': 'SettingsMetadata',
            'salesforce_enabled': 'str',
            'salesforce_metadata': 'SettingsMetadata'
        }

        self.attribute_map = {
            'boxnet_enabled': 'boxnetEnabled',
            'boxnet_metadata': 'boxnetMetadata',
            'dropbox_enabled': 'dropboxEnabled',
            'dropbox_metadata': 'dropboxMetadata',
            'google_drive_enabled': 'googleDriveEnabled',
            'google_drive_metadata': 'googleDriveMetadata',
            'one_drive_enabled': 'oneDriveEnabled',
            'one_drive_metadata': 'oneDriveMetadata',
            'salesforce_enabled': 'salesforceEnabled',
            'salesforce_metadata': 'salesforceMetadata'
        }

        self._boxnet_enabled = boxnet_enabled
        self._boxnet_metadata = boxnet_metadata
        self._dropbox_enabled = dropbox_enabled
        self._dropbox_metadata = dropbox_metadata
        self._google_drive_enabled = google_drive_enabled
        self._google_drive_metadata = google_drive_metadata
        self._one_drive_enabled = one_drive_enabled
        self._one_drive_metadata = one_drive_metadata
        self._salesforce_enabled = salesforce_enabled
        self._salesforce_metadata = salesforce_metadata

    @property
    def boxnet_enabled(self):
        """
        Gets the boxnet_enabled of this ExternalDocumentSources.
        

        :return: The boxnet_enabled of this ExternalDocumentSources.
        :rtype: str
        """
        return self._boxnet_enabled

    @boxnet_enabled.setter
    def boxnet_enabled(self, boxnet_enabled):
        """
        Sets the boxnet_enabled of this ExternalDocumentSources.
        

        :param boxnet_enabled: The boxnet_enabled of this ExternalDocumentSources.
        :type: str
        """

        self._boxnet_enabled = boxnet_enabled

    @property
    def boxnet_metadata(self):
        """
        Gets the boxnet_metadata of this ExternalDocumentSources.

        :return: The boxnet_metadata of this ExternalDocumentSources.
        :rtype: SettingsMetadata
        """
        return self._boxnet_metadata

    @boxnet_metadata.setter
    def boxnet_metadata(self, boxnet_metadata):
        """
        Sets the boxnet_metadata of this ExternalDocumentSources.

        :param boxnet_metadata: The boxnet_metadata of this ExternalDocumentSources.
        :type: SettingsMetadata
        """

        self._boxnet_metadata = boxnet_metadata

    @property
    def dropbox_enabled(self):
        """
        Gets the dropbox_enabled of this ExternalDocumentSources.
        

        :return: The dropbox_enabled of this ExternalDocumentSources.
        :rtype: str
        """
        return self._dropbox_enabled

    @dropbox_enabled.setter
    def dropbox_enabled(self, dropbox_enabled):
        """
        Sets the dropbox_enabled of this ExternalDocumentSources.
        

        :param dropbox_enabled: The dropbox_enabled of this ExternalDocumentSources.
        :type: str
        """

        self._dropbox_enabled = dropbox_enabled

    @property
    def dropbox_metadata(self):
        """
        Gets the dropbox_metadata of this ExternalDocumentSources.

        :return: The dropbox_metadata of this ExternalDocumentSources.
        :rtype: SettingsMetadata
        """
        return self._dropbox_metadata

    @dropbox_metadata.setter
    def dropbox_metadata(self, dropbox_metadata):
        """
        Sets the dropbox_metadata of this ExternalDocumentSources.

        :param dropbox_metadata: The dropbox_metadata of this ExternalDocumentSources.
        :type: SettingsMetadata
        """

        self._dropbox_metadata = dropbox_metadata

    @property
    def google_drive_enabled(self):
        """
        Gets the google_drive_enabled of this ExternalDocumentSources.
        

        :return: The google_drive_enabled of this ExternalDocumentSources.
        :rtype: str
        """
        return self._google_drive_enabled

    @google_drive_enabled.setter
    def google_drive_enabled(self, google_drive_enabled):
        """
        Sets the google_drive_enabled of this ExternalDocumentSources.
        

        :param google_drive_enabled: The google_drive_enabled of this ExternalDocumentSources.
        :type: str
        """

        self._google_drive_enabled = google_drive_enabled

    @property
    def google_drive_metadata(self):
        """
        Gets the google_drive_metadata of this ExternalDocumentSources.

        :return: The google_drive_metadata of this ExternalDocumentSources.
        :rtype: SettingsMetadata
        """
        return self._google_drive_metadata

    @google_drive_metadata.setter
    def google_drive_metadata(self, google_drive_metadata):
        """
        Sets the google_drive_metadata of this ExternalDocumentSources.

        :param google_drive_metadata: The google_drive_metadata of this ExternalDocumentSources.
        :type: SettingsMetadata
        """

        self._google_drive_metadata = google_drive_metadata

    @property
    def one_drive_enabled(self):
        """
        Gets the one_drive_enabled of this ExternalDocumentSources.
        

        :return: The one_drive_enabled of this ExternalDocumentSources.
        :rtype: str
        """
        return self._one_drive_enabled

    @one_drive_enabled.setter
    def one_drive_enabled(self, one_drive_enabled):
        """
        Sets the one_drive_enabled of this ExternalDocumentSources.
        

        :param one_drive_enabled: The one_drive_enabled of this ExternalDocumentSources.
        :type: str
        """

        self._one_drive_enabled = one_drive_enabled

    @property
    def one_drive_metadata(self):
        """
        Gets the one_drive_metadata of this ExternalDocumentSources.

        :return: The one_drive_metadata of this ExternalDocumentSources.
        :rtype: SettingsMetadata
        """
        return self._one_drive_metadata

    @one_drive_metadata.setter
    def one_drive_metadata(self, one_drive_metadata):
        """
        Sets the one_drive_metadata of this ExternalDocumentSources.

        :param one_drive_metadata: The one_drive_metadata of this ExternalDocumentSources.
        :type: SettingsMetadata
        """

        self._one_drive_metadata = one_drive_metadata

    @property
    def salesforce_enabled(self):
        """
        Gets the salesforce_enabled of this ExternalDocumentSources.
        

        :return: The salesforce_enabled of this ExternalDocumentSources.
        :rtype: str
        """
        return self._salesforce_enabled

    @salesforce_enabled.setter
    def salesforce_enabled(self, salesforce_enabled):
        """
        Sets the salesforce_enabled of this ExternalDocumentSources.
        

        :param salesforce_enabled: The salesforce_enabled of this ExternalDocumentSources.
        :type: str
        """

        self._salesforce_enabled = salesforce_enabled

    @property
    def salesforce_metadata(self):
        """
        Gets the salesforce_metadata of this ExternalDocumentSources.

        :return: The salesforce_metadata of this ExternalDocumentSources.
        :rtype: SettingsMetadata
        """
        return self._salesforce_metadata

    @salesforce_metadata.setter
    def salesforce_metadata(self, salesforce_metadata):
        """
        Sets the salesforce_metadata of this ExternalDocumentSources.

        :param salesforce_metadata: The salesforce_metadata of this ExternalDocumentSources.
        :type: SettingsMetadata
        """

        self._salesforce_metadata = salesforce_metadata

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
