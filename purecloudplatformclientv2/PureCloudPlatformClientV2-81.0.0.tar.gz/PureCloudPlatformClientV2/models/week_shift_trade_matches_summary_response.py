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

class WeekShiftTradeMatchesSummaryResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        WeekShiftTradeMatchesSummaryResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'week_date': 'date',
            'count': 'int'
        }

        self.attribute_map = {
            'week_date': 'weekDate',
            'count': 'count'
        }

        self._week_date = None
        self._count = None

    @property
    def week_date(self):
        """
        Gets the week_date of this WeekShiftTradeMatchesSummaryResponse.
        The schedule week date in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

        :return: The week_date of this WeekShiftTradeMatchesSummaryResponse.
        :rtype: date
        """
        return self._week_date

    @week_date.setter
    def week_date(self, week_date):
        """
        Sets the week_date of this WeekShiftTradeMatchesSummaryResponse.
        The schedule week date in yyyy-MM-dd format. Dates are represented as an ISO-8601 string. For example: yyyy-MM-dd

        :param week_date: The week_date of this WeekShiftTradeMatchesSummaryResponse.
        :type: date
        """
        
        self._week_date = week_date

    @property
    def count(self):
        """
        Gets the count of this WeekShiftTradeMatchesSummaryResponse.
        The number of trades in the Matched state for the given week

        :return: The count of this WeekShiftTradeMatchesSummaryResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this WeekShiftTradeMatchesSummaryResponse.
        The number of trades in the Matched state for the given week

        :param count: The count of this WeekShiftTradeMatchesSummaryResponse.
        :type: int
        """
        
        self._count = count

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

