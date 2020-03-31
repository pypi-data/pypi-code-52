# coding: utf-8

"""
    Intrinio API

    Welcome to the Intrinio API! Through our Financial Data Marketplace, we offer a wide selection of financial data feed APIs sourced by our own proprietary processes as well as from many data vendors. For a complete API request / response reference please view the [Intrinio API documentation](https://intrinio.com/documentation/api_v2). If you need additional help in using the API, please visit the [Intrinio website](https://intrinio.com) and click on the chat icon in the lower right corner.  # noqa: E501

    OpenAPI spec version: 2.9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from intrinio_sdk.api_client import ApiClient


class ZacksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_zacks_analyst_ratings(self, **kwargs):  # noqa: E501
        """Zacks Analyst Ratings  # noqa: E501

        Returns buy, sell, and hold recommendations from analysts at brokerages for all companies in the Zacks universe. Zack’s storied research team aggregates and validates the ratings from professional analysts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_zacks_analyst_ratings(_async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID)
        :param str start_date: Limit ratings to those on or after this date
        :param str end_date: Limit ratings to those on or before this date
        :param float mean_greater: Return only records with a mean (average) higher than this value
        :param float mean_less: Return only records with a mean (average) lower than this value
        :param int strong_buys_greater: Return only records with more than this many Strong Buy recommendations
        :param int strong_buys_less: Return only records with fewer than this many Strong Buy recommendations
        :param int buys_greater: Return only records with more than this many Buy recommendations
        :param int buys_less: Return only records with fewer than this many Buy recommendations
        :param int holds_greater: Return only records with more than this many Hold recommendations
        :param int holds_less: Return only records with fewer than this many Hold recommendations
        :param int sells_greater: Return only records with more than this many Sell recommendations
        :param int sells_less: Return only records with fewer than this many Sell recommendations
        :param int strong_sells_greater: Return only records with more than this many Strong Sell recommendations
        :param int strong_sells_less: Return only records with fewer than this many Strong Sell recommendations
        :param int total_greater: Return only records with more than this many recommendations, regardless of type
        :param int total_less: Return only records with fewer than this many recommendations, regardless of type
        :param int page_size: The number of results to return
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseZacksAnalystRatings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_zacks_analyst_ratings_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_zacks_analyst_ratings_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_zacks_analyst_ratings_with_http_info(self, **kwargs):  # noqa: E501
        """Zacks Analyst Ratings  # noqa: E501

        Returns buy, sell, and hold recommendations from analysts at brokerages for all companies in the Zacks universe. Zack’s storied research team aggregates and validates the ratings from professional analysts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_zacks_analyst_ratings_with_http_info(_async=True)
        >>> result = thread.get()

        :param async bool
        :param str identifier: A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID)
        :param str start_date: Limit ratings to those on or after this date
        :param str end_date: Limit ratings to those on or before this date
        :param float mean_greater: Return only records with a mean (average) higher than this value
        :param float mean_less: Return only records with a mean (average) lower than this value
        :param int strong_buys_greater: Return only records with more than this many Strong Buy recommendations
        :param int strong_buys_less: Return only records with fewer than this many Strong Buy recommendations
        :param int buys_greater: Return only records with more than this many Buy recommendations
        :param int buys_less: Return only records with fewer than this many Buy recommendations
        :param int holds_greater: Return only records with more than this many Hold recommendations
        :param int holds_less: Return only records with fewer than this many Hold recommendations
        :param int sells_greater: Return only records with more than this many Sell recommendations
        :param int sells_less: Return only records with fewer than this many Sell recommendations
        :param int strong_sells_greater: Return only records with more than this many Strong Sell recommendations
        :param int strong_sells_less: Return only records with fewer than this many Strong Sell recommendations
        :param int total_greater: Return only records with more than this many recommendations, regardless of type
        :param int total_less: Return only records with fewer than this many recommendations, regardless of type
        :param int page_size: The number of results to return
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseZacksAnalystRatings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['identifier', 'start_date', 'end_date', 'mean_greater', 'mean_less', 'strong_buys_greater', 'strong_buys_less', 'buys_greater', 'buys_less', 'holds_greater', 'holds_less', 'sells_greater', 'sells_less', 'strong_sells_greater', 'strong_sells_less', 'total_greater', 'total_less', 'page_size', 'next_page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_zacks_analyst_ratings" % key
                )
            params[key] = val
        del params['kwargs']

        if 'mean_greater' in params and params['mean_greater'] > 5:  # noqa: E501
            raise ValueError("Invalid value for parameter `mean_greater` when calling `get_zacks_analyst_ratings`, must be a value less than or equal to `5`")  # noqa: E501
        if 'mean_greater' in params and params['mean_greater'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `mean_greater` when calling `get_zacks_analyst_ratings`, must be a value greater than or equal to `1`")  # noqa: E501
        if 'mean_less' in params and params['mean_less'] > 5:  # noqa: E501
            raise ValueError("Invalid value for parameter `mean_less` when calling `get_zacks_analyst_ratings`, must be a value less than or equal to `5`")  # noqa: E501
        if 'mean_less' in params and params['mean_less'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `mean_less` when calling `get_zacks_analyst_ratings`, must be a value greater than or equal to `1`")  # noqa: E501
        if 'strong_buys_greater' in params and params['strong_buys_greater'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `strong_buys_greater` when calling `get_zacks_analyst_ratings`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'strong_buys_less' in params and params['strong_buys_less'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `strong_buys_less` when calling `get_zacks_analyst_ratings`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'buys_greater' in params and params['buys_greater'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `buys_greater` when calling `get_zacks_analyst_ratings`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'buys_less' in params and params['buys_less'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `buys_less` when calling `get_zacks_analyst_ratings`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'holds_greater' in params and params['holds_greater'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `holds_greater` when calling `get_zacks_analyst_ratings`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'holds_less' in params and params['holds_less'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `holds_less` when calling `get_zacks_analyst_ratings`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'sells_greater' in params and params['sells_greater'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `sells_greater` when calling `get_zacks_analyst_ratings`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'sells_less' in params and params['sells_less'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `sells_less` when calling `get_zacks_analyst_ratings`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'strong_sells_greater' in params and params['strong_sells_greater'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `strong_sells_greater` when calling `get_zacks_analyst_ratings`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'strong_sells_less' in params and params['strong_sells_less'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `strong_sells_less` when calling `get_zacks_analyst_ratings`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'total_greater' in params and params['total_greater'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `total_greater` when calling `get_zacks_analyst_ratings`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'total_less' in params and params['total_less'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `total_less` when calling `get_zacks_analyst_ratings`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'page_size' in params and params['page_size'] > 10000:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `get_zacks_analyst_ratings`, must be a value less than or equal to `10000`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'identifier' in params:
            query_params.append(('identifier', params['identifier']))  # noqa: E501
        if 'start_date' in params:
            query_params.append(('start_date', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('end_date', params['end_date']))  # noqa: E501
        if 'mean_greater' in params:
            query_params.append(('mean_greater', params['mean_greater']))  # noqa: E501
        if 'mean_less' in params:
            query_params.append(('mean_less', params['mean_less']))  # noqa: E501
        if 'strong_buys_greater' in params:
            query_params.append(('strong_buys_greater', params['strong_buys_greater']))  # noqa: E501
        if 'strong_buys_less' in params:
            query_params.append(('strong_buys_less', params['strong_buys_less']))  # noqa: E501
        if 'buys_greater' in params:
            query_params.append(('buys_greater', params['buys_greater']))  # noqa: E501
        if 'buys_less' in params:
            query_params.append(('buys_less', params['buys_less']))  # noqa: E501
        if 'holds_greater' in params:
            query_params.append(('holds_greater', params['holds_greater']))  # noqa: E501
        if 'holds_less' in params:
            query_params.append(('holds_less', params['holds_less']))  # noqa: E501
        if 'sells_greater' in params:
            query_params.append(('sells_greater', params['sells_greater']))  # noqa: E501
        if 'sells_less' in params:
            query_params.append(('sells_less', params['sells_less']))  # noqa: E501
        if 'strong_sells_greater' in params:
            query_params.append(('strong_sells_greater', params['strong_sells_greater']))  # noqa: E501
        if 'strong_sells_less' in params:
            query_params.append(('strong_sells_less', params['strong_sells_less']))  # noqa: E501
        if 'total_greater' in params:
            query_params.append(('total_greater', params['total_greater']))  # noqa: E501
        if 'total_less' in params:
            query_params.append(('total_less', params['total_less']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'next_page' in params:
            query_params.append(('next_page', params['next_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/zacks/analyst_ratings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseZacksAnalystRatings',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_zacks_eps_surprises(self, **kwargs):  # noqa: E501
        """Zacks EPS Surprises  # noqa: E501

        Returns Zacks eps surprise data for all Securities.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_zacks_eps_surprises(_async=True)
        >>> result = thread.get()

        :param async bool
        :param str start_date: Limit EPS surprises to those on or after this date
        :param str end_date: Limit EPS surprises to those on or before this date
        :param float eps_actual_greater: Return only records with an actual EPS higher than this value
        :param float eps_actual_less: Return only records with an actual EPS lower than this value
        :param float eps_mean_estimate_greater: Return only records with an EPS mean estimate greater than this value
        :param float eps_mean_estimate_less: Return only records with an EPS mean estimate lower than this value
        :param float eps_amount_diff_greater: Return only records with an EPS amount difference greater than this value
        :param float eps_amount_diff_less: Return only records with an EPS amount difference less than this value
        :param float eps_percent_diff_greater: Return only records with an EPS percent difference greater than this value
        :param float eps_percent_diff_less: Return only records with an EPS percent difference less than this value
        :param float eps_count_estimate_greater: Return only records with an EPS count estimate greater than this value
        :param float eps_count_estimate_less: Return only records with an EPS count estimate less than this value
        :param float eps_std_dev_estimate_greater: Return only records with an EPS standard deviation greater than this value
        :param float eps_std_dev_estimate_less: Return only records with an EPS standard deviation less than this value
        :param int page_size: The number of results to return
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseZacksEPSSurprises
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_zacks_eps_surprises_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_zacks_eps_surprises_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_zacks_eps_surprises_with_http_info(self, **kwargs):  # noqa: E501
        """Zacks EPS Surprises  # noqa: E501

        Returns Zacks eps surprise data for all Securities.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_zacks_eps_surprises_with_http_info(_async=True)
        >>> result = thread.get()

        :param async bool
        :param str start_date: Limit EPS surprises to those on or after this date
        :param str end_date: Limit EPS surprises to those on or before this date
        :param float eps_actual_greater: Return only records with an actual EPS higher than this value
        :param float eps_actual_less: Return only records with an actual EPS lower than this value
        :param float eps_mean_estimate_greater: Return only records with an EPS mean estimate greater than this value
        :param float eps_mean_estimate_less: Return only records with an EPS mean estimate lower than this value
        :param float eps_amount_diff_greater: Return only records with an EPS amount difference greater than this value
        :param float eps_amount_diff_less: Return only records with an EPS amount difference less than this value
        :param float eps_percent_diff_greater: Return only records with an EPS percent difference greater than this value
        :param float eps_percent_diff_less: Return only records with an EPS percent difference less than this value
        :param float eps_count_estimate_greater: Return only records with an EPS count estimate greater than this value
        :param float eps_count_estimate_less: Return only records with an EPS count estimate less than this value
        :param float eps_std_dev_estimate_greater: Return only records with an EPS standard deviation greater than this value
        :param float eps_std_dev_estimate_less: Return only records with an EPS standard deviation less than this value
        :param int page_size: The number of results to return
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseZacksEPSSurprises
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_date', 'end_date', 'eps_actual_greater', 'eps_actual_less', 'eps_mean_estimate_greater', 'eps_mean_estimate_less', 'eps_amount_diff_greater', 'eps_amount_diff_less', 'eps_percent_diff_greater', 'eps_percent_diff_less', 'eps_count_estimate_greater', 'eps_count_estimate_less', 'eps_std_dev_estimate_greater', 'eps_std_dev_estimate_less', 'page_size', 'next_page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_zacks_eps_surprises" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page_size' in params and params['page_size'] > 10000:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `get_zacks_eps_surprises`, must be a value less than or equal to `10000`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_date' in params:
            query_params.append(('start_date', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('end_date', params['end_date']))  # noqa: E501
        if 'eps_actual_greater' in params:
            query_params.append(('eps_actual_greater', params['eps_actual_greater']))  # noqa: E501
        if 'eps_actual_less' in params:
            query_params.append(('eps_actual_less', params['eps_actual_less']))  # noqa: E501
        if 'eps_mean_estimate_greater' in params:
            query_params.append(('eps_mean_estimate_greater', params['eps_mean_estimate_greater']))  # noqa: E501
        if 'eps_mean_estimate_less' in params:
            query_params.append(('eps_mean_estimate_less', params['eps_mean_estimate_less']))  # noqa: E501
        if 'eps_amount_diff_greater' in params:
            query_params.append(('eps_amount_diff_greater', params['eps_amount_diff_greater']))  # noqa: E501
        if 'eps_amount_diff_less' in params:
            query_params.append(('eps_amount_diff_less', params['eps_amount_diff_less']))  # noqa: E501
        if 'eps_percent_diff_greater' in params:
            query_params.append(('eps_percent_diff_greater', params['eps_percent_diff_greater']))  # noqa: E501
        if 'eps_percent_diff_less' in params:
            query_params.append(('eps_percent_diff_less', params['eps_percent_diff_less']))  # noqa: E501
        if 'eps_count_estimate_greater' in params:
            query_params.append(('eps_count_estimate_greater', params['eps_count_estimate_greater']))  # noqa: E501
        if 'eps_count_estimate_less' in params:
            query_params.append(('eps_count_estimate_less', params['eps_count_estimate_less']))  # noqa: E501
        if 'eps_std_dev_estimate_greater' in params:
            query_params.append(('eps_std_dev_estimate_greater', params['eps_std_dev_estimate_greater']))  # noqa: E501
        if 'eps_std_dev_estimate_less' in params:
            query_params.append(('eps_std_dev_estimate_less', params['eps_std_dev_estimate_less']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'next_page' in params:
            query_params.append(('next_page', params['next_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/zacks/eps_surprises', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseZacksEPSSurprises',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_zacks_sales_surprises(self, **kwargs):  # noqa: E501
        """Zacks Sales Surprises  # noqa: E501

        Returns Zacks sales surprise data for all Securities.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_zacks_sales_surprises(_async=True)
        >>> result = thread.get()

        :param async bool
        :param str start_date: Limit sales surprises to those on or after this date
        :param str end_date: Limit sales surprises to those on or before this date
        :param float sales_actual_greater: Return only records with an actual sales higher than this value
        :param float sales_actual_less: Return only records with an actual sales lower than this value
        :param float sales_mean_estimate_greater: Return only records with a sales mean estimate greater than this value
        :param float sales_mean_estimate_less: Return only records with a sales mean estimate lower than this value
        :param float sales_amount_diff_greater: Return only records with a sales amount difference greater than this value
        :param float sales_amount_diff_less: Return only records with a sales amount difference less than this value
        :param float sales_percent_diff_greater: Return only records with a sales percent difference greater than this value
        :param float sales_percent_diff_less: Return only records with a sales percent difference less than this value
        :param float sales_count_estimate_greater: Return only records with a sales count estimate greater than this value
        :param float sales_count_estimate_less: Return only records with a sales count estimate less than this value
        :param float sales_std_dev_estimate_greater: Return only records with a sales standard deviation greater than this value
        :param float sales_std_dev_estimate_less: Return only records with a sales standard deviation less than this value
        :param int page_size: The number of results to return
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseZacksSalesSurprises
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_zacks_sales_surprises_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_zacks_sales_surprises_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_zacks_sales_surprises_with_http_info(self, **kwargs):  # noqa: E501
        """Zacks Sales Surprises  # noqa: E501

        Returns Zacks sales surprise data for all Securities.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_zacks_sales_surprises_with_http_info(_async=True)
        >>> result = thread.get()

        :param async bool
        :param str start_date: Limit sales surprises to those on or after this date
        :param str end_date: Limit sales surprises to those on or before this date
        :param float sales_actual_greater: Return only records with an actual sales higher than this value
        :param float sales_actual_less: Return only records with an actual sales lower than this value
        :param float sales_mean_estimate_greater: Return only records with a sales mean estimate greater than this value
        :param float sales_mean_estimate_less: Return only records with a sales mean estimate lower than this value
        :param float sales_amount_diff_greater: Return only records with a sales amount difference greater than this value
        :param float sales_amount_diff_less: Return only records with a sales amount difference less than this value
        :param float sales_percent_diff_greater: Return only records with a sales percent difference greater than this value
        :param float sales_percent_diff_less: Return only records with a sales percent difference less than this value
        :param float sales_count_estimate_greater: Return only records with a sales count estimate greater than this value
        :param float sales_count_estimate_less: Return only records with a sales count estimate less than this value
        :param float sales_std_dev_estimate_greater: Return only records with a sales standard deviation greater than this value
        :param float sales_std_dev_estimate_less: Return only records with a sales standard deviation less than this value
        :param int page_size: The number of results to return
        :param str next_page: Gets the next page of data from a previous API call
        :return: ApiResponseZacksSalesSurprises
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_date', 'end_date', 'sales_actual_greater', 'sales_actual_less', 'sales_mean_estimate_greater', 'sales_mean_estimate_less', 'sales_amount_diff_greater', 'sales_amount_diff_less', 'sales_percent_diff_greater', 'sales_percent_diff_less', 'sales_count_estimate_greater', 'sales_count_estimate_less', 'sales_std_dev_estimate_greater', 'sales_std_dev_estimate_less', 'page_size', 'next_page']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_zacks_sales_surprises" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page_size' in params and params['page_size'] > 10000:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `get_zacks_sales_surprises`, must be a value less than or equal to `10000`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_date' in params:
            query_params.append(('start_date', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('end_date', params['end_date']))  # noqa: E501
        if 'sales_actual_greater' in params:
            query_params.append(('sales_actual_greater', params['sales_actual_greater']))  # noqa: E501
        if 'sales_actual_less' in params:
            query_params.append(('sales_actual_less', params['sales_actual_less']))  # noqa: E501
        if 'sales_mean_estimate_greater' in params:
            query_params.append(('sales_mean_estimate_greater', params['sales_mean_estimate_greater']))  # noqa: E501
        if 'sales_mean_estimate_less' in params:
            query_params.append(('sales_mean_estimate_less', params['sales_mean_estimate_less']))  # noqa: E501
        if 'sales_amount_diff_greater' in params:
            query_params.append(('sales_amount_diff_greater', params['sales_amount_diff_greater']))  # noqa: E501
        if 'sales_amount_diff_less' in params:
            query_params.append(('sales_amount_diff_less', params['sales_amount_diff_less']))  # noqa: E501
        if 'sales_percent_diff_greater' in params:
            query_params.append(('sales_percent_diff_greater', params['sales_percent_diff_greater']))  # noqa: E501
        if 'sales_percent_diff_less' in params:
            query_params.append(('sales_percent_diff_less', params['sales_percent_diff_less']))  # noqa: E501
        if 'sales_count_estimate_greater' in params:
            query_params.append(('sales_count_estimate_greater', params['sales_count_estimate_greater']))  # noqa: E501
        if 'sales_count_estimate_less' in params:
            query_params.append(('sales_count_estimate_less', params['sales_count_estimate_less']))  # noqa: E501
        if 'sales_std_dev_estimate_greater' in params:
            query_params.append(('sales_std_dev_estimate_greater', params['sales_std_dev_estimate_greater']))  # noqa: E501
        if 'sales_std_dev_estimate_less' in params:
            query_params.append(('sales_std_dev_estimate_less', params['sales_std_dev_estimate_less']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'next_page' in params:
            query_params.append(('next_page', params['next_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/zacks/sales_surprises', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResponseZacksSalesSurprises',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
