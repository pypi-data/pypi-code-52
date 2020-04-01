# coding: utf-8

"""
    3Di API

    3Di simulation API (latest version: 3.0)   Framework release: 0.0.37   3Di core release: 2.0.6  deployed on:  02:54PM (UTC) on March 20, 2020  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class DamageSeconds(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'basic_post_processing': 'int',
        'cost_type': 'str',
        'flood_month': 'str',
        'inundation_period': 'str',
        'repair_time_infrastructure': 'str',
        'repair_time_buildings': 'str'
    }

    attribute_map = {
        'basic_post_processing': 'basic_post_processing',
        'cost_type': 'cost_type',
        'flood_month': 'flood_month',
        'inundation_period': 'inundation_period',
        'repair_time_infrastructure': 'repair_time_infrastructure',
        'repair_time_buildings': 'repair_time_buildings'
    }

    def __init__(self, basic_post_processing=None, cost_type=None, flood_month=None, inundation_period=None, repair_time_infrastructure=None, repair_time_buildings=None):  # noqa: E501
        """DamageSeconds - a model defined in OpenAPI"""  # noqa: E501

        self._basic_post_processing = None
        self._cost_type = None
        self._flood_month = None
        self._inundation_period = None
        self._repair_time_infrastructure = None
        self._repair_time_buildings = None
        self.discriminator = None

        if basic_post_processing is not None:
            self.basic_post_processing = basic_post_processing
        if cost_type is not None:
            self.cost_type = cost_type
        if flood_month is not None:
            self.flood_month = flood_month
        if inundation_period is not None:
            self.inundation_period = inundation_period
        if repair_time_infrastructure is not None:
            self.repair_time_infrastructure = repair_time_infrastructure
        if repair_time_buildings is not None:
            self.repair_time_buildings = repair_time_buildings

    @property
    def basic_post_processing(self):
        """Gets the basic_post_processing of this DamageSeconds.  # noqa: E501


        :return: The basic_post_processing of this DamageSeconds.  # noqa: E501
        :rtype: int
        """
        return self._basic_post_processing

    @basic_post_processing.setter
    def basic_post_processing(self, basic_post_processing):
        """Sets the basic_post_processing of this DamageSeconds.


        :param basic_post_processing: The basic_post_processing of this DamageSeconds.  # noqa: E501
        :type: int
        """

        self._basic_post_processing = basic_post_processing

    @property
    def cost_type(self):
        """Gets the cost_type of this DamageSeconds.  # noqa: E501

        'min', 'avg', or 'max'  # noqa: E501

        :return: The cost_type of this DamageSeconds.  # noqa: E501
        :rtype: str
        """
        return self._cost_type

    @cost_type.setter
    def cost_type(self, cost_type):
        """Sets the cost_type of this DamageSeconds.

        'min', 'avg', or 'max'  # noqa: E501

        :param cost_type: The cost_type of this DamageSeconds.  # noqa: E501
        :type: str
        """
        allowed_values = ["min", "avg", "max"]  # noqa: E501
        if cost_type not in allowed_values:
            raise ValueError(
                "Invalid value for `cost_type` ({0}), must be one of {1}"  # noqa: E501
                .format(cost_type, allowed_values)
            )

        self._cost_type = cost_type

    @property
    def flood_month(self):
        """Gets the flood_month of this DamageSeconds.  # noqa: E501


        :return: The flood_month of this DamageSeconds.  # noqa: E501
        :rtype: str
        """
        return self._flood_month

    @flood_month.setter
    def flood_month(self, flood_month):
        """Sets the flood_month of this DamageSeconds.


        :param flood_month: The flood_month of this DamageSeconds.  # noqa: E501
        :type: str
        """
        allowed_values = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]  # noqa: E501
        if flood_month not in allowed_values:
            raise ValueError(
                "Invalid value for `flood_month` ({0}), must be one of {1}"  # noqa: E501
                .format(flood_month, allowed_values)
            )

        self._flood_month = flood_month

    @property
    def inundation_period(self):
        """Gets the inundation_period of this DamageSeconds.  # noqa: E501


        :return: The inundation_period of this DamageSeconds.  # noqa: E501
        :rtype: str
        """
        return self._inundation_period

    @inundation_period.setter
    def inundation_period(self, inundation_period):
        """Sets the inundation_period of this DamageSeconds.


        :param inundation_period: The inundation_period of this DamageSeconds.  # noqa: E501
        :type: str
        """

        self._inundation_period = inundation_period

    @property
    def repair_time_infrastructure(self):
        """Gets the repair_time_infrastructure of this DamageSeconds.  # noqa: E501


        :return: The repair_time_infrastructure of this DamageSeconds.  # noqa: E501
        :rtype: str
        """
        return self._repair_time_infrastructure

    @repair_time_infrastructure.setter
    def repair_time_infrastructure(self, repair_time_infrastructure):
        """Sets the repair_time_infrastructure of this DamageSeconds.


        :param repair_time_infrastructure: The repair_time_infrastructure of this DamageSeconds.  # noqa: E501
        :type: str
        """

        self._repair_time_infrastructure = repair_time_infrastructure

    @property
    def repair_time_buildings(self):
        """Gets the repair_time_buildings of this DamageSeconds.  # noqa: E501


        :return: The repair_time_buildings of this DamageSeconds.  # noqa: E501
        :rtype: str
        """
        return self._repair_time_buildings

    @repair_time_buildings.setter
    def repair_time_buildings(self, repair_time_buildings):
        """Sets the repair_time_buildings of this DamageSeconds.


        :param repair_time_buildings: The repair_time_buildings of this DamageSeconds.  # noqa: E501
        :type: str
        """

        self._repair_time_buildings = repair_time_buildings

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DamageSeconds):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
