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


class EnvelopeTemplateDefinition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, created=None, description=None, folder_id=None, folder_name=None, folder_uri=None, last_modified=None, last_modified_by=None, name=None, new_password=None, owner=None, page_count=None, parent_folder_uri=None, password=None, shared=None, template_id=None, uri=None):
        """
        EnvelopeTemplateDefinition - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'created': 'str',
            'description': 'str',
            'folder_id': 'str',
            'folder_name': 'str',
            'folder_uri': 'str',
            'last_modified': 'str',
            'last_modified_by': 'UserInfo',
            'name': 'str',
            'new_password': 'str',
            'owner': 'UserInfo',
            'page_count': 'int',
            'parent_folder_uri': 'str',
            'password': 'str',
            'shared': 'str',
            'template_id': 'str',
            'uri': 'str'
        }

        self.attribute_map = {
            'created': 'created',
            'description': 'description',
            'folder_id': 'folderId',
            'folder_name': 'folderName',
            'folder_uri': 'folderUri',
            'last_modified': 'lastModified',
            'last_modified_by': 'lastModifiedBy',
            'name': 'name',
            'new_password': 'newPassword',
            'owner': 'owner',
            'page_count': 'pageCount',
            'parent_folder_uri': 'parentFolderUri',
            'password': 'password',
            'shared': 'shared',
            'template_id': 'templateId',
            'uri': 'uri'
        }

        self._created = created
        self._description = description
        self._folder_id = folder_id
        self._folder_name = folder_name
        self._folder_uri = folder_uri
        self._last_modified = last_modified
        self._last_modified_by = last_modified_by
        self._name = name
        self._new_password = new_password
        self._owner = owner
        self._page_count = page_count
        self._parent_folder_uri = parent_folder_uri
        self._password = password
        self._shared = shared
        self._template_id = template_id
        self._uri = uri

    @property
    def created(self):
        """
        Gets the created of this EnvelopeTemplateDefinition.
        

        :return: The created of this EnvelopeTemplateDefinition.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this EnvelopeTemplateDefinition.
        

        :param created: The created of this EnvelopeTemplateDefinition.
        :type: str
        """

        self._created = created

    @property
    def description(self):
        """
        Gets the description of this EnvelopeTemplateDefinition.
        

        :return: The description of this EnvelopeTemplateDefinition.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this EnvelopeTemplateDefinition.
        

        :param description: The description of this EnvelopeTemplateDefinition.
        :type: str
        """

        self._description = description

    @property
    def folder_id(self):
        """
        Gets the folder_id of this EnvelopeTemplateDefinition.
        The ID for the folder.

        :return: The folder_id of this EnvelopeTemplateDefinition.
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """
        Sets the folder_id of this EnvelopeTemplateDefinition.
        The ID for the folder.

        :param folder_id: The folder_id of this EnvelopeTemplateDefinition.
        :type: str
        """

        self._folder_id = folder_id

    @property
    def folder_name(self):
        """
        Gets the folder_name of this EnvelopeTemplateDefinition.
         The name of the folder in which the template is located.

        :return: The folder_name of this EnvelopeTemplateDefinition.
        :rtype: str
        """
        return self._folder_name

    @folder_name.setter
    def folder_name(self, folder_name):
        """
        Sets the folder_name of this EnvelopeTemplateDefinition.
         The name of the folder in which the template is located.

        :param folder_name: The folder_name of this EnvelopeTemplateDefinition.
        :type: str
        """

        self._folder_name = folder_name

    @property
    def folder_uri(self):
        """
        Gets the folder_uri of this EnvelopeTemplateDefinition.
        The URI of the folder.

        :return: The folder_uri of this EnvelopeTemplateDefinition.
        :rtype: str
        """
        return self._folder_uri

    @folder_uri.setter
    def folder_uri(self, folder_uri):
        """
        Sets the folder_uri of this EnvelopeTemplateDefinition.
        The URI of the folder.

        :param folder_uri: The folder_uri of this EnvelopeTemplateDefinition.
        :type: str
        """

        self._folder_uri = folder_uri

    @property
    def last_modified(self):
        """
        Gets the last_modified of this EnvelopeTemplateDefinition.
        

        :return: The last_modified of this EnvelopeTemplateDefinition.
        :rtype: str
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """
        Sets the last_modified of this EnvelopeTemplateDefinition.
        

        :param last_modified: The last_modified of this EnvelopeTemplateDefinition.
        :type: str
        """

        self._last_modified = last_modified

    @property
    def last_modified_by(self):
        """
        Gets the last_modified_by of this EnvelopeTemplateDefinition.

        :return: The last_modified_by of this EnvelopeTemplateDefinition.
        :rtype: UserInfo
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """
        Sets the last_modified_by of this EnvelopeTemplateDefinition.

        :param last_modified_by: The last_modified_by of this EnvelopeTemplateDefinition.
        :type: UserInfo
        """

        self._last_modified_by = last_modified_by

    @property
    def name(self):
        """
        Gets the name of this EnvelopeTemplateDefinition.
        

        :return: The name of this EnvelopeTemplateDefinition.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this EnvelopeTemplateDefinition.
        

        :param name: The name of this EnvelopeTemplateDefinition.
        :type: str
        """

        self._name = name

    @property
    def new_password(self):
        """
        Gets the new_password of this EnvelopeTemplateDefinition.
        

        :return: The new_password of this EnvelopeTemplateDefinition.
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        """
        Sets the new_password of this EnvelopeTemplateDefinition.
        

        :param new_password: The new_password of this EnvelopeTemplateDefinition.
        :type: str
        """

        self._new_password = new_password

    @property
    def owner(self):
        """
        Gets the owner of this EnvelopeTemplateDefinition.

        :return: The owner of this EnvelopeTemplateDefinition.
        :rtype: UserInfo
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this EnvelopeTemplateDefinition.

        :param owner: The owner of this EnvelopeTemplateDefinition.
        :type: UserInfo
        """

        self._owner = owner

    @property
    def page_count(self):
        """
        Gets the page_count of this EnvelopeTemplateDefinition.
        An integer value specifying the number of document pages in the template. Omit this property if not submitting a page count.

        :return: The page_count of this EnvelopeTemplateDefinition.
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """
        Sets the page_count of this EnvelopeTemplateDefinition.
        An integer value specifying the number of document pages in the template. Omit this property if not submitting a page count.

        :param page_count: The page_count of this EnvelopeTemplateDefinition.
        :type: int
        """

        self._page_count = page_count

    @property
    def parent_folder_uri(self):
        """
        Gets the parent_folder_uri of this EnvelopeTemplateDefinition.
        

        :return: The parent_folder_uri of this EnvelopeTemplateDefinition.
        :rtype: str
        """
        return self._parent_folder_uri

    @parent_folder_uri.setter
    def parent_folder_uri(self, parent_folder_uri):
        """
        Sets the parent_folder_uri of this EnvelopeTemplateDefinition.
        

        :param parent_folder_uri: The parent_folder_uri of this EnvelopeTemplateDefinition.
        :type: str
        """

        self._parent_folder_uri = parent_folder_uri

    @property
    def password(self):
        """
        Gets the password of this EnvelopeTemplateDefinition.
        

        :return: The password of this EnvelopeTemplateDefinition.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this EnvelopeTemplateDefinition.
        

        :param password: The password of this EnvelopeTemplateDefinition.
        :type: str
        """

        self._password = password

    @property
    def shared(self):
        """
        Gets the shared of this EnvelopeTemplateDefinition.
        When set to **true**, this custom tab is shared.

        :return: The shared of this EnvelopeTemplateDefinition.
        :rtype: str
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """
        Sets the shared of this EnvelopeTemplateDefinition.
        When set to **true**, this custom tab is shared.

        :param shared: The shared of this EnvelopeTemplateDefinition.
        :type: str
        """

        self._shared = shared

    @property
    def template_id(self):
        """
        Gets the template_id of this EnvelopeTemplateDefinition.
        The unique identifier of the template. If this is not provided, DocuSign will generate a value. 

        :return: The template_id of this EnvelopeTemplateDefinition.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """
        Sets the template_id of this EnvelopeTemplateDefinition.
        The unique identifier of the template. If this is not provided, DocuSign will generate a value. 

        :param template_id: The template_id of this EnvelopeTemplateDefinition.
        :type: str
        """

        self._template_id = template_id

    @property
    def uri(self):
        """
        Gets the uri of this EnvelopeTemplateDefinition.
        

        :return: The uri of this EnvelopeTemplateDefinition.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this EnvelopeTemplateDefinition.
        

        :param uri: The uri of this EnvelopeTemplateDefinition.
        :type: str
        """

        self._uri = uri

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
