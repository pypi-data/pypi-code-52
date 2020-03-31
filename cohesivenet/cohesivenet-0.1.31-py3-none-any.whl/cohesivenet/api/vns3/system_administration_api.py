# coding: utf-8

"""
    VNS3 Controller API

    Cohesive networks VNS3 API providing complete control of your network's addresses, routes, rules and edge  # noqa: E501

    The version of the OpenAPI document: 4.8
    Contact: solutions@cohesive.net
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import urllib3.exceptions


from cohesivenet import Logger
from cohesivenet.api_builder import VersionRouter
from cohesivenet.exceptions import ApiException
from cohesivenet.api.vns3 import configuration_api as config_api


def get_cloud_data(api_client, **kwargs):  # noqa: E501
    """get_cloud_data  # noqa: E501

    Returns cloud-specific data depending upon cloud type. Supports EC2 and GCE. More clouds coming soon.  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.get_cloud_data(client, async_req=True)

    :param async_req bool: execute request asynchronously
    :param _return_http_data_only: response data without head status code
                                    and headers
    :param _preload_content: if False, the urllib3.HTTPResponse object will
                                be returned without reading/decoding response
                                data. Default is True.
    :param _request_timeout: timeout setting for this request. If one
                                number provided, it will be total request
                                timeout. It can also be a pair (tuple) of
                                (connection, read) timeouts.
    :return: APIResponse or awaitable if async
    """

    local_var_params = locals()

    collection_formats = {}

    path_params = {}

    query_params = []

    header_params = {}

    form_params = []
    local_var_files = {}

    body_params = None
    # HTTP header `Accept`
    header_params["Accept"] = api_client.select_header_accept(
        ["application/json"]
    )  # noqa: E501

    # Authentication setting
    auth_settings = ["basicAuth"]  # noqa: E501

    return api_client.call_api(
        "/cloud_data",
        "GET",
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type="object",  # noqa: E501
        auth_settings=auth_settings,
        async_req=local_var_params.get("async_req"),
        _return_http_data_only=local_var_params.get(
            "_return_http_data_only"
        ),  # noqa: E501
        _preload_content=local_var_params.get("_preload_content", True),
        _request_timeout=local_var_params.get("_request_timeout"),
        collection_formats=collection_formats,
    )


def get_status(api_client, **kwargs):  # noqa: E501
    """get_status  # noqa: E501

    Describe Runtime status details  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.get_status(async_req=True)

    :param async_req bool: execute request asynchronously
    :param _return_http_data_only: response data without head status code
                                    and headers
    :param _preload_content: if False, the urllib3.HTTPResponse object will
                                be returned without reading/decoding response
                                data. Default is True.
    :param _request_timeout: timeout setting for this request. If one
                                number provided, it will be total request
                                timeout. It can also be a pair (tuple) of
                                (connection, read) timeouts.
    :return: APIResponse or awaitable if async
    """

    local_var_params = locals()

    collection_formats = {}

    path_params = {}

    query_params = []

    header_params = {}

    form_params = []
    local_var_files = {}

    body_params = None
    # HTTP header `Accept`
    header_params["Accept"] = api_client.select_header_accept(
        ["application/json"]
    )  # noqa: E501

    # Authentication setting
    auth_settings = ["basicAuth"]  # noqa: E501

    return api_client.call_api(
        "/status",
        "GET",
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type="object",  # noqa: E501
        auth_settings=auth_settings,
        async_req=local_var_params.get("async_req"),
        _return_http_data_only=local_var_params.get(
            "_return_http_data_only"
        ),  # noqa: E501
        _preload_content=local_var_params.get("_preload_content", True),
        _request_timeout=local_var_params.get("_request_timeout"),
        collection_formats=collection_formats,
    )


def get_system_status(api_client, timestamp=None, **kwargs):  # noqa: E501
    """get_system_status  # noqa: E501

    Provides information about the underlying appliance; memory, cpu, disk space, etc  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.get_system_status(async_req=True)

    :param async_req bool: execute request asynchronously
    :param int timestamp: Unix timestamp
    :param _return_http_data_only: response data without head status code
                                    and headers
    :param _preload_content: if False, the urllib3.HTTPResponse object will
                                be returned without reading/decoding response
                                data. Default is True.
    :param _request_timeout: timeout setting for this request. If one
                                number provided, it will be total request
                                timeout. It can also be a pair (tuple) of
                                (connection, read) timeouts.
    :return: APIResponse or awaitable if async
    """

    local_var_params = locals()

    request_params = ["timestamp"]  # noqa: E501

    collection_formats = {}

    path_params = {}

    query_params = []
    for param in [p for p in request_params if local_var_params.get(p) is not None]:
        query_params.append((param, local_var_params[param]))  # noqa: E501

    header_params = {}

    form_params = []
    local_var_files = {}

    body_params = None
    # HTTP header `Accept`
    header_params["Accept"] = api_client.select_header_accept(
        ["application/json"]
    )  # noqa: E501

    # Authentication setting
    auth_settings = ["basicAuth"]  # noqa: E501

    return api_client.call_api(
        "/status/system",
        "GET",
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type="object",  # noqa: E501
        auth_settings=auth_settings,
        async_req=local_var_params.get("async_req"),
        _return_http_data_only=local_var_params.get(
            "_return_http_data_only"
        ),  # noqa: E501
        _preload_content=local_var_params.get("_preload_content", True),
        _request_timeout=local_var_params.get("_request_timeout"),
        collection_formats=collection_formats,
    )


def get_task_status(api_client, token=None, **kwargs):  # noqa: E501
    """get_task_status  # noqa: E501

    Describe task status details  # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.get_task_status(body, async_req=True)

    :param async_req bool: execute request asynchronously
    :param token str: Task token to retrieve status for (required)
    :param _return_http_data_only: response data without head status code
                                    and headers
    :param _preload_content: if False, the urllib3.HTTPResponse object will
                                be returned without reading/decoding response
                                data. Default is True.
    :param _request_timeout: timeout setting for this request. If one
                                number provided, it will be total request
                                timeout. It can also be a pair (tuple) of
                                (connection, read) timeouts.
    :return: APIResponse or awaitable if async
    """

    local_var_params = locals()

    request_params = ["token"]  # noqa: E501

    collection_formats = {}

    path_params = {}

    query_params = []
    for param in [p for p in request_params if local_var_params.get(p) is not None]:
        query_params.append((param, local_var_params[param]))  # noqa: E501

    header_params = {}

    form_params = []
    local_var_files = {}

    body_params = {}

    # HTTP header `Accept`
    header_params["Accept"] = api_client.select_header_accept(
        ["application/json"]
    )  # noqa: E501

    # Authentication setting
    auth_settings = ["basicAuth"]  # noqa: E501

    return api_client.call_api(
        "/status/task",
        "GET",
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type="object",  # noqa: E501
        auth_settings=auth_settings,
        async_req=local_var_params.get("async_req"),
        _return_http_data_only=local_var_params.get(
            "_return_http_data_only"
        ),  # noqa: E501
        _preload_content=local_var_params.get("_preload_content", True),
        _request_timeout=local_var_params.get("_request_timeout"),
        collection_formats=collection_formats,
    )


def post_generate_keypair(api_client, body=None, **kwargs):  # noqa: E501
    """post_generate_keypair  # noqa: E501

    Generating a remote support key which can be shared with Cohesive to provide  access to the internal of the VNS3 Controller
    remotely as a \"one time key\".  Once Cohesive has used the key it can be revoked and access terminated.   # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.post_generate_keypair(client, body, async_req=True)

    :param async_req bool: execute request asynchronously
    :param passphrase_body str: Encrypted passphrase file which will be used to generate an X509 key for  accessing the VNS3 Controller
    in support mode. These are generated and owned by Cohesive.  Contact support@cohesive.net for an encrypted passphrase file.  (required)
    :param _return_http_data_only: response data without head status code
                                    and headers
    :param _preload_content: if False, the urllib3.HTTPResponse object will
                                be returned without reading/decoding response
                                data. Default is True.
    :param _request_timeout: timeout setting for this request. If one
                                number provided, it will be total request
                                timeout. It can also be a pair (tuple) of
                                (connection, read) timeouts.
    :return: APIResponse or awaitable if async
    """

    local_var_params = locals()

    collection_formats = {}

    path_params = {}

    query_params = []

    header_params = {}

    form_params = []
    local_var_files = {}

    body_params = body

    # HTTP header `Accept`
    header_params["Accept"] = api_client.select_header_accept(
        ["text/plain", "application/octet-stream"]
    )  # noqa: E501

    # HTTP header `Content-Type`
    header_params["Content-Type"] = api_client.select_header_content_type(  # noqa: E501
        ["text/plain"]
    )  # noqa: E501

    # Authentication setting
    auth_settings = ["basicAuth"]  # noqa: E501

    return api_client.call_api(
        "/remote_support/keypair",
        "POST",
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type="file",  # noqa: E501
        auth_settings=auth_settings,
        async_req=local_var_params.get("async_req"),
        _return_http_data_only=local_var_params.get(
            "_return_http_data_only"
        ),  # noqa: E501
        _preload_content=local_var_params.get("_preload_content", True),
        _request_timeout=local_var_params.get("_request_timeout"),
        collection_formats=collection_formats,
    )


def put_remote_support(
    api_client, enabled=None, revoke_credential=None, **kwargs
):  # noqa: E501
    """put_remote_support  # noqa: E501

    Enables and disables remote support. Revokes the validity of a remote support
    keypair generated with postGenerateKeypair   # noqa: E501

    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.put_remote_support(async_req=True)

    :param async_req bool: execute request asynchronously
    :param enabled bool: True if remote support should be enabled
    :param revoke_credential bool: True if remote support credential should be revoked
    :param _return_http_data_only: response data without head status code
                                    and headers
    :param _preload_content: if False, the urllib3.HTTPResponse object will
                                be returned without reading/decoding response
                                data. Default is True.
    :param _request_timeout: timeout setting for this request. If one
                                number provided, it will be total request
                                timeout. It can also be a pair (tuple) of
                                (connection, read) timeouts.
    :return: APIResponse or awaitable if async
    """

    local_var_params = locals()

    request_params = ["enabled", "revoke_credential"]

    collection_formats = {}

    path_params = {}

    query_params = []

    header_params = {}

    form_params = []

    local_var_files = {}

    body_params = {}
    for param in [p for p in request_params if local_var_params.get(p) is not None]:
        body_params[param] = local_var_params[param]

    # HTTP header `Accept`
    header_params["Accept"] = api_client.select_header_accept(
        ["application/json"]
    )  # noqa: E501

    # HTTP header `Content-Type`
    header_params["Content-Type"] = api_client.select_header_content_type(  # noqa: E501
        ["application/json"]
    )  # noqa: E501

    # Authentication setting
    auth_settings = ["basicAuth"]  # noqa: E501

    return api_client.call_api(
        "/remote_support",
        "PUT",
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type="object",  # noqa: E501
        auth_settings=auth_settings,
        async_req=local_var_params.get("async_req"),
        _return_http_data_only=local_var_params.get(
            "_return_http_data_only"
        ),  # noqa: E501
        _preload_content=local_var_params.get("_preload_content", True),
        _request_timeout=local_var_params.get("_request_timeout"),
        collection_formats=collection_formats,
    )


def put_server_action(api_client, reboot=True, **kwargs):  # noqa: E501
    """put_server_action  # noqa: E501

    Server action for VNS3 controller. Currently only reboot supported.  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> response = await api.put_server_action(async_req=True)

    :param async_req bool: execute request asynchronously
    :param reboot bool:
    :param _return_http_data_only: response data without head status code
                                    and headers
    :param _preload_content: if False, the urllib3.HTTPResponse object will
                                be returned without reading/decoding response
                                data. Default is True.
    :param _request_timeout: timeout setting for this request. If one
                                number provided, it will be total request
                                timeout. It can also be a pair (tuple) of
                                (connection, read) timeouts.
    :return: APIResponse or awaitable if async
    """

    local_var_params = locals()

    request_params = ["reboot"]

    collection_formats = {}

    path_params = {}

    query_params = []

    header_params = {}

    form_params = []

    local_var_files = {}

    body_params = {}
    for param in [p for p in request_params if local_var_params.get(p) is not None]:
        body_params[param] = local_var_params[param]

    # HTTP header `Accept`
    header_params["Accept"] = api_client.select_header_accept(
        ["application/json"]
    )  # noqa: E501

    # HTTP header `Content-Type`
    header_params["Content-Type"] = api_client.select_header_content_type(  # noqa: E501
        ["application/json"]
    )  # noqa: E501

    # Authentication setting
    auth_settings = ["basicAuth"]  # noqa: E501

    return api_client.call_api(
        "/server",
        "PUT",
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type="object",  # noqa: E501
        auth_settings=auth_settings,
        async_req=local_var_params.get("async_req"),
        _return_http_data_only=local_var_params.get(
            "_return_http_data_only"
        ),  # noqa: E501
        _preload_content=local_var_params.get("_preload_content", True),
        _request_timeout=local_var_params.get("_request_timeout"),
        collection_formats=collection_formats,
    )


def _wait_for_down(api_client, retry_timeout=2, timeout=30, sleep_time=0):
    import time

    start_time = time.time()

    while time.time() - start_time < timeout:
        try:
            config_api.get_config(api_client, _request_timeout=retry_timeout)
            if sleep_time:
                time.sleep(sleep_time)
        except (
            urllib3.exceptions.ConnectTimeoutError,
            urllib3.exceptions.NewConnectionError,
            urllib3.exceptions.MaxRetryError,
        ):
            return True
    raise ApiException("API failed to go down [timeout=%sseconds]" % timeout)


def wait_for_api(
    api_client,
    retry_timeout=2,
    timeout=60,
    wait_for_reboot=False,
    assert_config=None,
    healthy_ping_count=10,
    sleep_time=1.5,
    **kwargs
):  # noqa: E501
    """wait_for_api  # noqa: E501

    Wait for api availability. This method makes a synchronous HTTP request for API status
    :param _request_timeout: timeout setting for this request. If one
                                number provided, it will be total request
                                timeout. It can also be a pair (tuple) of
                                (connection, read) timeouts.
    :return: {}
    """
    import time

    start_time = time.time()

    if wait_for_reboot:
        _wait_for_down(api_client, sleep_time=1, timeout=timeout)

    successful_pings = 0
    target_host = api_client.host_uri
    while time.time() - start_time < timeout:
        try:
            config_detail = config_api.get_config(api_client, _request_timeout=retry_timeout)
            if (
                config_detail
                and config_detail.response
                and config_detail.response.vns3_version
            ):
                if not assert_config or (assert_config(config_detail.response)):
                    successful_pings = successful_pings + 1
                    if successful_pings >= healthy_ping_count:
                        return config_detail.response
        except (
            urllib3.exceptions.ConnectTimeoutError,
            urllib3.exceptions.NewConnectionError,
            urllib3.exceptions.MaxRetryError,
        ):
            Logger.debug(
                "API connection error on API ping. Retrying in %ds." % sleep_time,
                host=target_host,
            )
        except ApiException as e:
            if e.status == 502:
                time.sleep(sleep_time)
            else:
                raise e

        time.sleep(sleep_time)
    raise ApiException("API timeout [timeout=%sseconds]" % timeout)


class SystemAdministrationApiRouter(VersionRouter):
    function_library = {
        "get_cloud_data": {"4.8.4": get_cloud_data},
        "get_status": {"4.8.4": get_status},
        "get_task_status": {"4.8.4": get_task_status},
        "get_system_status": {"4.8.4": get_system_status},
        "post_generate_keypair": {"4.8.4": post_generate_keypair},
        "put_remote_support": {"4.8.4": put_remote_support},
        "put_server_action": {"4.8.4": put_server_action},
        "wait_for_api": {"4.8.4": wait_for_api},
    }
