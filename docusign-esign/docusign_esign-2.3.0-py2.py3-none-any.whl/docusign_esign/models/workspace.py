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


class Workspace(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, billable_account_id=None, created=None, created_by_information=None, last_modified=None, last_modified_by_information=None, status=None, workspace_base_url=None, workspace_description=None, workspace_id=None, workspace_name=None, workspace_uri=None):
        """
        Workspace - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'billable_account_id': 'str',
            'created': 'str',
            'created_by_information': 'WorkspaceUser',
            'last_modified': 'str',
            'last_modified_by_information': 'WorkspaceUser',
            'status': 'str',
            'workspace_base_url': 'str',
            'workspace_description': 'str',
            'workspace_id': 'str',
            'workspace_name': 'str',
            'workspace_uri': 'str'
        }

        self.attribute_map = {
            'billable_account_id': 'billableAccountId',
            'created': 'created',
            'created_by_information': 'createdByInformation',
            'last_modified': 'lastModified',
            'last_modified_by_information': 'lastModifiedByInformation',
            'status': 'status',
            'workspace_base_url': 'workspaceBaseUrl',
            'workspace_description': 'workspaceDescription',
            'workspace_id': 'workspaceId',
            'workspace_name': 'workspaceName',
            'workspace_uri': 'workspaceUri'
        }

        self._billable_account_id = billable_account_id
        self._created = created
        self._created_by_information = created_by_information
        self._last_modified = last_modified
        self._last_modified_by_information = last_modified_by_information
        self._status = status
        self._workspace_base_url = workspace_base_url
        self._workspace_description = workspace_description
        self._workspace_id = workspace_id
        self._workspace_name = workspace_name
        self._workspace_uri = workspace_uri

    @property
    def billable_account_id(self):
        """
        Gets the billable_account_id of this Workspace.
        

        :return: The billable_account_id of this Workspace.
        :rtype: str
        """
        return self._billable_account_id

    @billable_account_id.setter
    def billable_account_id(self, billable_account_id):
        """
        Sets the billable_account_id of this Workspace.
        

        :param billable_account_id: The billable_account_id of this Workspace.
        :type: str
        """

        self._billable_account_id = billable_account_id

    @property
    def created(self):
        """
        Gets the created of this Workspace.
        

        :return: The created of this Workspace.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this Workspace.
        

        :param created: The created of this Workspace.
        :type: str
        """

        self._created = created

    @property
    def created_by_information(self):
        """
        Gets the created_by_information of this Workspace.

        :return: The created_by_information of this Workspace.
        :rtype: WorkspaceUser
        """
        return self._created_by_information

    @created_by_information.setter
    def created_by_information(self, created_by_information):
        """
        Sets the created_by_information of this Workspace.

        :param created_by_information: The created_by_information of this Workspace.
        :type: WorkspaceUser
        """

        self._created_by_information = created_by_information

    @property
    def last_modified(self):
        """
        Gets the last_modified of this Workspace.
        Utc date and time the comment was last updated (can only be done by creator.)

        :return: The last_modified of this Workspace.
        :rtype: str
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """
        Sets the last_modified of this Workspace.
        Utc date and time the comment was last updated (can only be done by creator.)

        :param last_modified: The last_modified of this Workspace.
        :type: str
        """

        self._last_modified = last_modified

    @property
    def last_modified_by_information(self):
        """
        Gets the last_modified_by_information of this Workspace.

        :return: The last_modified_by_information of this Workspace.
        :rtype: WorkspaceUser
        """
        return self._last_modified_by_information

    @last_modified_by_information.setter
    def last_modified_by_information(self, last_modified_by_information):
        """
        Sets the last_modified_by_information of this Workspace.

        :param last_modified_by_information: The last_modified_by_information of this Workspace.
        :type: WorkspaceUser
        """

        self._last_modified_by_information = last_modified_by_information

    @property
    def status(self):
        """
        Gets the status of this Workspace.
        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.

        :return: The status of this Workspace.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Workspace.
        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.

        :param status: The status of this Workspace.
        :type: str
        """

        self._status = status

    @property
    def workspace_base_url(self):
        """
        Gets the workspace_base_url of this Workspace.
        The relative URL that may be used to access the workspace.

        :return: The workspace_base_url of this Workspace.
        :rtype: str
        """
        return self._workspace_base_url

    @workspace_base_url.setter
    def workspace_base_url(self, workspace_base_url):
        """
        Sets the workspace_base_url of this Workspace.
        The relative URL that may be used to access the workspace.

        :param workspace_base_url: The workspace_base_url of this Workspace.
        :type: str
        """

        self._workspace_base_url = workspace_base_url

    @property
    def workspace_description(self):
        """
        Gets the workspace_description of this Workspace.
        Text describing the purpose of the workspace.

        :return: The workspace_description of this Workspace.
        :rtype: str
        """
        return self._workspace_description

    @workspace_description.setter
    def workspace_description(self, workspace_description):
        """
        Sets the workspace_description of this Workspace.
        Text describing the purpose of the workspace.

        :param workspace_description: The workspace_description of this Workspace.
        :type: str
        """

        self._workspace_description = workspace_description

    @property
    def workspace_id(self):
        """
        Gets the workspace_id of this Workspace.
        The id of the workspace, always populated.

        :return: The workspace_id of this Workspace.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """
        Sets the workspace_id of this Workspace.
        The id of the workspace, always populated.

        :param workspace_id: The workspace_id of this Workspace.
        :type: str
        """

        self._workspace_id = workspace_id

    @property
    def workspace_name(self):
        """
        Gets the workspace_name of this Workspace.
        The name of the workspace.

        :return: The workspace_name of this Workspace.
        :rtype: str
        """
        return self._workspace_name

    @workspace_name.setter
    def workspace_name(self, workspace_name):
        """
        Sets the workspace_name of this Workspace.
        The name of the workspace.

        :param workspace_name: The workspace_name of this Workspace.
        :type: str
        """

        self._workspace_name = workspace_name

    @property
    def workspace_uri(self):
        """
        Gets the workspace_uri of this Workspace.
        The relative URI that may be used to access the workspace.

        :return: The workspace_uri of this Workspace.
        :rtype: str
        """
        return self._workspace_uri

    @workspace_uri.setter
    def workspace_uri(self, workspace_uri):
        """
        Sets the workspace_uri of this Workspace.
        The relative URI that may be used to access the workspace.

        :param workspace_uri: The workspace_uri of this Workspace.
        :type: str
        """

        self._workspace_uri = workspace_uri

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
