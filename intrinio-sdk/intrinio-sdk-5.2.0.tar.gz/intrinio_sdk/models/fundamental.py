# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from intrinio_sdk.models.company_summary import CompanySummary  # noqa: F401,E501


class Fundamental(object):
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
        'statement_code': 'str',
        'fiscal_year': 'float',
        'fiscal_period': 'str',
        'type': 'str',
        'start_date': 'date',
        'end_date': 'date',
        'filing_date': 'datetime',
        'is_latest': 'bool',
        'company': 'CompanySummary'
    }

    attribute_map = {
        'id': 'id',
        'statement_code': 'statement_code',
        'fiscal_year': 'fiscal_year',
        'fiscal_period': 'fiscal_period',
        'type': 'type',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'filing_date': 'filing_date',
        'is_latest': 'is_latest',
        'company': 'company'
    }

    def __init__(self, id=None, statement_code=None, fiscal_year=None, fiscal_period=None, type=None, start_date=None, end_date=None, filing_date=None, is_latest=None, company=None):  # noqa: E501
        """Fundamental - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._statement_code = None
        self._fiscal_year = None
        self._fiscal_period = None
        self._type = None
        self._start_date = None
        self._end_date = None
        self._filing_date = None
        self._is_latest = None
        self._company = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if statement_code is not None:
            self.statement_code = statement_code
        if fiscal_year is not None:
            self.fiscal_year = fiscal_year
        if fiscal_period is not None:
            self.fiscal_period = fiscal_period
        if type is not None:
            self.type = type
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if filing_date is not None:
            self.filing_date = filing_date
        if is_latest is not None:
            self.is_latest = is_latest
        if company is not None:
            self.company = company

    @property
    def id(self):
        """Gets the id of this Fundamental.  # noqa: E501

        The Intrinio ID of the Fundamental  # noqa: E501

        :return: The id of this Fundamental.  # noqa: E501
        :rtype: str
        """
        return self._id
        
    @property
    def id_dict(self):
        """Gets the id of this Fundamental.  # noqa: E501

        The Intrinio ID of the Fundamental as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The id of this Fundamental.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.id
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'id': value }

        
        return result
        

    @id.setter
    def id(self, id):
        """Sets the id of this Fundamental.

        The Intrinio ID of the Fundamental  # noqa: E501

        :param id: The id of this Fundamental.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def statement_code(self):
        """Gets the statement_code of this Fundamental.  # noqa: E501

        The code of the financial statement that the Fundamental represents  # noqa: E501

        :return: The statement_code of this Fundamental.  # noqa: E501
        :rtype: str
        """
        return self._statement_code
        
    @property
    def statement_code_dict(self):
        """Gets the statement_code of this Fundamental.  # noqa: E501

        The code of the financial statement that the Fundamental represents as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The statement_code of this Fundamental.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.statement_code
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'statement_code': value }

        
        return result
        

    @statement_code.setter
    def statement_code(self, statement_code):
        """Sets the statement_code of this Fundamental.

        The code of the financial statement that the Fundamental represents  # noqa: E501

        :param statement_code: The statement_code of this Fundamental.  # noqa: E501
        :type: str
        """

        self._statement_code = statement_code

    @property
    def fiscal_year(self):
        """Gets the fiscal_year of this Fundamental.  # noqa: E501

        The fiscal year  # noqa: E501

        :return: The fiscal_year of this Fundamental.  # noqa: E501
        :rtype: float
        """
        return self._fiscal_year
        
    @property
    def fiscal_year_dict(self):
        """Gets the fiscal_year of this Fundamental.  # noqa: E501

        The fiscal year as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The fiscal_year of this Fundamental.  # noqa: E501
        :rtype: float
        """

        result = None

        value = self.fiscal_year
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'fiscal_year': value }

        
        return result
        

    @fiscal_year.setter
    def fiscal_year(self, fiscal_year):
        """Sets the fiscal_year of this Fundamental.

        The fiscal year  # noqa: E501

        :param fiscal_year: The fiscal_year of this Fundamental.  # noqa: E501
        :type: float
        """

        self._fiscal_year = fiscal_year

    @property
    def fiscal_period(self):
        """Gets the fiscal_period of this Fundamental.  # noqa: E501

        The fiscal period  # noqa: E501

        :return: The fiscal_period of this Fundamental.  # noqa: E501
        :rtype: str
        """
        return self._fiscal_period
        
    @property
    def fiscal_period_dict(self):
        """Gets the fiscal_period of this Fundamental.  # noqa: E501

        The fiscal period as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The fiscal_period of this Fundamental.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.fiscal_period
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'fiscal_period': value }

        
        return result
        

    @fiscal_period.setter
    def fiscal_period(self, fiscal_period):
        """Sets the fiscal_period of this Fundamental.

        The fiscal period  # noqa: E501

        :param fiscal_period: The fiscal_period of this Fundamental.  # noqa: E501
        :type: str
        """

        self._fiscal_period = fiscal_period

    @property
    def type(self):
        """Gets the type of this Fundamental.  # noqa: E501

        The type of Fundamental  # noqa: E501

        :return: The type of this Fundamental.  # noqa: E501
        :rtype: str
        """
        return self._type
        
    @property
    def type_dict(self):
        """Gets the type of this Fundamental.  # noqa: E501

        The type of Fundamental as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The type of this Fundamental.  # noqa: E501
        :rtype: str
        """

        result = None

        value = self.type
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'type': value }

        
        return result
        

    @type.setter
    def type(self, type):
        """Sets the type of this Fundamental.

        The type of Fundamental  # noqa: E501

        :param type: The type of this Fundamental.  # noqa: E501
        :type: str
        """
        allowed_values = ["reported", "restated", "calculated"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def start_date(self):
        """Gets the start_date of this Fundamental.  # noqa: E501

        The period start date  # noqa: E501

        :return: The start_date of this Fundamental.  # noqa: E501
        :rtype: date
        """
        return self._start_date
        
    @property
    def start_date_dict(self):
        """Gets the start_date of this Fundamental.  # noqa: E501

        The period start date as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The start_date of this Fundamental.  # noqa: E501
        :rtype: date
        """

        result = None

        value = self.start_date
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'start_date': value }

        
        return result
        

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Fundamental.

        The period start date  # noqa: E501

        :param start_date: The start_date of this Fundamental.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this Fundamental.  # noqa: E501

        The period start date  # noqa: E501

        :return: The end_date of this Fundamental.  # noqa: E501
        :rtype: date
        """
        return self._end_date
        
    @property
    def end_date_dict(self):
        """Gets the end_date of this Fundamental.  # noqa: E501

        The period start date as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The end_date of this Fundamental.  # noqa: E501
        :rtype: date
        """

        result = None

        value = self.end_date
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'end_date': value }

        
        return result
        

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this Fundamental.

        The period start date  # noqa: E501

        :param end_date: The end_date of this Fundamental.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def filing_date(self):
        """Gets the filing_date of this Fundamental.  # noqa: E501

        The date and time when the Fundamental was filed with the SEC  # noqa: E501

        :return: The filing_date of this Fundamental.  # noqa: E501
        :rtype: datetime
        """
        return self._filing_date
        
    @property
    def filing_date_dict(self):
        """Gets the filing_date of this Fundamental.  # noqa: E501

        The date and time when the Fundamental was filed with the SEC as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The filing_date of this Fundamental.  # noqa: E501
        :rtype: datetime
        """

        result = None

        value = self.filing_date
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'filing_date': value }

        
        return result
        

    @filing_date.setter
    def filing_date(self, filing_date):
        """Sets the filing_date of this Fundamental.

        The date and time when the Fundamental was filed with the SEC  # noqa: E501

        :param filing_date: The filing_date of this Fundamental.  # noqa: E501
        :type: datetime
        """

        self._filing_date = filing_date

    @property
    def is_latest(self):
        """Gets the is_latest of this Fundamental.  # noqa: E501

        Is this the latest fundamental available based on the company's most recent filings? Use the Lookup Fundamental endpoint to find the latest fundamental (<a href=\"https://docs.intrinio.com/documentation/web_api/lookup_fundamental_v2\" target=\"_blank\">reference</a>)  # noqa: E501

        :return: The is_latest of this Fundamental.  # noqa: E501
        :rtype: bool
        """
        return self._is_latest
        
    @property
    def is_latest_dict(self):
        """Gets the is_latest of this Fundamental.  # noqa: E501

        Is this the latest fundamental available based on the company's most recent filings? Use the Lookup Fundamental endpoint to find the latest fundamental (<a href=\"https://docs.intrinio.com/documentation/web_api/lookup_fundamental_v2\" target=\"_blank\">reference</a>) as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The is_latest of this Fundamental.  # noqa: E501
        :rtype: bool
        """

        result = None

        value = self.is_latest
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'is_latest': value }

        
        return result
        

    @is_latest.setter
    def is_latest(self, is_latest):
        """Sets the is_latest of this Fundamental.

        Is this the latest fundamental available based on the company's most recent filings? Use the Lookup Fundamental endpoint to find the latest fundamental (<a href=\"https://docs.intrinio.com/documentation/web_api/lookup_fundamental_v2\" target=\"_blank\">reference</a>)  # noqa: E501

        :param is_latest: The is_latest of this Fundamental.  # noqa: E501
        :type: bool
        """

        self._is_latest = is_latest

    @property
    def company(self):
        """Gets the company of this Fundamental.  # noqa: E501

        The Company that the Fundamental was belongs to  # noqa: E501

        :return: The company of this Fundamental.  # noqa: E501
        :rtype: CompanySummary
        """
        return self._company
        
    @property
    def company_dict(self):
        """Gets the company of this Fundamental.  # noqa: E501

        The Company that the Fundamental was belongs to as a dictionary. Useful for Panda Dataframes.  # noqa: E501

        :return: The company of this Fundamental.  # noqa: E501
        :rtype: CompanySummary
        """

        result = None

        value = self.company
        if isinstance(value, list):
            result = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result = value.to_dict()
        elif isinstance(value, dict):
            result = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result = { 'company': value }

        
        return result
        

    @company.setter
    def company(self, company):
        """Sets the company of this Fundamental.

        The Company that the Fundamental was belongs to  # noqa: E501

        :param company: The company of this Fundamental.  # noqa: E501
        :type: CompanySummary
        """

        self._company = company

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Fundamental):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
