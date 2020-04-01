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


class MessagePost(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, role=None, type=None, name=None, email=None, avatar_url=None, metadata=None, payload=None, text=None, media_url=None, media_type=None, items=None, actions=None, block_chat_input=None, display_settings=None, fields=None, destination=None, override=None, coordinates=None, location=None):
        """
        MessagePost - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'role': 'str',
            'type': 'str',
            'name': 'str',
            'email': 'str',
            'avatar_url': 'str',
            'metadata': 'object',
            'payload': 'str',
            'text': 'str',
            'media_url': 'str',
            'media_type': 'str',
            'items': 'list[MessageItem]',
            'actions': 'list[Action]',
            'block_chat_input': 'bool',
            'display_settings': 'DisplaySettings',
            'fields': 'list[FieldPost]',
            'destination': 'Destination',
            'override': 'MessageOverride',
            'coordinates': 'Coordinates',
            'location': 'Location'
        }

        self.attribute_map = {
            'role': 'role',
            'type': 'type',
            'name': 'name',
            'email': 'email',
            'avatar_url': 'avatarUrl',
            'metadata': 'metadata',
            'payload': 'payload',
            'text': 'text',
            'media_url': 'mediaUrl',
            'media_type': 'mediaType',
            'items': 'items',
            'actions': 'actions',
            'block_chat_input': 'blockChatInput',
            'display_settings': 'displaySettings',
            'fields': 'fields',
            'destination': 'destination',
            'override': 'override',
            'coordinates': 'coordinates',
            'location': 'location'
        }

        self._role = None
        self._type = None
        self._name = None
        self._email = None
        self._avatar_url = None
        self._metadata = None
        self._payload = None
        self._text = None
        self._media_url = None
        self._media_type = None
        self._items = None
        self._actions = None
        self._block_chat_input = None
        self._display_settings = None
        self._fields = None
        self._destination = None
        self._override = None
        self._coordinates = None
        self._location = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if role is not None:
          self.role = role
        if type is not None:
          self.type = type
        if name is not None:
          self.name = name
        if email is not None:
          self.email = email
        if avatar_url is not None:
          self.avatar_url = avatar_url
        if metadata is not None:
          self.metadata = metadata
        if payload is not None:
          self.payload = payload
        if text is not None:
          self.text = text
        if media_url is not None:
          self.media_url = media_url
        if media_type is not None:
          self.media_type = media_type
        if items is not None:
          self.items = items
        if actions is not None:
          self.actions = actions
        if block_chat_input is not None:
          self.block_chat_input = block_chat_input
        if display_settings is not None:
          self.display_settings = display_settings
        if fields is not None:
          self.fields = fields
        if destination is not None:
          self.destination = destination
        if override is not None:
          self.override = override
        if coordinates is not None:
          self.coordinates = coordinates
        if location is not None:
          self.location = location

    @property
    def role(self):
        """
        Gets the role of this MessagePost.
        The role of the individual posting the message. See [**RoleEnum**](Enums.md#RoleEnum) for available values.

        :return: The role of this MessagePost.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this MessagePost.
        The role of the individual posting the message. See [**RoleEnum**](Enums.md#RoleEnum) for available values.

        :param role: The role of this MessagePost.
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")

        self._role = role

    @property
    def type(self):
        """
        Gets the type of this MessagePost.
        The message type. See [**MessageTypeEnum**](Enums.md#MessageTypeEnum) for available values.

        :return: The type of this MessagePost.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this MessagePost.
        The message type. See [**MessageTypeEnum**](Enums.md#MessageTypeEnum) for available values.

        :param type: The type of this MessagePost.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def name(self):
        """
        Gets the name of this MessagePost.
        The display name of the message author.

        :return: The name of this MessagePost.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MessagePost.
        The display name of the message author.

        :param name: The name of this MessagePost.
        :type: str
        """

        self._name = name

    @property
    def email(self):
        """
        Gets the email of this MessagePost.
        The email address of the message author.

        :return: The email of this MessagePost.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this MessagePost.
        The email address of the message author.

        :param email: The email of this MessagePost.
        :type: str
        """

        self._email = email

    @property
    def avatar_url(self):
        """
        Gets the avatar_url of this MessagePost.
        The URL of the desired message avatar image.

        :return: The avatar_url of this MessagePost.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """
        Sets the avatar_url of this MessagePost.
        The URL of the desired message avatar image.

        :param avatar_url: The avatar_url of this MessagePost.
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def metadata(self):
        """
        Gets the metadata of this MessagePost.
        Flat JSON object containing any custom properties associated with the message.

        :return: The metadata of this MessagePost.
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this MessagePost.
        Flat JSON object containing any custom properties associated with the message.

        :param metadata: The metadata of this MessagePost.
        :type: object
        """

        self._metadata = metadata

    @property
    def payload(self):
        """
        Gets the payload of this MessagePost.
        The payload of a reply action, if applicable.

        :return: The payload of this MessagePost.
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """
        Sets the payload of this MessagePost.
        The payload of a reply action, if applicable.

        :param payload: The payload of this MessagePost.
        :type: str
        """

        self._payload = payload

    @property
    def text(self):
        """
        Gets the text of this MessagePost.
        The message text. Required for text messages. 

        :return: The text of this MessagePost.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this MessagePost.
        The message text. Required for text messages. 

        :param text: The text of this MessagePost.
        :type: str
        """

        self._text = text

    @property
    def media_url(self):
        """
        Gets the media_url of this MessagePost.
        The mediaUrl for the message. Required for image/file messages. 

        :return: The media_url of this MessagePost.
        :rtype: str
        """
        return self._media_url

    @media_url.setter
    def media_url(self, media_url):
        """
        Sets the media_url of this MessagePost.
        The mediaUrl for the message. Required for image/file messages. 

        :param media_url: The media_url of this MessagePost.
        :type: str
        """

        self._media_url = media_url

    @property
    def media_type(self):
        """
        Gets the media_type of this MessagePost.
        The mediaType for the message. Required for image/file messages. 

        :return: The media_type of this MessagePost.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """
        Sets the media_type of this MessagePost.
        The mediaType for the message. Required for image/file messages. 

        :param media_type: The media_type of this MessagePost.
        :type: str
        """

        self._media_type = media_type

    @property
    def items(self):
        """
        Gets the items of this MessagePost.
        The items in the message list. Required for carousel and list messages. 

        :return: The items of this MessagePost.
        :rtype: list[MessageItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this MessagePost.
        The items in the message list. Required for carousel and list messages. 

        :param items: The items of this MessagePost.
        :type: list[MessageItem]
        """

        self._items = items

    @property
    def actions(self):
        """
        Gets the actions of this MessagePost.
        The actions in the message.

        :return: The actions of this MessagePost.
        :rtype: list[Action]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this MessagePost.
        The actions in the message.

        :param actions: The actions of this MessagePost.
        :type: list[Action]
        """

        self._actions = actions

    @property
    def block_chat_input(self):
        """
        Gets the block_chat_input of this MessagePost.
        Indicates if the Web SDK chat input should be blocked. Defaults to false. Only for form messages. 

        :return: The block_chat_input of this MessagePost.
        :rtype: bool
        """
        return self._block_chat_input

    @block_chat_input.setter
    def block_chat_input(self, block_chat_input):
        """
        Sets the block_chat_input of this MessagePost.
        Indicates if the Web SDK chat input should be blocked. Defaults to false. Only for form messages. 

        :param block_chat_input: The block_chat_input of this MessagePost.
        :type: bool
        """

        self._block_chat_input = block_chat_input

    @property
    def display_settings(self):
        """
        Gets the display_settings of this MessagePost.
        Settings to adjust the carousel layout. See [Display Settings](https://docs.smooch.io/rest/#display-settings).

        :return: The display_settings of this MessagePost.
        :rtype: DisplaySettings
        """
        return self._display_settings

    @display_settings.setter
    def display_settings(self, display_settings):
        """
        Sets the display_settings of this MessagePost.
        Settings to adjust the carousel layout. See [Display Settings](https://docs.smooch.io/rest/#display-settings).

        :param display_settings: The display_settings of this MessagePost.
        :type: DisplaySettings
        """

        self._display_settings = display_settings

    @property
    def fields(self):
        """
        Gets the fields of this MessagePost.
        The fields in the form. Required for form messages. 

        :return: The fields of this MessagePost.
        :rtype: list[FieldPost]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """
        Sets the fields of this MessagePost.
        The fields in the form. Required for form messages. 

        :param fields: The fields of this MessagePost.
        :type: list[FieldPost]
        """

        self._fields = fields

    @property
    def destination(self):
        """
        Gets the destination of this MessagePost.
        Specifies which channel to deliver a message to. See [list integrations](https://docs.smooch.io/rest/#list-integrations) to get integration ID and type.

        :return: The destination of this MessagePost.
        :rtype: Destination
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """
        Sets the destination of this MessagePost.
        Specifies which channel to deliver a message to. See [list integrations](https://docs.smooch.io/rest/#list-integrations) to get integration ID and type.

        :param destination: The destination of this MessagePost.
        :type: Destination
        """

        self._destination = destination

    @property
    def override(self):
        """
        Gets the override of this MessagePost.
        Specifies channel-specific overrides to use in order to bypass Smooch's message translation logic.

        :return: The override of this MessagePost.
        :rtype: MessageOverride
        """
        return self._override

    @override.setter
    def override(self, override):
        """
        Sets the override of this MessagePost.
        Specifies channel-specific overrides to use in order to bypass Smooch's message translation logic.

        :param override: The override of this MessagePost.
        :type: MessageOverride
        """

        self._override = override

    @property
    def coordinates(self):
        """
        Gets the coordinates of this MessagePost.
        Data representing the location being sent in the message.

        :return: The coordinates of this MessagePost.
        :rtype: Coordinates
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """
        Sets the coordinates of this MessagePost.
        Data representing the location being sent in the message.

        :param coordinates: The coordinates of this MessagePost.
        :type: Coordinates
        """

        self._coordinates = coordinates

    @property
    def location(self):
        """
        Gets the location of this MessagePost.
        Additional information about the location being sent in the message.

        :return: The location of this MessagePost.
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this MessagePost.
        Additional information about the location being sent in the message.

        :param location: The location of this MessagePost.
        :type: Location
        """

        self._location = location

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
        if not isinstance(other, MessagePost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
