# coding: utf-8

"""
    Smooch

    The Smooch API is a unified interface for powering messaging in your customer experiences across every channel. Our API speeds access to new markets, reduces time to ship, eliminates complexity, and helps you build the best experiences for your customers. For more information, visit our [official documentation](https://docs.smooch.io).

    OpenAPI spec version: 5.25
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ChannelEntityItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, type=None, integration_id=None, phone_number=None, user_id=None, address=None, username=None, chat_id=None):
        """
        ChannelEntityItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'integration_id': 'str',
            'phone_number': 'str',
            'user_id': 'str',
            'address': 'str',
            'username': 'str',
            'chat_id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'integration_id': 'integrationId',
            'phone_number': 'phoneNumber',
            'user_id': 'userId',
            'address': 'address',
            'username': 'username',
            'chat_id': 'chatId'
        }

        self._type = None
        self._integration_id = None
        self._phone_number = None
        self._user_id = None
        self._address = None
        self._username = None
        self._chat_id = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if type is not None:
          self.type = type
        if integration_id is not None:
          self.integration_id = integration_id
        if phone_number is not None:
          self.phone_number = phone_number
        if user_id is not None:
          self.user_id = user_id
        if address is not None:
          self.address = address
        if username is not None:
          self.username = username
        if chat_id is not None:
          self.chat_id = chat_id

    @property
    def type(self):
        """
        Gets the type of this ChannelEntityItem.
        The type of channel. See [**IntegrationTypeEnum**](Enums.md#IntegrationTypeEnum) for available values.

        :return: The type of this ChannelEntityItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ChannelEntityItem.
        The type of channel. See [**IntegrationTypeEnum**](Enums.md#IntegrationTypeEnum) for available values.

        :param type: The type of this ChannelEntityItem.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def integration_id(self):
        """
        Gets the integration_id of this ChannelEntityItem.
        The ID of the integration.

        :return: The integration_id of this ChannelEntityItem.
        :rtype: str
        """
        return self._integration_id

    @integration_id.setter
    def integration_id(self, integration_id):
        """
        Sets the integration_id of this ChannelEntityItem.
        The ID of the integration.

        :param integration_id: The integration_id of this ChannelEntityItem.
        :type: str
        """

        self._integration_id = integration_id

    @property
    def phone_number(self):
        """
        Gets the phone_number of this ChannelEntityItem.
        The phone number for a *twilio* or *messagebird* integration

        :return: The phone_number of this ChannelEntityItem.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this ChannelEntityItem.
        The phone number for a *twilio* or *messagebird* integration

        :param phone_number: The phone_number of this ChannelEntityItem.
        :type: str
        """

        self._phone_number = phone_number

    @property
    def user_id(self):
        """
        Gets the user_id of this ChannelEntityItem.
        The userId for a *messenger*, *viber*, *line*, *wechat* or *twitter* integration

        :return: The user_id of this ChannelEntityItem.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this ChannelEntityItem.
        The userId for a *messenger*, *viber*, *line*, *wechat* or *twitter* integration

        :param user_id: The user_id of this ChannelEntityItem.
        :type: str
        """

        self._user_id = user_id

    @property
    def address(self):
        """
        Gets the address of this ChannelEntityItem.
        The email address for a *mailgun* integration

        :return: The address of this ChannelEntityItem.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this ChannelEntityItem.
        The email address for a *mailgun* integration

        :param address: The address of this ChannelEntityItem.
        :type: str
        """

        self._address = address

    @property
    def username(self):
        """
        Gets the username of this ChannelEntityItem.
        The username for a *whatsapp* integration

        :return: The username of this ChannelEntityItem.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this ChannelEntityItem.
        The username for a *whatsapp* integration

        :param username: The username of this ChannelEntityItem.
        :type: str
        """

        self._username = username

    @property
    def chat_id(self):
        """
        Gets the chat_id of this ChannelEntityItem.
        The chat id for a *telegram* integration

        :return: The chat_id of this ChannelEntityItem.
        :rtype: str
        """
        return self._chat_id

    @chat_id.setter
    def chat_id(self, chat_id):
        """
        Sets the chat_id of this ChannelEntityItem.
        The chat id for a *telegram* integration

        :param chat_id: The chat_id of this ChannelEntityItem.
        :type: str
        """

        self._chat_id = chat_id

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
        if not isinstance(other, ChannelEntityItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
