# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class AuthConfigOpenLdap(pulumi.CustomResource):
    access_mode: pulumi.Output[str]
    """
    Access mode for auth. `required`, `restricted`, `unrestricted` are supported. Default `unrestricted` (string)
    """
    allowed_principal_ids: pulumi.Output[list]
    """
    Allowed principal ids for auth. Required if `access_mode` is `required` or `restricted`. Ex: `openldap_user://<DN>`  `openldap_group://<DN>` (list)
    """
    annotations: pulumi.Output[dict]
    """
    Annotations of the resource (map)
    """
    certificate: pulumi.Output[str]
    """
    Base64 encoded CA certificate for TLS if self-signed. Use filebase64(<FILE>) for encoding file (string)
    """
    connection_timeout: pulumi.Output[float]
    """
    OpenLdap connection timeout. Default `5000` (int)
    """
    enabled: pulumi.Output[bool]
    """
    Enable auth config provider. Default `true` (bool)
    """
    group_dn_attribute: pulumi.Output[str]
    """
    Group DN attribute. Default `entryDN` (string)
    """
    group_member_mapping_attribute: pulumi.Output[str]
    """
    Group member mapping attribute. Default `member` (string)
    """
    group_member_user_attribute: pulumi.Output[str]
    """
    Group member user attribute. Default `entryDN` (string)
    """
    group_name_attribute: pulumi.Output[str]
    """
    Group name attribute. Default `cn` (string)
    """
    group_object_class: pulumi.Output[str]
    """
    Group object class. Default `groupOfNames` (string)
    """
    group_search_attribute: pulumi.Output[str]
    """
    Group search attribute. Default `cn` (string)
    """
    group_search_base: pulumi.Output[str]
    """
    Group search base (string)
    """
    labels: pulumi.Output[dict]
    """
    Labels of the resource (map)
    """
    name: pulumi.Output[str]
    """
    (Computed) The name of the resource (string)
    """
    nested_group_membership_enabled: pulumi.Output[bool]
    """
    Nested group membership enable. Default `false` (bool)
    """
    port: pulumi.Output[float]
    """
    OpenLdap port. Default `389` (int)
    """
    servers: pulumi.Output[list]
    """
    OpenLdap servers list (list)
    """
    service_account_distinguished_name: pulumi.Output[str]
    """
    Service account DN for access OpenLdap service (string)
    """
    service_account_password: pulumi.Output[str]
    """
    Service account password for access OpenLdap service (string)
    """
    tls: pulumi.Output[bool]
    """
    Enable TLS connection (bool)
    """
    type: pulumi.Output[str]
    """
    (Computed) The type of the resource (string)
    """
    user_disabled_bit_mask: pulumi.Output[float]
    """
    User disabled bit mask (int)
    """
    user_enabled_attribute: pulumi.Output[str]
    """
    User enable attribute (string)
    """
    user_login_attribute: pulumi.Output[str]
    """
    User login attribute. Default `uid` (string)
    """
    user_member_attribute: pulumi.Output[str]
    """
    User member attribute. Default `memberOf` (string)
    """
    user_name_attribute: pulumi.Output[str]
    """
    User name attribute. Default `givenName` (string)
    """
    user_object_class: pulumi.Output[str]
    """
    User object class. Default `inetorgperson` (string)
    """
    user_search_attribute: pulumi.Output[str]
    """
    User search attribute. Default `uid|sn|givenName` (string)
    """
    user_search_base: pulumi.Output[str]
    """
    User search base DN (string)
    """
    def __init__(__self__, resource_name, opts=None, access_mode=None, allowed_principal_ids=None, annotations=None, certificate=None, connection_timeout=None, enabled=None, group_dn_attribute=None, group_member_mapping_attribute=None, group_member_user_attribute=None, group_name_attribute=None, group_object_class=None, group_search_attribute=None, group_search_base=None, labels=None, nested_group_membership_enabled=None, port=None, servers=None, service_account_distinguished_name=None, service_account_password=None, tls=None, user_disabled_bit_mask=None, user_enabled_attribute=None, user_login_attribute=None, user_member_attribute=None, user_name_attribute=None, user_object_class=None, user_search_attribute=None, user_search_base=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a Rancher v2 Auth Config OpenLdap resource. This can be used to configure and enable Auth Config OpenLdap for Rancher v2 RKE clusters and retrieve their information.

        In addition to the built-in local auth, only one external auth config provider can be enabled at a time.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-rancher2/blob/master/website/docs/r/authConfigOpenLdap.html.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_mode: Access mode for auth. `required`, `restricted`, `unrestricted` are supported. Default `unrestricted` (string)
        :param pulumi.Input[list] allowed_principal_ids: Allowed principal ids for auth. Required if `access_mode` is `required` or `restricted`. Ex: `openldap_user://<DN>`  `openldap_group://<DN>` (list)
        :param pulumi.Input[dict] annotations: Annotations of the resource (map)
        :param pulumi.Input[str] certificate: Base64 encoded CA certificate for TLS if self-signed. Use filebase64(<FILE>) for encoding file (string)
        :param pulumi.Input[float] connection_timeout: OpenLdap connection timeout. Default `5000` (int)
        :param pulumi.Input[bool] enabled: Enable auth config provider. Default `true` (bool)
        :param pulumi.Input[str] group_dn_attribute: Group DN attribute. Default `entryDN` (string)
        :param pulumi.Input[str] group_member_mapping_attribute: Group member mapping attribute. Default `member` (string)
        :param pulumi.Input[str] group_member_user_attribute: Group member user attribute. Default `entryDN` (string)
        :param pulumi.Input[str] group_name_attribute: Group name attribute. Default `cn` (string)
        :param pulumi.Input[str] group_object_class: Group object class. Default `groupOfNames` (string)
        :param pulumi.Input[str] group_search_attribute: Group search attribute. Default `cn` (string)
        :param pulumi.Input[str] group_search_base: Group search base (string)
        :param pulumi.Input[dict] labels: Labels of the resource (map)
        :param pulumi.Input[bool] nested_group_membership_enabled: Nested group membership enable. Default `false` (bool)
        :param pulumi.Input[float] port: OpenLdap port. Default `389` (int)
        :param pulumi.Input[list] servers: OpenLdap servers list (list)
        :param pulumi.Input[str] service_account_distinguished_name: Service account DN for access OpenLdap service (string)
        :param pulumi.Input[str] service_account_password: Service account password for access OpenLdap service (string)
        :param pulumi.Input[bool] tls: Enable TLS connection (bool)
        :param pulumi.Input[float] user_disabled_bit_mask: User disabled bit mask (int)
        :param pulumi.Input[str] user_enabled_attribute: User enable attribute (string)
        :param pulumi.Input[str] user_login_attribute: User login attribute. Default `uid` (string)
        :param pulumi.Input[str] user_member_attribute: User member attribute. Default `memberOf` (string)
        :param pulumi.Input[str] user_name_attribute: User name attribute. Default `givenName` (string)
        :param pulumi.Input[str] user_object_class: User object class. Default `inetorgperson` (string)
        :param pulumi.Input[str] user_search_attribute: User search attribute. Default `uid|sn|givenName` (string)
        :param pulumi.Input[str] user_search_base: User search base DN (string)
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['access_mode'] = access_mode
            __props__['allowed_principal_ids'] = allowed_principal_ids
            __props__['annotations'] = annotations
            __props__['certificate'] = certificate
            __props__['connection_timeout'] = connection_timeout
            __props__['enabled'] = enabled
            __props__['group_dn_attribute'] = group_dn_attribute
            __props__['group_member_mapping_attribute'] = group_member_mapping_attribute
            __props__['group_member_user_attribute'] = group_member_user_attribute
            __props__['group_name_attribute'] = group_name_attribute
            __props__['group_object_class'] = group_object_class
            __props__['group_search_attribute'] = group_search_attribute
            __props__['group_search_base'] = group_search_base
            __props__['labels'] = labels
            __props__['nested_group_membership_enabled'] = nested_group_membership_enabled
            __props__['port'] = port
            if servers is None:
                raise TypeError("Missing required property 'servers'")
            __props__['servers'] = servers
            if service_account_distinguished_name is None:
                raise TypeError("Missing required property 'service_account_distinguished_name'")
            __props__['service_account_distinguished_name'] = service_account_distinguished_name
            if service_account_password is None:
                raise TypeError("Missing required property 'service_account_password'")
            __props__['service_account_password'] = service_account_password
            __props__['tls'] = tls
            __props__['user_disabled_bit_mask'] = user_disabled_bit_mask
            __props__['user_enabled_attribute'] = user_enabled_attribute
            __props__['user_login_attribute'] = user_login_attribute
            __props__['user_member_attribute'] = user_member_attribute
            __props__['user_name_attribute'] = user_name_attribute
            __props__['user_object_class'] = user_object_class
            __props__['user_search_attribute'] = user_search_attribute
            if user_search_base is None:
                raise TypeError("Missing required property 'user_search_base'")
            __props__['user_search_base'] = user_search_base
            __props__['name'] = None
            __props__['type'] = None
        super(AuthConfigOpenLdap, __self__).__init__(
            'rancher2:index/authConfigOpenLdap:AuthConfigOpenLdap',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, access_mode=None, allowed_principal_ids=None, annotations=None, certificate=None, connection_timeout=None, enabled=None, group_dn_attribute=None, group_member_mapping_attribute=None, group_member_user_attribute=None, group_name_attribute=None, group_object_class=None, group_search_attribute=None, group_search_base=None, labels=None, name=None, nested_group_membership_enabled=None, port=None, servers=None, service_account_distinguished_name=None, service_account_password=None, tls=None, type=None, user_disabled_bit_mask=None, user_enabled_attribute=None, user_login_attribute=None, user_member_attribute=None, user_name_attribute=None, user_object_class=None, user_search_attribute=None, user_search_base=None):
        """
        Get an existing AuthConfigOpenLdap resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_mode: Access mode for auth. `required`, `restricted`, `unrestricted` are supported. Default `unrestricted` (string)
        :param pulumi.Input[list] allowed_principal_ids: Allowed principal ids for auth. Required if `access_mode` is `required` or `restricted`. Ex: `openldap_user://<DN>`  `openldap_group://<DN>` (list)
        :param pulumi.Input[dict] annotations: Annotations of the resource (map)
        :param pulumi.Input[str] certificate: Base64 encoded CA certificate for TLS if self-signed. Use filebase64(<FILE>) for encoding file (string)
        :param pulumi.Input[float] connection_timeout: OpenLdap connection timeout. Default `5000` (int)
        :param pulumi.Input[bool] enabled: Enable auth config provider. Default `true` (bool)
        :param pulumi.Input[str] group_dn_attribute: Group DN attribute. Default `entryDN` (string)
        :param pulumi.Input[str] group_member_mapping_attribute: Group member mapping attribute. Default `member` (string)
        :param pulumi.Input[str] group_member_user_attribute: Group member user attribute. Default `entryDN` (string)
        :param pulumi.Input[str] group_name_attribute: Group name attribute. Default `cn` (string)
        :param pulumi.Input[str] group_object_class: Group object class. Default `groupOfNames` (string)
        :param pulumi.Input[str] group_search_attribute: Group search attribute. Default `cn` (string)
        :param pulumi.Input[str] group_search_base: Group search base (string)
        :param pulumi.Input[dict] labels: Labels of the resource (map)
        :param pulumi.Input[str] name: (Computed) The name of the resource (string)
        :param pulumi.Input[bool] nested_group_membership_enabled: Nested group membership enable. Default `false` (bool)
        :param pulumi.Input[float] port: OpenLdap port. Default `389` (int)
        :param pulumi.Input[list] servers: OpenLdap servers list (list)
        :param pulumi.Input[str] service_account_distinguished_name: Service account DN for access OpenLdap service (string)
        :param pulumi.Input[str] service_account_password: Service account password for access OpenLdap service (string)
        :param pulumi.Input[bool] tls: Enable TLS connection (bool)
        :param pulumi.Input[str] type: (Computed) The type of the resource (string)
        :param pulumi.Input[float] user_disabled_bit_mask: User disabled bit mask (int)
        :param pulumi.Input[str] user_enabled_attribute: User enable attribute (string)
        :param pulumi.Input[str] user_login_attribute: User login attribute. Default `uid` (string)
        :param pulumi.Input[str] user_member_attribute: User member attribute. Default `memberOf` (string)
        :param pulumi.Input[str] user_name_attribute: User name attribute. Default `givenName` (string)
        :param pulumi.Input[str] user_object_class: User object class. Default `inetorgperson` (string)
        :param pulumi.Input[str] user_search_attribute: User search attribute. Default `uid|sn|givenName` (string)
        :param pulumi.Input[str] user_search_base: User search base DN (string)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["access_mode"] = access_mode
        __props__["allowed_principal_ids"] = allowed_principal_ids
        __props__["annotations"] = annotations
        __props__["certificate"] = certificate
        __props__["connection_timeout"] = connection_timeout
        __props__["enabled"] = enabled
        __props__["group_dn_attribute"] = group_dn_attribute
        __props__["group_member_mapping_attribute"] = group_member_mapping_attribute
        __props__["group_member_user_attribute"] = group_member_user_attribute
        __props__["group_name_attribute"] = group_name_attribute
        __props__["group_object_class"] = group_object_class
        __props__["group_search_attribute"] = group_search_attribute
        __props__["group_search_base"] = group_search_base
        __props__["labels"] = labels
        __props__["name"] = name
        __props__["nested_group_membership_enabled"] = nested_group_membership_enabled
        __props__["port"] = port
        __props__["servers"] = servers
        __props__["service_account_distinguished_name"] = service_account_distinguished_name
        __props__["service_account_password"] = service_account_password
        __props__["tls"] = tls
        __props__["type"] = type
        __props__["user_disabled_bit_mask"] = user_disabled_bit_mask
        __props__["user_enabled_attribute"] = user_enabled_attribute
        __props__["user_login_attribute"] = user_login_attribute
        __props__["user_member_attribute"] = user_member_attribute
        __props__["user_name_attribute"] = user_name_attribute
        __props__["user_object_class"] = user_object_class
        __props__["user_search_attribute"] = user_search_attribute
        __props__["user_search_base"] = user_search_base
        return AuthConfigOpenLdap(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

