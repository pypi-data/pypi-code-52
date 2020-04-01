# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..client.configuration import Configuration
from ..client.api_client import ApiClient


class FoldersApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def list(self, account_id, **kwargs):
        """
        Gets a list of the folders for the account.
        Retrieves a list of the folders for the account, including the folder hierarchy. You can specify whether to return just the template folder or template folder and normal folders by setting the `template` query string parameter.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The external account number (int) or account ID Guid. (required)
        :param str include:
        :param str include_items:
        :param str start_position:
        :param str template: Specifies the items that are returned. Valid values are:   * include - The folder list will return normal folders plus template folders.  * only - Only the list of template folders are returned.
        :param str user_filter:
        :return: FoldersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_with_http_info(account_id, **kwargs)
        else:
            (data) = self.list_with_http_info(account_id, **kwargs)
            return data

    def list_with_http_info(self, account_id, **kwargs):
        """
        Gets a list of the folders for the account.
        Retrieves a list of the folders for the account, including the folder hierarchy. You can specify whether to return just the template folder or template folder and normal folders by setting the `template` query string parameter.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_with_http_info(account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The external account number (int) or account ID Guid. (required)
        :param str include:
        :param str include_items:
        :param str start_position:
        :param str template: Specifies the items that are returned. Valid values are:   * include - The folder list will return normal folders plus template folders.  * only - Only the list of template folders are returned.
        :param str user_filter:
        :return: FoldersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'include', 'include_items', 'start_position', 'template', 'user_filter']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `list`")


        collection_formats = {}

        resource_path = '/v2.1/accounts/{accountId}/folders'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']

        query_params = {}
        if 'include' in params:
            query_params['include'] = params['include']
        if 'include_items' in params:
            query_params['include_items'] = params['include_items']
        if 'start_position' in params:
            query_params['start_position'] = params['start_position']
        if 'template' in params:
            query_params['template'] = params['template']
        if 'user_filter' in params:
            query_params['user_filter'] = params['user_filter']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FoldersResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_items(self, account_id, folder_id, **kwargs):
        """
        Gets a list of the envelopes in the specified folder.
        Retrieves a list of the envelopes in the specified folder. You can narrow the query by specifying search criteria in the query string parameters.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_items(account_id, folder_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The external account number (int) or account ID Guid. (required)
        :param str folder_id: The ID of the folder being accessed. (required)
        :param str from_date:  Only return items on or after this date. If no value is provided, the default search is the previous 30 days. 
        :param str include_items:
        :param str owner_email:  The email of the folder owner. 
        :param str owner_name:  The name of the folder owner. 
        :param str search_text:  The search text used to search the items of the envelope. The search looks at recipient names and emails, envelope custom fields, sender name, and subject. 
        :param str start_position: The position of the folder items to return. This is used for repeated calls, when the number of envelopes returned is too much for one return (calls return 100 envelopes at a time). The default value is 0.
        :param str status: The current status of the envelope. If no value is provided, the default search is all/any status.
        :param str to_date: Only return items up to this date. If no value is provided, the default search is to the current date.
        :return: FolderItemsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_items_with_http_info(account_id, folder_id, **kwargs)
        else:
            (data) = self.list_items_with_http_info(account_id, folder_id, **kwargs)
            return data

    def list_items_with_http_info(self, account_id, folder_id, **kwargs):
        """
        Gets a list of the envelopes in the specified folder.
        Retrieves a list of the envelopes in the specified folder. You can narrow the query by specifying search criteria in the query string parameters.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_items_with_http_info(account_id, folder_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The external account number (int) or account ID Guid. (required)
        :param str folder_id: The ID of the folder being accessed. (required)
        :param str from_date:  Only return items on or after this date. If no value is provided, the default search is the previous 30 days. 
        :param str include_items:
        :param str owner_email:  The email of the folder owner. 
        :param str owner_name:  The name of the folder owner. 
        :param str search_text:  The search text used to search the items of the envelope. The search looks at recipient names and emails, envelope custom fields, sender name, and subject. 
        :param str start_position: The position of the folder items to return. This is used for repeated calls, when the number of envelopes returned is too much for one return (calls return 100 envelopes at a time). The default value is 0.
        :param str status: The current status of the envelope. If no value is provided, the default search is all/any status.
        :param str to_date: Only return items up to this date. If no value is provided, the default search is to the current date.
        :return: FolderItemsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'folder_id', 'from_date', 'include_items', 'owner_email', 'owner_name', 'search_text', 'start_position', 'status', 'to_date']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_items" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `list_items`")
        # verify the required parameter 'folder_id' is set
        if ('folder_id' not in params) or (params['folder_id'] is None):
            raise ValueError("Missing the required parameter `folder_id` when calling `list_items`")


        collection_formats = {}

        resource_path = '/v2.1/accounts/{accountId}/folders/{folderId}'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']
        if 'folder_id' in params:
            path_params['folderId'] = params['folder_id']

        query_params = {}
        if 'from_date' in params:
            query_params['from_date'] = params['from_date']
        if 'include_items' in params:
            query_params['include_items'] = params['include_items']
        if 'owner_email' in params:
            query_params['owner_email'] = params['owner_email']
        if 'owner_name' in params:
            query_params['owner_name'] = params['owner_name']
        if 'search_text' in params:
            query_params['search_text'] = params['search_text']
        if 'start_position' in params:
            query_params['start_position'] = params['start_position']
        if 'status' in params:
            query_params['status'] = params['status']
        if 'to_date' in params:
            query_params['to_date'] = params['to_date']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FolderItemsResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def move_envelopes(self, account_id, folder_id, **kwargs):
        """
        Moves an envelope from its current folder to the specified folder.
        Moves envelopes to the specified folder.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.move_envelopes(account_id, folder_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The external account number (int) or account ID Guid. (required)
        :param str folder_id: The ID of the folder being accessed. (required)
        :param FoldersRequest folders_request:
        :return: FoldersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.move_envelopes_with_http_info(account_id, folder_id, **kwargs)
        else:
            (data) = self.move_envelopes_with_http_info(account_id, folder_id, **kwargs)
            return data

    def move_envelopes_with_http_info(self, account_id, folder_id, **kwargs):
        """
        Moves an envelope from its current folder to the specified folder.
        Moves envelopes to the specified folder.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.move_envelopes_with_http_info(account_id, folder_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The external account number (int) or account ID Guid. (required)
        :param str folder_id: The ID of the folder being accessed. (required)
        :param FoldersRequest folders_request:
        :return: FoldersResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'folder_id', 'folders_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method move_envelopes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `move_envelopes`")
        # verify the required parameter 'folder_id' is set
        if ('folder_id' not in params) or (params['folder_id'] is None):
            raise ValueError("Missing the required parameter `folder_id` when calling `move_envelopes`")


        collection_formats = {}

        resource_path = '/v2.1/accounts/{accountId}/folders/{folderId}'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']
        if 'folder_id' in params:
            path_params['folderId'] = params['folder_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'folders_request' in params:
            body_params = params['folders_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FoldersResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def search(self, account_id, search_folder_id, **kwargs):
        """
        Gets a list of envelopes in folders matching the specified criteria.
        Retrieves a list of envelopes that match the criteria specified in the query.  If the user ID of the user making the call is the same as the user ID for any returned recipient, then the userId property is added to the returned information for those recipients.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.search(account_id, search_folder_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The external account number (int) or account ID Guid. (required)
        :param str search_folder_id: Specifies the envelope group that is searched by the request. These are logical groupings, not actual folder names. Valid values are: drafts, awaiting_my_signature, completed, out_for_signature. (required)
        :param str all: Specifies that all envelopes that match the criteria are returned.
        :param str count: Specifies the number of records returned in the cache. The number must be greater than 0 and less than or equal to 100.
        :param str from_date: Specifies the start of the date range to return. If no value is provided, the default search is the previous 30 days.
        :param str include_recipients: When set to **true**, the recipient information is returned in the response.
        :param str order: Specifies the order in which the list is returned. Valid values are: `asc` for ascending order, and `desc` for descending order.
        :param str order_by: Specifies the property used to sort the list. Valid values are: `action_required`, `created`, `completed`, `sent`, `signer_list`, `status`, or `subject`.
        :param str start_position: Specifies the the starting location in the result set of the items that are returned.
        :param str to_date: Specifies the end of the date range to return.
        :return: FolderItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.search_with_http_info(account_id, search_folder_id, **kwargs)
        else:
            (data) = self.search_with_http_info(account_id, search_folder_id, **kwargs)
            return data

    def search_with_http_info(self, account_id, search_folder_id, **kwargs):
        """
        Gets a list of envelopes in folders matching the specified criteria.
        Retrieves a list of envelopes that match the criteria specified in the query.  If the user ID of the user making the call is the same as the user ID for any returned recipient, then the userId property is added to the returned information for those recipients.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.search_with_http_info(account_id, search_folder_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account_id: The external account number (int) or account ID Guid. (required)
        :param str search_folder_id: Specifies the envelope group that is searched by the request. These are logical groupings, not actual folder names. Valid values are: drafts, awaiting_my_signature, completed, out_for_signature. (required)
        :param str all: Specifies that all envelopes that match the criteria are returned.
        :param str count: Specifies the number of records returned in the cache. The number must be greater than 0 and less than or equal to 100.
        :param str from_date: Specifies the start of the date range to return. If no value is provided, the default search is the previous 30 days.
        :param str include_recipients: When set to **true**, the recipient information is returned in the response.
        :param str order: Specifies the order in which the list is returned. Valid values are: `asc` for ascending order, and `desc` for descending order.
        :param str order_by: Specifies the property used to sort the list. Valid values are: `action_required`, `created`, `completed`, `sent`, `signer_list`, `status`, or `subject`.
        :param str start_position: Specifies the the starting location in the result set of the items that are returned.
        :param str to_date: Specifies the end of the date range to return.
        :return: FolderItemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'search_folder_id', 'all', 'count', 'from_date', 'include_recipients', 'order', 'order_by', 'start_position', 'to_date']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params) or (params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `search`")
        # verify the required parameter 'search_folder_id' is set
        if ('search_folder_id' not in params) or (params['search_folder_id'] is None):
            raise ValueError("Missing the required parameter `search_folder_id` when calling `search`")


        collection_formats = {}

        resource_path = '/v2.1/accounts/{accountId}/search_folders/{searchFolderId}'.replace('{format}', 'json')
        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']
        if 'search_folder_id' in params:
            path_params['searchFolderId'] = params['search_folder_id']

        query_params = {}
        if 'all' in params:
            query_params['all'] = params['all']
        if 'count' in params:
            query_params['count'] = params['count']
        if 'from_date' in params:
            query_params['from_date'] = params['from_date']
        if 'include_recipients' in params:
            query_params['include_recipients'] = params['include_recipients']
        if 'order' in params:
            query_params['order'] = params['order']
        if 'order_by' in params:
            query_params['order_by'] = params['order_by']
        if 'start_position' in params:
            query_params['start_position'] = params['start_position']
        if 'to_date' in params:
            query_params['to_date'] = params['to_date']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FolderItemResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
