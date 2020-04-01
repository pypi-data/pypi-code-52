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

class SurveyQuestion(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SurveyQuestion - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'text': 'str',
            'help_text': 'str',
            'type': 'str',
            'na_enabled': 'bool',
            'visibility_condition': 'VisibilityCondition',
            'answer_options': 'list[AnswerOption]',
            'max_response_characters': 'int',
            'explanation_prompt': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'text': 'text',
            'help_text': 'helpText',
            'type': 'type',
            'na_enabled': 'naEnabled',
            'visibility_condition': 'visibilityCondition',
            'answer_options': 'answerOptions',
            'max_response_characters': 'maxResponseCharacters',
            'explanation_prompt': 'explanationPrompt'
        }

        self._id = None
        self._text = None
        self._help_text = None
        self._type = None
        self._na_enabled = None
        self._visibility_condition = None
        self._answer_options = None
        self._max_response_characters = None
        self._explanation_prompt = None

    @property
    def id(self):
        """
        Gets the id of this SurveyQuestion.


        :return: The id of this SurveyQuestion.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SurveyQuestion.


        :param id: The id of this SurveyQuestion.
        :type: str
        """
        
        self._id = id

    @property
    def text(self):
        """
        Gets the text of this SurveyQuestion.


        :return: The text of this SurveyQuestion.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this SurveyQuestion.


        :param text: The text of this SurveyQuestion.
        :type: str
        """
        
        self._text = text

    @property
    def help_text(self):
        """
        Gets the help_text of this SurveyQuestion.


        :return: The help_text of this SurveyQuestion.
        :rtype: str
        """
        return self._help_text

    @help_text.setter
    def help_text(self, help_text):
        """
        Sets the help_text of this SurveyQuestion.


        :param help_text: The help_text of this SurveyQuestion.
        :type: str
        """
        
        self._help_text = help_text

    @property
    def type(self):
        """
        Gets the type of this SurveyQuestion.


        :return: The type of this SurveyQuestion.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this SurveyQuestion.


        :param type: The type of this SurveyQuestion.
        :type: str
        """
        allowed_values = ["multipleChoiceQuestion", "freeTextQuestion", "npsQuestion", "readOnlyTextBlockQuestion"]
        if type.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for type -> " + type
            self._type = "outdated_sdk_version"
        else:
            self._type = type

    @property
    def na_enabled(self):
        """
        Gets the na_enabled of this SurveyQuestion.


        :return: The na_enabled of this SurveyQuestion.
        :rtype: bool
        """
        return self._na_enabled

    @na_enabled.setter
    def na_enabled(self, na_enabled):
        """
        Sets the na_enabled of this SurveyQuestion.


        :param na_enabled: The na_enabled of this SurveyQuestion.
        :type: bool
        """
        
        self._na_enabled = na_enabled

    @property
    def visibility_condition(self):
        """
        Gets the visibility_condition of this SurveyQuestion.


        :return: The visibility_condition of this SurveyQuestion.
        :rtype: VisibilityCondition
        """
        return self._visibility_condition

    @visibility_condition.setter
    def visibility_condition(self, visibility_condition):
        """
        Sets the visibility_condition of this SurveyQuestion.


        :param visibility_condition: The visibility_condition of this SurveyQuestion.
        :type: VisibilityCondition
        """
        
        self._visibility_condition = visibility_condition

    @property
    def answer_options(self):
        """
        Gets the answer_options of this SurveyQuestion.
        Options from which to choose an answer for this question. Only used by Multiple Choice type questions.

        :return: The answer_options of this SurveyQuestion.
        :rtype: list[AnswerOption]
        """
        return self._answer_options

    @answer_options.setter
    def answer_options(self, answer_options):
        """
        Sets the answer_options of this SurveyQuestion.
        Options from which to choose an answer for this question. Only used by Multiple Choice type questions.

        :param answer_options: The answer_options of this SurveyQuestion.
        :type: list[AnswerOption]
        """
        
        self._answer_options = answer_options

    @property
    def max_response_characters(self):
        """
        Gets the max_response_characters of this SurveyQuestion.
        How many characters are allowed in the text response to this question. Used by NPS and Free Text question types.

        :return: The max_response_characters of this SurveyQuestion.
        :rtype: int
        """
        return self._max_response_characters

    @max_response_characters.setter
    def max_response_characters(self, max_response_characters):
        """
        Sets the max_response_characters of this SurveyQuestion.
        How many characters are allowed in the text response to this question. Used by NPS and Free Text question types.

        :param max_response_characters: The max_response_characters of this SurveyQuestion.
        :type: int
        """
        
        self._max_response_characters = max_response_characters

    @property
    def explanation_prompt(self):
        """
        Gets the explanation_prompt of this SurveyQuestion.
        Prompt for details explaining the chosen NPS score. Used by NPS questions.

        :return: The explanation_prompt of this SurveyQuestion.
        :rtype: str
        """
        return self._explanation_prompt

    @explanation_prompt.setter
    def explanation_prompt(self, explanation_prompt):
        """
        Sets the explanation_prompt of this SurveyQuestion.
        Prompt for details explaining the chosen NPS score. Used by NPS questions.

        :param explanation_prompt: The explanation_prompt of this SurveyQuestion.
        :type: str
        """
        
        self._explanation_prompt = explanation_prompt

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

