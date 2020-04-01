# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re
import json

from ..utils import sanitize_for_serialization

class QueueConversationVideoEventTopicParticipant(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        QueueConversationVideoEventTopicParticipant - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'connected_time': 'datetime',
            'end_time': 'datetime',
            'user_id': 'str',
            'external_contact_id': 'str',
            'external_organization_id': 'str',
            'name': 'str',
            'queue_id': 'str',
            'group_id': 'str',
            'team_id': 'str',
            'purpose': 'str',
            'consult_participant_id': 'str',
            'address': 'str',
            'wrapup_required': 'bool',
            'wrapup_expected': 'bool',
            'wrapup_prompt': 'str',
            'wrapup_timeout_ms': 'int',
            'wrapup': 'QueueConversationVideoEventTopicWrapup',
            'start_acw_time': 'datetime',
            'end_acw_time': 'datetime',
            'conversation_routing_data': 'QueueConversationVideoEventTopicConversationRoutingData',
            'alerting_timeout_ms': 'int',
            'monitored_participant_id': 'str',
            'screen_recording_state': 'str',
            'flagged_reason': 'str',
            'attributes': 'dict(str, str)',
            'calls': 'list[QueueConversationVideoEventTopicCall]',
            'callbacks': 'list[QueueConversationVideoEventTopicCallback]',
            'chats': 'list[QueueConversationVideoEventTopicChat]',
            'cobrowsesessions': 'list[QueueConversationVideoEventTopicCobrowse]',
            'emails': 'list[QueueConversationVideoEventTopicEmail]',
            'messages': 'list[QueueConversationVideoEventTopicMessage]',
            'screenshares': 'list[QueueConversationVideoEventTopicScreenshare]',
            'social_expressions': 'list[QueueConversationVideoEventTopicSocialExpression]',
            'videos': 'list[QueueConversationVideoEventTopicVideo]',
            'additional_properties': 'object'
        }

        self.attribute_map = {
            'id': 'id',
            'connected_time': 'connectedTime',
            'end_time': 'endTime',
            'user_id': 'userId',
            'external_contact_id': 'externalContactId',
            'external_organization_id': 'externalOrganizationId',
            'name': 'name',
            'queue_id': 'queueId',
            'group_id': 'groupId',
            'team_id': 'teamId',
            'purpose': 'purpose',
            'consult_participant_id': 'consultParticipantId',
            'address': 'address',
            'wrapup_required': 'wrapupRequired',
            'wrapup_expected': 'wrapupExpected',
            'wrapup_prompt': 'wrapupPrompt',
            'wrapup_timeout_ms': 'wrapupTimeoutMs',
            'wrapup': 'wrapup',
            'start_acw_time': 'startAcwTime',
            'end_acw_time': 'endAcwTime',
            'conversation_routing_data': 'conversationRoutingData',
            'alerting_timeout_ms': 'alertingTimeoutMs',
            'monitored_participant_id': 'monitoredParticipantId',
            'screen_recording_state': 'screenRecordingState',
            'flagged_reason': 'flaggedReason',
            'attributes': 'attributes',
            'calls': 'calls',
            'callbacks': 'callbacks',
            'chats': 'chats',
            'cobrowsesessions': 'cobrowsesessions',
            'emails': 'emails',
            'messages': 'messages',
            'screenshares': 'screenshares',
            'social_expressions': 'socialExpressions',
            'videos': 'videos',
            'additional_properties': 'additionalProperties'
        }

        self._id = None
        self._connected_time = None
        self._end_time = None
        self._user_id = None
        self._external_contact_id = None
        self._external_organization_id = None
        self._name = None
        self._queue_id = None
        self._group_id = None
        self._team_id = None
        self._purpose = None
        self._consult_participant_id = None
        self._address = None
        self._wrapup_required = None
        self._wrapup_expected = None
        self._wrapup_prompt = None
        self._wrapup_timeout_ms = None
        self._wrapup = None
        self._start_acw_time = None
        self._end_acw_time = None
        self._conversation_routing_data = None
        self._alerting_timeout_ms = None
        self._monitored_participant_id = None
        self._screen_recording_state = None
        self._flagged_reason = None
        self._attributes = None
        self._calls = None
        self._callbacks = None
        self._chats = None
        self._cobrowsesessions = None
        self._emails = None
        self._messages = None
        self._screenshares = None
        self._social_expressions = None
        self._videos = None
        self._additional_properties = None

    @property
    def id(self):
        """
        Gets the id of this QueueConversationVideoEventTopicParticipant.


        :return: The id of this QueueConversationVideoEventTopicParticipant.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this QueueConversationVideoEventTopicParticipant.


        :param id: The id of this QueueConversationVideoEventTopicParticipant.
        :type: str
        """
        
        self._id = id

    @property
    def connected_time(self):
        """
        Gets the connected_time of this QueueConversationVideoEventTopicParticipant.


        :return: The connected_time of this QueueConversationVideoEventTopicParticipant.
        :rtype: datetime
        """
        return self._connected_time

    @connected_time.setter
    def connected_time(self, connected_time):
        """
        Sets the connected_time of this QueueConversationVideoEventTopicParticipant.


        :param connected_time: The connected_time of this QueueConversationVideoEventTopicParticipant.
        :type: datetime
        """
        
        self._connected_time = connected_time

    @property
    def end_time(self):
        """
        Gets the end_time of this QueueConversationVideoEventTopicParticipant.


        :return: The end_time of this QueueConversationVideoEventTopicParticipant.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this QueueConversationVideoEventTopicParticipant.


        :param end_time: The end_time of this QueueConversationVideoEventTopicParticipant.
        :type: datetime
        """
        
        self._end_time = end_time

    @property
    def user_id(self):
        """
        Gets the user_id of this QueueConversationVideoEventTopicParticipant.


        :return: The user_id of this QueueConversationVideoEventTopicParticipant.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this QueueConversationVideoEventTopicParticipant.


        :param user_id: The user_id of this QueueConversationVideoEventTopicParticipant.
        :type: str
        """
        
        self._user_id = user_id

    @property
    def external_contact_id(self):
        """
        Gets the external_contact_id of this QueueConversationVideoEventTopicParticipant.


        :return: The external_contact_id of this QueueConversationVideoEventTopicParticipant.
        :rtype: str
        """
        return self._external_contact_id

    @external_contact_id.setter
    def external_contact_id(self, external_contact_id):
        """
        Sets the external_contact_id of this QueueConversationVideoEventTopicParticipant.


        :param external_contact_id: The external_contact_id of this QueueConversationVideoEventTopicParticipant.
        :type: str
        """
        
        self._external_contact_id = external_contact_id

    @property
    def external_organization_id(self):
        """
        Gets the external_organization_id of this QueueConversationVideoEventTopicParticipant.


        :return: The external_organization_id of this QueueConversationVideoEventTopicParticipant.
        :rtype: str
        """
        return self._external_organization_id

    @external_organization_id.setter
    def external_organization_id(self, external_organization_id):
        """
        Sets the external_organization_id of this QueueConversationVideoEventTopicParticipant.


        :param external_organization_id: The external_organization_id of this QueueConversationVideoEventTopicParticipant.
        :type: str
        """
        
        self._external_organization_id = external_organization_id

    @property
    def name(self):
        """
        Gets the name of this QueueConversationVideoEventTopicParticipant.


        :return: The name of this QueueConversationVideoEventTopicParticipant.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this QueueConversationVideoEventTopicParticipant.


        :param name: The name of this QueueConversationVideoEventTopicParticipant.
        :type: str
        """
        
        self._name = name

    @property
    def queue_id(self):
        """
        Gets the queue_id of this QueueConversationVideoEventTopicParticipant.


        :return: The queue_id of this QueueConversationVideoEventTopicParticipant.
        :rtype: str
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id):
        """
        Sets the queue_id of this QueueConversationVideoEventTopicParticipant.


        :param queue_id: The queue_id of this QueueConversationVideoEventTopicParticipant.
        :type: str
        """
        
        self._queue_id = queue_id

    @property
    def group_id(self):
        """
        Gets the group_id of this QueueConversationVideoEventTopicParticipant.


        :return: The group_id of this QueueConversationVideoEventTopicParticipant.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this QueueConversationVideoEventTopicParticipant.


        :param group_id: The group_id of this QueueConversationVideoEventTopicParticipant.
        :type: str
        """
        
        self._group_id = group_id

    @property
    def team_id(self):
        """
        Gets the team_id of this QueueConversationVideoEventTopicParticipant.


        :return: The team_id of this QueueConversationVideoEventTopicParticipant.
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """
        Sets the team_id of this QueueConversationVideoEventTopicParticipant.


        :param team_id: The team_id of this QueueConversationVideoEventTopicParticipant.
        :type: str
        """
        
        self._team_id = team_id

    @property
    def purpose(self):
        """
        Gets the purpose of this QueueConversationVideoEventTopicParticipant.


        :return: The purpose of this QueueConversationVideoEventTopicParticipant.
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """
        Sets the purpose of this QueueConversationVideoEventTopicParticipant.


        :param purpose: The purpose of this QueueConversationVideoEventTopicParticipant.
        :type: str
        """
        
        self._purpose = purpose

    @property
    def consult_participant_id(self):
        """
        Gets the consult_participant_id of this QueueConversationVideoEventTopicParticipant.


        :return: The consult_participant_id of this QueueConversationVideoEventTopicParticipant.
        :rtype: str
        """
        return self._consult_participant_id

    @consult_participant_id.setter
    def consult_participant_id(self, consult_participant_id):
        """
        Sets the consult_participant_id of this QueueConversationVideoEventTopicParticipant.


        :param consult_participant_id: The consult_participant_id of this QueueConversationVideoEventTopicParticipant.
        :type: str
        """
        
        self._consult_participant_id = consult_participant_id

    @property
    def address(self):
        """
        Gets the address of this QueueConversationVideoEventTopicParticipant.


        :return: The address of this QueueConversationVideoEventTopicParticipant.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this QueueConversationVideoEventTopicParticipant.


        :param address: The address of this QueueConversationVideoEventTopicParticipant.
        :type: str
        """
        
        self._address = address

    @property
    def wrapup_required(self):
        """
        Gets the wrapup_required of this QueueConversationVideoEventTopicParticipant.


        :return: The wrapup_required of this QueueConversationVideoEventTopicParticipant.
        :rtype: bool
        """
        return self._wrapup_required

    @wrapup_required.setter
    def wrapup_required(self, wrapup_required):
        """
        Sets the wrapup_required of this QueueConversationVideoEventTopicParticipant.


        :param wrapup_required: The wrapup_required of this QueueConversationVideoEventTopicParticipant.
        :type: bool
        """
        
        self._wrapup_required = wrapup_required

    @property
    def wrapup_expected(self):
        """
        Gets the wrapup_expected of this QueueConversationVideoEventTopicParticipant.


        :return: The wrapup_expected of this QueueConversationVideoEventTopicParticipant.
        :rtype: bool
        """
        return self._wrapup_expected

    @wrapup_expected.setter
    def wrapup_expected(self, wrapup_expected):
        """
        Sets the wrapup_expected of this QueueConversationVideoEventTopicParticipant.


        :param wrapup_expected: The wrapup_expected of this QueueConversationVideoEventTopicParticipant.
        :type: bool
        """
        
        self._wrapup_expected = wrapup_expected

    @property
    def wrapup_prompt(self):
        """
        Gets the wrapup_prompt of this QueueConversationVideoEventTopicParticipant.


        :return: The wrapup_prompt of this QueueConversationVideoEventTopicParticipant.
        :rtype: str
        """
        return self._wrapup_prompt

    @wrapup_prompt.setter
    def wrapup_prompt(self, wrapup_prompt):
        """
        Sets the wrapup_prompt of this QueueConversationVideoEventTopicParticipant.


        :param wrapup_prompt: The wrapup_prompt of this QueueConversationVideoEventTopicParticipant.
        :type: str
        """
        
        self._wrapup_prompt = wrapup_prompt

    @property
    def wrapup_timeout_ms(self):
        """
        Gets the wrapup_timeout_ms of this QueueConversationVideoEventTopicParticipant.


        :return: The wrapup_timeout_ms of this QueueConversationVideoEventTopicParticipant.
        :rtype: int
        """
        return self._wrapup_timeout_ms

    @wrapup_timeout_ms.setter
    def wrapup_timeout_ms(self, wrapup_timeout_ms):
        """
        Sets the wrapup_timeout_ms of this QueueConversationVideoEventTopicParticipant.


        :param wrapup_timeout_ms: The wrapup_timeout_ms of this QueueConversationVideoEventTopicParticipant.
        :type: int
        """
        
        self._wrapup_timeout_ms = wrapup_timeout_ms

    @property
    def wrapup(self):
        """
        Gets the wrapup of this QueueConversationVideoEventTopicParticipant.


        :return: The wrapup of this QueueConversationVideoEventTopicParticipant.
        :rtype: QueueConversationVideoEventTopicWrapup
        """
        return self._wrapup

    @wrapup.setter
    def wrapup(self, wrapup):
        """
        Sets the wrapup of this QueueConversationVideoEventTopicParticipant.


        :param wrapup: The wrapup of this QueueConversationVideoEventTopicParticipant.
        :type: QueueConversationVideoEventTopicWrapup
        """
        
        self._wrapup = wrapup

    @property
    def start_acw_time(self):
        """
        Gets the start_acw_time of this QueueConversationVideoEventTopicParticipant.


        :return: The start_acw_time of this QueueConversationVideoEventTopicParticipant.
        :rtype: datetime
        """
        return self._start_acw_time

    @start_acw_time.setter
    def start_acw_time(self, start_acw_time):
        """
        Sets the start_acw_time of this QueueConversationVideoEventTopicParticipant.


        :param start_acw_time: The start_acw_time of this QueueConversationVideoEventTopicParticipant.
        :type: datetime
        """
        
        self._start_acw_time = start_acw_time

    @property
    def end_acw_time(self):
        """
        Gets the end_acw_time of this QueueConversationVideoEventTopicParticipant.


        :return: The end_acw_time of this QueueConversationVideoEventTopicParticipant.
        :rtype: datetime
        """
        return self._end_acw_time

    @end_acw_time.setter
    def end_acw_time(self, end_acw_time):
        """
        Sets the end_acw_time of this QueueConversationVideoEventTopicParticipant.


        :param end_acw_time: The end_acw_time of this QueueConversationVideoEventTopicParticipant.
        :type: datetime
        """
        
        self._end_acw_time = end_acw_time

    @property
    def conversation_routing_data(self):
        """
        Gets the conversation_routing_data of this QueueConversationVideoEventTopicParticipant.


        :return: The conversation_routing_data of this QueueConversationVideoEventTopicParticipant.
        :rtype: QueueConversationVideoEventTopicConversationRoutingData
        """
        return self._conversation_routing_data

    @conversation_routing_data.setter
    def conversation_routing_data(self, conversation_routing_data):
        """
        Sets the conversation_routing_data of this QueueConversationVideoEventTopicParticipant.


        :param conversation_routing_data: The conversation_routing_data of this QueueConversationVideoEventTopicParticipant.
        :type: QueueConversationVideoEventTopicConversationRoutingData
        """
        
        self._conversation_routing_data = conversation_routing_data

    @property
    def alerting_timeout_ms(self):
        """
        Gets the alerting_timeout_ms of this QueueConversationVideoEventTopicParticipant.


        :return: The alerting_timeout_ms of this QueueConversationVideoEventTopicParticipant.
        :rtype: int
        """
        return self._alerting_timeout_ms

    @alerting_timeout_ms.setter
    def alerting_timeout_ms(self, alerting_timeout_ms):
        """
        Sets the alerting_timeout_ms of this QueueConversationVideoEventTopicParticipant.


        :param alerting_timeout_ms: The alerting_timeout_ms of this QueueConversationVideoEventTopicParticipant.
        :type: int
        """
        
        self._alerting_timeout_ms = alerting_timeout_ms

    @property
    def monitored_participant_id(self):
        """
        Gets the monitored_participant_id of this QueueConversationVideoEventTopicParticipant.


        :return: The monitored_participant_id of this QueueConversationVideoEventTopicParticipant.
        :rtype: str
        """
        return self._monitored_participant_id

    @monitored_participant_id.setter
    def monitored_participant_id(self, monitored_participant_id):
        """
        Sets the monitored_participant_id of this QueueConversationVideoEventTopicParticipant.


        :param monitored_participant_id: The monitored_participant_id of this QueueConversationVideoEventTopicParticipant.
        :type: str
        """
        
        self._monitored_participant_id = monitored_participant_id

    @property
    def screen_recording_state(self):
        """
        Gets the screen_recording_state of this QueueConversationVideoEventTopicParticipant.


        :return: The screen_recording_state of this QueueConversationVideoEventTopicParticipant.
        :rtype: str
        """
        return self._screen_recording_state

    @screen_recording_state.setter
    def screen_recording_state(self, screen_recording_state):
        """
        Sets the screen_recording_state of this QueueConversationVideoEventTopicParticipant.


        :param screen_recording_state: The screen_recording_state of this QueueConversationVideoEventTopicParticipant.
        :type: str
        """
        allowed_values = ["REQUESTED", "ACTIVE", "PAUSED", "STOPPED", "ERROR", "TIMEOUT"]
        if screen_recording_state.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for screen_recording_state -> " + screen_recording_state
            self._screen_recording_state = "outdated_sdk_version"
        else:
            self._screen_recording_state = screen_recording_state

    @property
    def flagged_reason(self):
        """
        Gets the flagged_reason of this QueueConversationVideoEventTopicParticipant.


        :return: The flagged_reason of this QueueConversationVideoEventTopicParticipant.
        :rtype: str
        """
        return self._flagged_reason

    @flagged_reason.setter
    def flagged_reason(self, flagged_reason):
        """
        Sets the flagged_reason of this QueueConversationVideoEventTopicParticipant.


        :param flagged_reason: The flagged_reason of this QueueConversationVideoEventTopicParticipant.
        :type: str
        """
        
        self._flagged_reason = flagged_reason

    @property
    def attributes(self):
        """
        Gets the attributes of this QueueConversationVideoEventTopicParticipant.


        :return: The attributes of this QueueConversationVideoEventTopicParticipant.
        :rtype: dict(str, str)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """
        Sets the attributes of this QueueConversationVideoEventTopicParticipant.


        :param attributes: The attributes of this QueueConversationVideoEventTopicParticipant.
        :type: dict(str, str)
        """
        
        self._attributes = attributes

    @property
    def calls(self):
        """
        Gets the calls of this QueueConversationVideoEventTopicParticipant.


        :return: The calls of this QueueConversationVideoEventTopicParticipant.
        :rtype: list[QueueConversationVideoEventTopicCall]
        """
        return self._calls

    @calls.setter
    def calls(self, calls):
        """
        Sets the calls of this QueueConversationVideoEventTopicParticipant.


        :param calls: The calls of this QueueConversationVideoEventTopicParticipant.
        :type: list[QueueConversationVideoEventTopicCall]
        """
        
        self._calls = calls

    @property
    def callbacks(self):
        """
        Gets the callbacks of this QueueConversationVideoEventTopicParticipant.


        :return: The callbacks of this QueueConversationVideoEventTopicParticipant.
        :rtype: list[QueueConversationVideoEventTopicCallback]
        """
        return self._callbacks

    @callbacks.setter
    def callbacks(self, callbacks):
        """
        Sets the callbacks of this QueueConversationVideoEventTopicParticipant.


        :param callbacks: The callbacks of this QueueConversationVideoEventTopicParticipant.
        :type: list[QueueConversationVideoEventTopicCallback]
        """
        
        self._callbacks = callbacks

    @property
    def chats(self):
        """
        Gets the chats of this QueueConversationVideoEventTopicParticipant.


        :return: The chats of this QueueConversationVideoEventTopicParticipant.
        :rtype: list[QueueConversationVideoEventTopicChat]
        """
        return self._chats

    @chats.setter
    def chats(self, chats):
        """
        Sets the chats of this QueueConversationVideoEventTopicParticipant.


        :param chats: The chats of this QueueConversationVideoEventTopicParticipant.
        :type: list[QueueConversationVideoEventTopicChat]
        """
        
        self._chats = chats

    @property
    def cobrowsesessions(self):
        """
        Gets the cobrowsesessions of this QueueConversationVideoEventTopicParticipant.


        :return: The cobrowsesessions of this QueueConversationVideoEventTopicParticipant.
        :rtype: list[QueueConversationVideoEventTopicCobrowse]
        """
        return self._cobrowsesessions

    @cobrowsesessions.setter
    def cobrowsesessions(self, cobrowsesessions):
        """
        Sets the cobrowsesessions of this QueueConversationVideoEventTopicParticipant.


        :param cobrowsesessions: The cobrowsesessions of this QueueConversationVideoEventTopicParticipant.
        :type: list[QueueConversationVideoEventTopicCobrowse]
        """
        
        self._cobrowsesessions = cobrowsesessions

    @property
    def emails(self):
        """
        Gets the emails of this QueueConversationVideoEventTopicParticipant.


        :return: The emails of this QueueConversationVideoEventTopicParticipant.
        :rtype: list[QueueConversationVideoEventTopicEmail]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """
        Sets the emails of this QueueConversationVideoEventTopicParticipant.


        :param emails: The emails of this QueueConversationVideoEventTopicParticipant.
        :type: list[QueueConversationVideoEventTopicEmail]
        """
        
        self._emails = emails

    @property
    def messages(self):
        """
        Gets the messages of this QueueConversationVideoEventTopicParticipant.


        :return: The messages of this QueueConversationVideoEventTopicParticipant.
        :rtype: list[QueueConversationVideoEventTopicMessage]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """
        Sets the messages of this QueueConversationVideoEventTopicParticipant.


        :param messages: The messages of this QueueConversationVideoEventTopicParticipant.
        :type: list[QueueConversationVideoEventTopicMessage]
        """
        
        self._messages = messages

    @property
    def screenshares(self):
        """
        Gets the screenshares of this QueueConversationVideoEventTopicParticipant.


        :return: The screenshares of this QueueConversationVideoEventTopicParticipant.
        :rtype: list[QueueConversationVideoEventTopicScreenshare]
        """
        return self._screenshares

    @screenshares.setter
    def screenshares(self, screenshares):
        """
        Sets the screenshares of this QueueConversationVideoEventTopicParticipant.


        :param screenshares: The screenshares of this QueueConversationVideoEventTopicParticipant.
        :type: list[QueueConversationVideoEventTopicScreenshare]
        """
        
        self._screenshares = screenshares

    @property
    def social_expressions(self):
        """
        Gets the social_expressions of this QueueConversationVideoEventTopicParticipant.


        :return: The social_expressions of this QueueConversationVideoEventTopicParticipant.
        :rtype: list[QueueConversationVideoEventTopicSocialExpression]
        """
        return self._social_expressions

    @social_expressions.setter
    def social_expressions(self, social_expressions):
        """
        Sets the social_expressions of this QueueConversationVideoEventTopicParticipant.


        :param social_expressions: The social_expressions of this QueueConversationVideoEventTopicParticipant.
        :type: list[QueueConversationVideoEventTopicSocialExpression]
        """
        
        self._social_expressions = social_expressions

    @property
    def videos(self):
        """
        Gets the videos of this QueueConversationVideoEventTopicParticipant.


        :return: The videos of this QueueConversationVideoEventTopicParticipant.
        :rtype: list[QueueConversationVideoEventTopicVideo]
        """
        return self._videos

    @videos.setter
    def videos(self, videos):
        """
        Sets the videos of this QueueConversationVideoEventTopicParticipant.


        :param videos: The videos of this QueueConversationVideoEventTopicParticipant.
        :type: list[QueueConversationVideoEventTopicVideo]
        """
        
        self._videos = videos

    @property
    def additional_properties(self):
        """
        Gets the additional_properties of this QueueConversationVideoEventTopicParticipant.


        :return: The additional_properties of this QueueConversationVideoEventTopicParticipant.
        :rtype: object
        """
        return self._additional_properties

    @additional_properties.setter
    def additional_properties(self, additional_properties):
        """
        Sets the additional_properties of this QueueConversationVideoEventTopicParticipant.


        :param additional_properties: The additional_properties of this QueueConversationVideoEventTopicParticipant.
        :type: object
        """
        
        self._additional_properties = additional_properties

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

    def to_json(self):
        """
        Returns the model as raw JSON
        """
        return json.dumps(sanitize_for_serialization(self.to_dict()))

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

