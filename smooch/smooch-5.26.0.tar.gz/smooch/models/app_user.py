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


class AppUser(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, user_id=None, given_name=None, surname=None, email=None, signed_up_at=None, properties=None, conversation_started=None, clients=None, pending_clients=None):
        """
        AppUser - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'user_id': 'str',
            'given_name': 'str',
            'surname': 'str',
            'email': 'str',
            'signed_up_at': 'str',
            'properties': 'object',
            'conversation_started': 'bool',
            'clients': 'list[Client]',
            'pending_clients': 'list[Client]'
        }

        self.attribute_map = {
            'id': '_id',
            'user_id': 'userId',
            'given_name': 'givenName',
            'surname': 'surname',
            'email': 'email',
            'signed_up_at': 'signedUpAt',
            'properties': 'properties',
            'conversation_started': 'conversationStarted',
            'clients': 'clients',
            'pending_clients': 'pendingClients'
        }

        self._id = None
        self._user_id = None
        self._given_name = None
        self._surname = None
        self._email = None
        self._signed_up_at = None
        self._properties = None
        self._conversation_started = None
        self._clients = None
        self._pending_clients = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if id is not None:
          self.id = id
        if user_id is not None:
          self.user_id = user_id
        if given_name is not None:
          self.given_name = given_name
        if surname is not None:
          self.surname = surname
        if email is not None:
          self.email = email
        if signed_up_at is not None:
          self.signed_up_at = signed_up_at
        if properties is not None:
          self.properties = properties
        if conversation_started is not None:
          self.conversation_started = conversation_started
        if clients is not None:
          self.clients = clients
        if pending_clients is not None:
          self.pending_clients = pending_clients

    @property
    def id(self):
        """
        Gets the id of this AppUser.
        The app user's ID, generated automatically.

        :return: The id of this AppUser.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AppUser.
        The app user's ID, generated automatically.

        :param id: The id of this AppUser.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def user_id(self):
        """
        Gets the user_id of this AppUser.
        The app user's userId. This ID is specified by the appMaker. 

        :return: The user_id of this AppUser.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this AppUser.
        The app user's userId. This ID is specified by the appMaker. 

        :param user_id: The user_id of this AppUser.
        :type: str
        """

        self._user_id = user_id

    @property
    def given_name(self):
        """
        Gets the given_name of this AppUser.
        The app user's given name.

        :return: The given_name of this AppUser.
        :rtype: str
        """
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        """
        Sets the given_name of this AppUser.
        The app user's given name.

        :param given_name: The given_name of this AppUser.
        :type: str
        """

        self._given_name = given_name

    @property
    def surname(self):
        """
        Gets the surname of this AppUser.
        The app user's surname.

        :return: The surname of this AppUser.
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        """
        Sets the surname of this AppUser.
        The app user's surname.

        :param surname: The surname of this AppUser.
        :type: str
        """

        self._surname = surname

    @property
    def email(self):
        """
        Gets the email of this AppUser.
        The app user's email.

        :return: The email of this AppUser.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this AppUser.
        The app user's email.

        :param email: The email of this AppUser.
        :type: str
        """

        self._email = email

    @property
    def signed_up_at(self):
        """
        Gets the signed_up_at of this AppUser.
        A datetime string with the format *yyyy-mm-ddThh:mm:ssZ* representing the moment an appUser was created.

        :return: The signed_up_at of this AppUser.
        :rtype: str
        """
        return self._signed_up_at

    @signed_up_at.setter
    def signed_up_at(self, signed_up_at):
        """
        Sets the signed_up_at of this AppUser.
        A datetime string with the format *yyyy-mm-ddThh:mm:ssZ* representing the moment an appUser was created.

        :param signed_up_at: The signed_up_at of this AppUser.
        :type: str
        """

        self._signed_up_at = signed_up_at

    @property
    def properties(self):
        """
        Gets the properties of this AppUser.
        Custom properties for the app user.

        :return: The properties of this AppUser.
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this AppUser.
        Custom properties for the app user.

        :param properties: The properties of this AppUser.
        :type: object
        """
        if properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")

        self._properties = properties

    @property
    def conversation_started(self):
        """
        Gets the conversation_started of this AppUser.
        Flag indicating if the conversation has started for the app user.

        :return: The conversation_started of this AppUser.
        :rtype: bool
        """
        return self._conversation_started

    @conversation_started.setter
    def conversation_started(self, conversation_started):
        """
        Sets the conversation_started of this AppUser.
        Flag indicating if the conversation has started for the app user.

        :param conversation_started: The conversation_started of this AppUser.
        :type: bool
        """
        if conversation_started is None:
            raise ValueError("Invalid value for `conversation_started`, must not be `None`")

        self._conversation_started = conversation_started

    @property
    def clients(self):
        """
        Gets the clients of this AppUser.
        List of clients associated with the app user.

        :return: The clients of this AppUser.
        :rtype: list[Client]
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """
        Sets the clients of this AppUser.
        List of clients associated with the app user.

        :param clients: The clients of this AppUser.
        :type: list[Client]
        """

        self._clients = clients

    @property
    def pending_clients(self):
        """
        Gets the pending_clients of this AppUser.
        As clients, but containing linked clients which have not been confirmed yet (i.e. Twilio SMS).

        :return: The pending_clients of this AppUser.
        :rtype: list[Client]
        """
        return self._pending_clients

    @pending_clients.setter
    def pending_clients(self, pending_clients):
        """
        Sets the pending_clients of this AppUser.
        As clients, but containing linked clients which have not been confirmed yet (i.e. Twilio SMS).

        :param pending_clients: The pending_clients of this AppUser.
        :type: list[Client]
        """

        self._pending_clients = pending_clients

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
        if not isinstance(other, AppUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
