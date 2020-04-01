# coding: utf-8

"""
    Toshl

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Bankconnection(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'institution': 'str',
        'url': 'str',
        'provider': 'str',
        'logo': 'str',
        'name': 'str',
        '_from': 'str',
        'accounts': 'list[str]',
        'refreshed': 'str',
        'auto_refresh': 'bool',
        'can_refresh': 'bool',
        'review': 'int',
        'status': 'str',
        'deleted': 'bool',
        'reminder': 'bool',
        'regulated': 'bool',
        'partner': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'institution': 'institution',
        'url': 'url',
        'provider': 'provider',
        'logo': 'logo',
        'name': 'name',
        '_from': 'from',
        'accounts': 'accounts',
        'refreshed': 'refreshed',
        'auto_refresh': 'auto_refresh',
        'can_refresh': 'can_refresh',
        'review': 'review',
        'status': 'status',
        'deleted': 'deleted',
        'reminder': 'reminder',
        'regulated': 'regulated',
        'partner': 'partner'
    }

    def __init__(self, id=None, institution=None, url=None, provider=None, logo=None, name=None, _from=None, accounts=None, refreshed=None, auto_refresh=None, can_refresh=None, review=None, status=None, deleted=None, reminder=None, regulated=None, partner=None):  # noqa: E501
        """Bankconnection - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._institution = None
        self._url = None
        self._provider = None
        self._logo = None
        self._name = None
        self.__from = None
        self._accounts = None
        self._refreshed = None
        self._auto_refresh = None
        self._can_refresh = None
        self._review = None
        self._status = None
        self._deleted = None
        self._reminder = None
        self._regulated = None
        self._partner = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if institution is not None:
            self.institution = institution
        if url is not None:
            self.url = url
        if provider is not None:
            self.provider = provider
        if logo is not None:
            self.logo = logo
        if name is not None:
            self.name = name
        if _from is not None:
            self._from = _from
        if accounts is not None:
            self.accounts = accounts
        if refreshed is not None:
            self.refreshed = refreshed
        if auto_refresh is not None:
            self.auto_refresh = auto_refresh
        if can_refresh is not None:
            self.can_refresh = can_refresh
        if review is not None:
            self.review = review
        if status is not None:
            self.status = status
        if deleted is not None:
            self.deleted = deleted
        if reminder is not None:
            self.reminder = reminder
        if regulated is not None:
            self.regulated = regulated
        if partner is not None:
            self.partner = partner

    @property
    def id(self):
        """Gets the id of this Bankconnection.  # noqa: E501


        :return: The id of this Bankconnection.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Bankconnection.


        :param id: The id of this Bankconnection.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def institution(self):
        """Gets the institution of this Bankconnection.  # noqa: E501


        :return: The institution of this Bankconnection.  # noqa: E501
        :rtype: str
        """
        return self._institution

    @institution.setter
    def institution(self, institution):
        """Sets the institution of this Bankconnection.


        :param institution: The institution of this Bankconnection.  # noqa: E501
        :type: str
        """

        self._institution = institution

    @property
    def url(self):
        """Gets the url of this Bankconnection.  # noqa: E501


        :return: The url of this Bankconnection.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Bankconnection.


        :param url: The url of this Bankconnection.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def provider(self):
        """Gets the provider of this Bankconnection.  # noqa: E501


        :return: The provider of this Bankconnection.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this Bankconnection.


        :param provider: The provider of this Bankconnection.  # noqa: E501
        :type: str
        """

        self._provider = provider

    @property
    def logo(self):
        """Gets the logo of this Bankconnection.  # noqa: E501


        :return: The logo of this Bankconnection.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this Bankconnection.


        :param logo: The logo of this Bankconnection.  # noqa: E501
        :type: str
        """

        self._logo = logo

    @property
    def name(self):
        """Gets the name of this Bankconnection.  # noqa: E501


        :return: The name of this Bankconnection.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Bankconnection.


        :param name: The name of this Bankconnection.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def _from(self):
        """Gets the _from of this Bankconnection.  # noqa: E501


        :return: The _from of this Bankconnection.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this Bankconnection.


        :param _from: The _from of this Bankconnection.  # noqa: E501
        :type: str
        """

        self.__from = _from

    @property
    def accounts(self):
        """Gets the accounts of this Bankconnection.  # noqa: E501


        :return: The accounts of this Bankconnection.  # noqa: E501
        :rtype: list[str]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this Bankconnection.


        :param accounts: The accounts of this Bankconnection.  # noqa: E501
        :type: list[str]
        """

        self._accounts = accounts

    @property
    def refreshed(self):
        """Gets the refreshed of this Bankconnection.  # noqa: E501


        :return: The refreshed of this Bankconnection.  # noqa: E501
        :rtype: str
        """
        return self._refreshed

    @refreshed.setter
    def refreshed(self, refreshed):
        """Sets the refreshed of this Bankconnection.


        :param refreshed: The refreshed of this Bankconnection.  # noqa: E501
        :type: str
        """

        self._refreshed = refreshed

    @property
    def auto_refresh(self):
        """Gets the auto_refresh of this Bankconnection.  # noqa: E501


        :return: The auto_refresh of this Bankconnection.  # noqa: E501
        :rtype: bool
        """
        return self._auto_refresh

    @auto_refresh.setter
    def auto_refresh(self, auto_refresh):
        """Sets the auto_refresh of this Bankconnection.


        :param auto_refresh: The auto_refresh of this Bankconnection.  # noqa: E501
        :type: bool
        """

        self._auto_refresh = auto_refresh

    @property
    def can_refresh(self):
        """Gets the can_refresh of this Bankconnection.  # noqa: E501


        :return: The can_refresh of this Bankconnection.  # noqa: E501
        :rtype: bool
        """
        return self._can_refresh

    @can_refresh.setter
    def can_refresh(self, can_refresh):
        """Sets the can_refresh of this Bankconnection.


        :param can_refresh: The can_refresh of this Bankconnection.  # noqa: E501
        :type: bool
        """

        self._can_refresh = can_refresh

    @property
    def review(self):
        """Gets the review of this Bankconnection.  # noqa: E501


        :return: The review of this Bankconnection.  # noqa: E501
        :rtype: int
        """
        return self._review

    @review.setter
    def review(self, review):
        """Sets the review of this Bankconnection.


        :param review: The review of this Bankconnection.  # noqa: E501
        :type: int
        """

        self._review = review

    @property
    def status(self):
        """Gets the status of this Bankconnection.  # noqa: E501


        :return: The status of this Bankconnection.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Bankconnection.


        :param status: The status of this Bankconnection.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def deleted(self):
        """Gets the deleted of this Bankconnection.  # noqa: E501


        :return: The deleted of this Bankconnection.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Bankconnection.


        :param deleted: The deleted of this Bankconnection.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def reminder(self):
        """Gets the reminder of this Bankconnection.  # noqa: E501


        :return: The reminder of this Bankconnection.  # noqa: E501
        :rtype: bool
        """
        return self._reminder

    @reminder.setter
    def reminder(self, reminder):
        """Sets the reminder of this Bankconnection.


        :param reminder: The reminder of this Bankconnection.  # noqa: E501
        :type: bool
        """

        self._reminder = reminder

    @property
    def regulated(self):
        """Gets the regulated of this Bankconnection.  # noqa: E501


        :return: The regulated of this Bankconnection.  # noqa: E501
        :rtype: bool
        """
        return self._regulated

    @regulated.setter
    def regulated(self, regulated):
        """Sets the regulated of this Bankconnection.


        :param regulated: The regulated of this Bankconnection.  # noqa: E501
        :type: bool
        """

        self._regulated = regulated

    @property
    def partner(self):
        """Gets the partner of this Bankconnection.  # noqa: E501


        :return: The partner of this Bankconnection.  # noqa: E501
        :rtype: bool
        """
        return self._partner

    @partner.setter
    def partner(self, partner):
        """Sets the partner of this Bankconnection.


        :param partner: The partner of this Bankconnection.  # noqa: E501
        :type: bool
        """

        self._partner = partner

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Bankconnection, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Bankconnection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
