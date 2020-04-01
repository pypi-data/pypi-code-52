# coding: utf-8

"""
    API Specification

    # Introduction Welcome to gridscales API documentation.  A REST API is a programming interface that allows you to access and send data directly to our systems using HTTPS requests, without the need to use a web GUI. All the functionality you are already familiar with in your control panel is accessible through the API, including expert methods that are only available through the API. Allowing you to script any actions you require, regardless of their complexity.  First we will start with a general overview about how the API works, followed by an extensive list of each endpoint, describing them in great detail.  ## Requests  For security, gridscale requires all API requests are made through the HTTPS protocol so that traffic is encrypted. The following table displays the different type of requests that the interface responds to, depending on the action you require.  | Method | Description | | --- | --- | | GET | A simple search of information. The response is a JSON object. Requests using GET are always read-only. | | POST | Adds new objects and object relations. The POST request must contain all the required parameters in the form of a JSON object. | | PATCH | Changes an object or an object relation. The parameters in PATCH requests are usually optional, so only the changed parameters must be specified in a JSON object. | | DELETE | Deletes an object or object relation. The object is deleted if it exists. | | OPTIONS | Get an extensive list of the servers support methods and characteristics. We will not give example OPTION requests on each endpoint, as they are extensive and self-descriptive. |  <aside class=\"notice\"> The methods PATCH and DELETE are idempotent - that is, a request with identical parameters can be sent several times, and it doesn't change the result. </aside>  ## Status Codes  | HTTP Status | `Message` | Description | | --- | --- | --- | | 200 | `OK` | The request has been successfully processed and the result of the request is transmitted in the response. | | 202 | `Accepted` | The request has been accepted, but will run at a later date. Meaning we can not guarantee the success of the request. You should poll the request to be notified once the resource has been provisioned - see the requests endpoint on how to poll. | | 204 | `No Content` | The request was successful, but the answer deliberately contains no data. | | 400 | `Bad Request` | The request message was built incorrectly. | | 401 | `Unauthorised` | The request can not be performed without a valid authentication. X-Auth UserId or X-Auth token HTTP header is not set or the userID / token is invalid. | | 402 | `Payment Required` | Action can not be executed - not provided any or invalid payment methods. | | 403 | `Forbidden` | The request was not carried out due to lack of authorization of the user or because an impossible action was requested. | | 404 | `Not Found` | The requested resource was not found. Will also be used if you do a resource exists, but the user does not have permission for it. | | 405 | `Method Not Allowed` | The request may be made only with other HTTP methods (eg GET rather than POST). | | 409 | `Conflict` | The request was made under false assumptions. For example, a user can not be created twice with the same email. | | 415 | `Unsupported Media Type` | The contents of the request have been submitted with an invalid media type. All POST or PATCH requests must have \"Content-Type : application / json\" as a header, and send a JSON object as a payload. | | 424 | `Failed Dependency` | The request could not be performed because the object is in the wrong status. |  <aside class=\"success\"> Status 200-204 indicates that the request has been accepted and is processed. </aside> <aside class=\"notice\"> Status 400-424 indicates that there was a problem with the request. For more information about the problem you'll find in the body of 4xx response. </aside> <aside class=\"warning\"> A status 500 means that there was a server-side problem and your request can not be processed now. </aside>  ## Request Headers  | Header | Description | | --- | --- | | Content-Type | Always \"application/json\". | | X-Auth-userId | The user UUID. This can be found in the panel under \"API\" and will never change ( even after the change of user e-mail). | | X-Auth-Token | Is generated from the API hash and must be sent with all API requests. Both the token and its permissions can be configured in the panel.|  ## Response Headers  | Header | Description | | --- | --- | | Content-Type | Always \"application/json\". | | X-Exec-Time | The time taken to process the request (in ms). | | X-Api-Version | The currently active Provisioning API version. Useful when reporting bugs to us. | | X-Request-Id  | The unique identifier of the request, be sure to include it when referring to a request. |  ## Timestamp Format  All timestamps follow <a href=\"https://de.wikipedia.org/wiki/ISO_8601\" target=\"_blank_\">ISO 8601</a> and issued in <a href=\"https://www.timeanddate.de/zeitzonen/utc-gmt\" target=\"_blank_\">UTC</a>  ## CORS  ### Cross Origin Resource Sharing  To allow API access from other domains that supports the API CORS (Cross Origin Resource Sharing). See: enable-cors.org/ .  This allows direct use the API in the browser running a JavaScript web control panel.  All this is done in the background by the browser. The following HTTP headers are set by the API:  Header | Parameter | Description --- | --- | --- Access-Control-Allow-Methods   | GET, POST, PUT, PATCH, DELETE, OPTIONS | Contains all available methods that may be used for queries. Access-Control-Allow-Credentials | true | Is set to \"true\". Allows the browser to send the authentication data via X-Auth HTTP header. Access-Control-Allow-Headers | Origin, X-Requested-With, Content-Type, Accept, X-Auth-UserId, X-Auth-Token, X-Exec-Time, X-API-Version, X-Api-Client | The HTTP headers available for requests. Access-Control-Allow-Origin | * | The domain sent by the browser as a source of demand. Access-Control-Expose-Headers | X-Exec-Time, X-Api-Version | The HTTP headers that can be used by a browser application.  ## Object Relations Relationships describe resource objects (storages, networks, IPs, etc.) that are connected to a server. These relationships are treated like objects themselves and can have properties specific to this relation.  One example would be, that the MAC address of a private network connected to a server (Server-to-Network relation) can be found as property of the relation itself - the relation is the _network interface_ in the server.  Another example is storage, where the SCSI LUN is also part of the Server-to-Storage relation object.  This information is especially interesting if some kind of network boot is used on the servers, where the properties of the server need to be known beforehand.  ## Deleted Objects Objects that are deleted are no longer visible on their *regular* endpoints. For historical reasons these objects are still available read-only on a special endpoint named /deleted. If objects have been deleted but have not yet been billed in the current period, the yet-to-be-billed price is still shown.  <!-- #strip_js --> ## Node.js Library  We have a JavaScript library for you to use our API with ease.  <a href=\"https://www.npmjs.com/package/@gridscale/api\" target=\"_blank\"><img src=\"https://badge.fury.io/js/%40gridscale%2Fapi.svg\" alt=\"npm badge\"></a>  <aside class=\"success\"> We want to make it even easier for you to manage your Infrastructure via our API - so feel free to contact us with any ideas, or languages you would like to see included. </aside>  Requests with our Node.js lib return a little differently. Everything is the same except it allows you to add URL parameters to customize your requests.  To get started <a href=\"https://www.npmjs.com/package/@gridscale/api\" target=\"_blank\">click here</a> .  <!-- #strip_js_end -->  <!-- #strip_go --> ## Golang Library We also have a Golang library for Gophers.  Requests with our Golang lib return a little differently. Everything is the same except it allows you to add URL parameters to customize your requests.  To get started <a href=\"https://github.com/gridscale/gsclient-go\" target=\"_blank\">click here</a> .  <!-- #strip_go_end -->  # Authentication  In order to use the API, the User-UUID and an API_Token are required. Both are available via the web GUI which can be found here on <a href=\"https://my.gridscale.io/APIs/\" target=\"_blank\">Your Account</a>  <aside class=\"success\"> If your are logged in, your UUID and Token will be pulled dynamically from your account, so you can copy request examples straight into your code. </aside>  The User-UUID remains the same, even if the users email address is changed. The API_Token is a randomly generated hash that allows read/write access.  ## API_Token  <table class=\"security-details\"><tbody><tr><th> Security scheme type: </th><td> API Key </td></tr><tr><th> header parameter name:</th><td> X-Auth-Token </td></tr></tbody></table>  ## User_UUID  <table class=\"security-details\"><tbody><tr><th> Security scheme type: </th><td> API Key </td></tr><tr><th> header parameter name:</th><td> X-Auth-UserId </td></tr></tbody></table>  ## Examples  <!-- #strip_js --> > Node.js ``` // to get started // read the docs @ https://www.npmjs.com/package/@gs_js_auth/api var gs_js_auth = require('@gs_js_auth/api').gs_js_auth; var client = new gs_js_auth.Client(\"##API_TOKEN##\",\"##USER_UUID##\"); ``` <!-- #strip_js_end -->  <!-- #strip_go --> > Golang ``` // to get started // read the docs @ https://github.com/gridscale/gsclient-go config := gsclient.NewConfiguration(   \"https://api.gridscale.io\",   \"##USER_UUID##\",   \"##API_TOKEN##\",   false, //set debug mode ) client := gsclient.NewClient(config) ``` <!-- #strip_go_end -->  > Shell Authentication Headers ```   -H \"X-Auth-UserId: ##USER_UUID##\" \\   -H \"X-Auth-Token: ##API_TOKEN##\" \\ ```  > Setting Authentication in your Environment variables ``` export API_TOKEN=\"##API_TOKEN##\" USER_UUID=\"##USER_UUID##\" ```  <aside class=\"notice\"> You must replace <code>USER_UUID</code> and <code>API_Token</code> with your personal UUID and API key respectively. </aside>   # noqa: E501

    OpenAPI spec version: 1.0.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from gs_api_client.swagger.models.task_events_firewall import TaskEventsFirewall  # noqa: F401,E501
from gs_api_client.swagger.models.task_events_ipaddr import TaskEventsIpaddr  # noqa: F401,E501
from gs_api_client.swagger.models.task_events_isoimage import TaskEventsIsoimage  # noqa: F401,E501
from gs_api_client.swagger.models.task_events_loadbalancer import TaskEventsLoadbalancer  # noqa: F401,E501
from gs_api_client.swagger.models.task_events_marketplace_template import TaskEventsMarketplaceTemplate  # noqa: F401,E501
from gs_api_client.swagger.models.task_events_network import TaskEventsNetwork  # noqa: F401,E501
from gs_api_client.swagger.models.task_events_paas import TaskEventsPaas  # noqa: F401,E501
from gs_api_client.swagger.models.task_events_schedules import TaskEventsSchedules  # noqa: F401,E501
from gs_api_client.swagger.models.task_events_server import TaskEventsServer  # noqa: F401,E501
from gs_api_client.swagger.models.task_events_snapshot import TaskEventsSnapshot  # noqa: F401,E501
from gs_api_client.swagger.models.task_events_sshkey import TaskEventsSshkey  # noqa: F401,E501
from gs_api_client.swagger.models.task_events_storage import TaskEventsStorage  # noqa: F401,E501
from gs_api_client.swagger.models.task_events_template import TaskEventsTemplate  # noqa: F401,E501


class TaskEvents(object):
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
        'schedules': 'TaskEventsSchedules',
        'ipaddr': 'TaskEventsIpaddr',
        'loadbalancer': 'TaskEventsLoadbalancer',
        'paas': 'TaskEventsPaas',
        'marketplace_template': 'TaskEventsMarketplaceTemplate',
        'firewall': 'TaskEventsFirewall',
        'isoimage': 'TaskEventsIsoimage',
        'snapshot': 'TaskEventsSnapshot',
        'sshkey': 'TaskEventsSshkey',
        'storage': 'TaskEventsStorage',
        'server': 'TaskEventsServer',
        'template': 'TaskEventsTemplate',
        'network': 'TaskEventsNetwork'
    }

    attribute_map = {
        'schedules': 'schedules',
        'ipaddr': 'ipaddr',
        'loadbalancer': 'loadbalancer',
        'paas': 'paas',
        'marketplace_template': 'marketplace_template',
        'firewall': 'firewall',
        'isoimage': 'isoimage',
        'snapshot': 'snapshot',
        'sshkey': 'sshkey',
        'storage': 'storage',
        'server': 'server',
        'template': 'template',
        'network': 'network'
    }

    def __init__(self, schedules=None, ipaddr=None, loadbalancer=None, paas=None, marketplace_template=None, firewall=None, isoimage=None, snapshot=None, sshkey=None, storage=None, server=None, template=None, network=None):  # noqa: E501
        """TaskEvents - a model defined in Swagger"""  # noqa: E501

        self._schedules = None
        self._ipaddr = None
        self._loadbalancer = None
        self._paas = None
        self._marketplace_template = None
        self._firewall = None
        self._isoimage = None
        self._snapshot = None
        self._sshkey = None
        self._storage = None
        self._server = None
        self._template = None
        self._network = None
        self.discriminator = None

        if schedules is not None:
            self.schedules = schedules
        if ipaddr is not None:
            self.ipaddr = ipaddr
        if loadbalancer is not None:
            self.loadbalancer = loadbalancer
        if paas is not None:
            self.paas = paas
        if marketplace_template is not None:
            self.marketplace_template = marketplace_template
        if firewall is not None:
            self.firewall = firewall
        if isoimage is not None:
            self.isoimage = isoimage
        if snapshot is not None:
            self.snapshot = snapshot
        if sshkey is not None:
            self.sshkey = sshkey
        if storage is not None:
            self.storage = storage
        if server is not None:
            self.server = server
        if template is not None:
            self.template = template
        if network is not None:
            self.network = network

    @property
    def schedules(self):
        """Gets the schedules of this TaskEvents.  # noqa: E501


        :return: The schedules of this TaskEvents.  # noqa: E501
        :rtype: TaskEventsSchedules
        """
        return self._schedules

    @schedules.setter
    def schedules(self, schedules):
        """Sets the schedules of this TaskEvents.


        :param schedules: The schedules of this TaskEvents.  # noqa: E501
        :type: TaskEventsSchedules
        """

        self._schedules = schedules

    @property
    def ipaddr(self):
        """Gets the ipaddr of this TaskEvents.  # noqa: E501


        :return: The ipaddr of this TaskEvents.  # noqa: E501
        :rtype: TaskEventsIpaddr
        """
        return self._ipaddr

    @ipaddr.setter
    def ipaddr(self, ipaddr):
        """Sets the ipaddr of this TaskEvents.


        :param ipaddr: The ipaddr of this TaskEvents.  # noqa: E501
        :type: TaskEventsIpaddr
        """

        self._ipaddr = ipaddr

    @property
    def loadbalancer(self):
        """Gets the loadbalancer of this TaskEvents.  # noqa: E501


        :return: The loadbalancer of this TaskEvents.  # noqa: E501
        :rtype: TaskEventsLoadbalancer
        """
        return self._loadbalancer

    @loadbalancer.setter
    def loadbalancer(self, loadbalancer):
        """Sets the loadbalancer of this TaskEvents.


        :param loadbalancer: The loadbalancer of this TaskEvents.  # noqa: E501
        :type: TaskEventsLoadbalancer
        """

        self._loadbalancer = loadbalancer

    @property
    def paas(self):
        """Gets the paas of this TaskEvents.  # noqa: E501


        :return: The paas of this TaskEvents.  # noqa: E501
        :rtype: TaskEventsPaas
        """
        return self._paas

    @paas.setter
    def paas(self, paas):
        """Sets the paas of this TaskEvents.


        :param paas: The paas of this TaskEvents.  # noqa: E501
        :type: TaskEventsPaas
        """

        self._paas = paas

    @property
    def marketplace_template(self):
        """Gets the marketplace_template of this TaskEvents.  # noqa: E501


        :return: The marketplace_template of this TaskEvents.  # noqa: E501
        :rtype: TaskEventsMarketplaceTemplate
        """
        return self._marketplace_template

    @marketplace_template.setter
    def marketplace_template(self, marketplace_template):
        """Sets the marketplace_template of this TaskEvents.


        :param marketplace_template: The marketplace_template of this TaskEvents.  # noqa: E501
        :type: TaskEventsMarketplaceTemplate
        """

        self._marketplace_template = marketplace_template

    @property
    def firewall(self):
        """Gets the firewall of this TaskEvents.  # noqa: E501


        :return: The firewall of this TaskEvents.  # noqa: E501
        :rtype: TaskEventsFirewall
        """
        return self._firewall

    @firewall.setter
    def firewall(self, firewall):
        """Sets the firewall of this TaskEvents.


        :param firewall: The firewall of this TaskEvents.  # noqa: E501
        :type: TaskEventsFirewall
        """

        self._firewall = firewall

    @property
    def isoimage(self):
        """Gets the isoimage of this TaskEvents.  # noqa: E501


        :return: The isoimage of this TaskEvents.  # noqa: E501
        :rtype: TaskEventsIsoimage
        """
        return self._isoimage

    @isoimage.setter
    def isoimage(self, isoimage):
        """Sets the isoimage of this TaskEvents.


        :param isoimage: The isoimage of this TaskEvents.  # noqa: E501
        :type: TaskEventsIsoimage
        """

        self._isoimage = isoimage

    @property
    def snapshot(self):
        """Gets the snapshot of this TaskEvents.  # noqa: E501


        :return: The snapshot of this TaskEvents.  # noqa: E501
        :rtype: TaskEventsSnapshot
        """
        return self._snapshot

    @snapshot.setter
    def snapshot(self, snapshot):
        """Sets the snapshot of this TaskEvents.


        :param snapshot: The snapshot of this TaskEvents.  # noqa: E501
        :type: TaskEventsSnapshot
        """

        self._snapshot = snapshot

    @property
    def sshkey(self):
        """Gets the sshkey of this TaskEvents.  # noqa: E501


        :return: The sshkey of this TaskEvents.  # noqa: E501
        :rtype: TaskEventsSshkey
        """
        return self._sshkey

    @sshkey.setter
    def sshkey(self, sshkey):
        """Sets the sshkey of this TaskEvents.


        :param sshkey: The sshkey of this TaskEvents.  # noqa: E501
        :type: TaskEventsSshkey
        """

        self._sshkey = sshkey

    @property
    def storage(self):
        """Gets the storage of this TaskEvents.  # noqa: E501


        :return: The storage of this TaskEvents.  # noqa: E501
        :rtype: TaskEventsStorage
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this TaskEvents.


        :param storage: The storage of this TaskEvents.  # noqa: E501
        :type: TaskEventsStorage
        """

        self._storage = storage

    @property
    def server(self):
        """Gets the server of this TaskEvents.  # noqa: E501


        :return: The server of this TaskEvents.  # noqa: E501
        :rtype: TaskEventsServer
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this TaskEvents.


        :param server: The server of this TaskEvents.  # noqa: E501
        :type: TaskEventsServer
        """

        self._server = server

    @property
    def template(self):
        """Gets the template of this TaskEvents.  # noqa: E501


        :return: The template of this TaskEvents.  # noqa: E501
        :rtype: TaskEventsTemplate
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this TaskEvents.


        :param template: The template of this TaskEvents.  # noqa: E501
        :type: TaskEventsTemplate
        """

        self._template = template

    @property
    def network(self):
        """Gets the network of this TaskEvents.  # noqa: E501


        :return: The network of this TaskEvents.  # noqa: E501
        :rtype: TaskEventsNetwork
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this TaskEvents.


        :param network: The network of this TaskEvents.  # noqa: E501
        :type: TaskEventsNetwork
        """

        self._network = network

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
        if issubclass(TaskEvents, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TaskEvents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
