# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals


# pylint: disable=line-too-long
def load_arguments_eh(self, _):
    from azure.cli.core.commands.parameters import tags_type, get_enum_type, resource_group_name_type, name_type, \
        get_location_type, get_three_state_flag, get_resource_name_completion_list
    from azure.cli.core.commands.validators import get_default_location_from_resource_group
    from azure.cli.command_modules.eventhubs._completers import get_consumergroup_command_completion_list, \
        get_eventhubs_command_completion_list
    from azure.cli.command_modules.eventhubs._validator import validate_storageaccount, validate_partner_namespace, validate_rights
    from knack.arguments import CLIArgumentType
    from azure.cli.core.profiles import ResourceType
    (KeyType, AccessRights, SkuName) = self.get_models('KeyType', 'AccessRights', 'SkuName', resource_type=ResourceType.MGMT_EVENTHUB)

    rights_arg_type = CLIArgumentType(options_list=['--rights'], nargs='+', arg_type=get_enum_type(AccessRights), validator=validate_rights, help='Space-separated list of Authorization rule rights')
    key_arg_type = CLIArgumentType(options_list=['--key'], arg_type=get_enum_type(KeyType), help='specifies Primary or Secondary key needs to be reset')
    keyvalue_arg_type = CLIArgumentType(options_list=['--key-value'], help='Optional, if the key value provided, is set for KeyType or autogenerated Key value set for keyType.')
    event_hub_name_arg_type = CLIArgumentType(options_list=['--eventhub-name'], help='Name of EventHub')
    namespace_name_arg_type = CLIArgumentType(options_list=['--namespace-name'], help='Name of Namespace', id_part='name')

    with self.argument_context('eventhubs') as c:
        c.argument('resource_group_name', arg_type=resource_group_name_type)
        c.argument('namespace_name', id_part='name', help='name of Namespace')

    with self.argument_context('eventhubs namespace exists') as c:
        c.argument('namespace_name', arg_type=name_type, help='Namespace name. Name can contain only letters, numbers, and hyphens. The namespace must start with a letter, and it must end with a letter or number.')

    with self.argument_context('eventhubs namespace') as c:
        c.argument('namespace_name', arg_type=name_type, id_part='name', completer=get_resource_name_completion_list('Microsoft.ServiceBus/namespaces'), help='Name of Namespace')
        c.argument('is_kafka_enabled', options_list=['--enable-kafka'], arg_type=get_three_state_flag(),
                   help='A boolean value that indicates whether Kafka is enabled for eventhub namespace.')
        c.argument('tags', arg_type=tags_type)
        c.argument('sku', options_list=['--sku'], arg_type=get_enum_type(SkuName), help='Namespace SKU.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx), validator=get_default_location_from_resource_group)
        c.argument('capacity', type=int, help='Capacity for Sku')
        c.argument('is_auto_inflate_enabled', options_list=['--enable-auto-inflate'], arg_type=get_three_state_flag(), help='A boolean value that indicates whether AutoInflate is enabled for eventhub namespace.')
        c.argument('maximum_throughput_units', type=int, help='Upper limit of throughput units when AutoInflate is enabled, vaule should be within 0 to 20 throughput units. ( 0 if AutoInflateEnabled = true)')
        c.argument('default_action', arg_group='networkrule', options_list=['--default-action'], arg_type=get_enum_type(['Allow', 'Deny']),
                   help='Default Action for Network Rule Set.')

    # region Namespace Authorizationrule
    with self.argument_context('eventhubs namespace authorization-rule list') as c:
        c.argument('namespace_name', options_list=['--namespace-name'], id_part=None, help='Name of Namespace')

    with self.argument_context('eventhubs namespace authorization-rule keys list') as c:
        c.argument('authorization_rule_name', arg_type=name_type, id_part=None, help='Name of Namespace AuthorizationRule')
        c.argument('namespace_name', options_list=['--namespace-name'], id_part=None, help='Name of Namespace')

    for scope in ['eventhubs namespace authorization-rule', 'eventhubs namespace authorization-rule keys renew']:
        with self.argument_context(scope) as c:
            c.argument('authorization_rule_name', arg_type=name_type, id_part='child_name_1', help='Name of Namespace AuthorizationRule')
            c.argument('namespace_name', arg_type=namespace_name_arg_type)

    for scope in ['eventhubs namespace authorization-rule create', 'eventhubs namespace authorization-rule update', 'eventhubs eventhub authorization-rule create', 'eventhubs eventhub authorization-rule update']:
        with self.argument_context(scope) as c:
            c.argument('rights', arg_type=rights_arg_type)

    with self.argument_context('eventhubs namespace authorization-rule keys renew') as c:
        c.argument('key_type', arg_type=key_arg_type)
        c.argument('key', arg_type=keyvalue_arg_type)

# region - Eventhub Create
    with self.argument_context('eventhubs eventhub') as c:
        c.argument('event_hub_name', arg_type=name_type, id_part='child_name_1', completer=get_eventhubs_command_completion_list, help='Name of Eventhub')

    for scope in ['eventhubs eventhub update', 'eventhubs eventhub create']:
        with self.argument_context(scope) as c:
            c.argument('message_retention_in_days', options_list=['--message-retention'], type=int, help='Number of days to retain events for this Event Hub, value should be 1 to 7 days and depends on Namespace sku. if Namespace sku is Basic than value should be one and is Manadatory parameter. Namespace sku is standard value should be 1 to 7 days, default is 7 days and is optional parameter')
            c.argument('partition_count', type=int, help='Number of partitions created for the Event Hub. By default, allowed values are 2-32. Lower value of 1 is supported with Kafka enabled namespaces. In presence of a custom quota, the upper limit will match the upper limit of the quota.')
            c.argument('status', arg_type=get_enum_type(['Active', 'Disabled', 'SendDisabled']), help='Status of Eventhub')
            c.argument('enabled', options_list=['--enable-capture'], arg_type=get_three_state_flag(), help='A boolean value that indicates whether capture description is enabled.')
            c.argument('skip_empty_archives', options_list=['--skip-empty-archives'], arg_type=get_three_state_flag(), help='A boolean value that indicates whether to Skip Empty.')
            c.argument('capture_interval_seconds', arg_group='Capture', options_list=['--capture-interval'], type=int, help='Allows you to set the frequency with which the capture to Azure Blobs will happen, value should between 60 to 900 seconds')
            c.argument('capture_size_limit_bytes', arg_group='Capture', options_list=['--capture-size-limit'], type=int, help='Defines the amount of data built up in your Event Hub before an capture operation, value should be between 10485760 to 524288000 bytes')
            c.argument('destination_name', arg_group='Capture-Destination', help='Name for capture destination')
            c.argument('storage_account_resource_id', arg_group='Capture-Destination', validator=validate_storageaccount, options_list=['--storage-account'], help='Name (if within same resource group and not of type Classic Storage) or ARM id of the storage account to be used to create the blobs')
            c.argument('blob_container', arg_group='Capture-Destination', help='Blob container Name')
            c.argument('archive_name_format', arg_group='Capture-Destination', help='Blob naming convention for archive, e.g. {Namespace}/{EventHub}/{PartitionId}/{Year}/{Month}/{Day}/{Hour}/{Minute}/{Second}. Here all the parameters (Namespace,EventHub .. etc) are mandatory irrespective of order')

    with self.argument_context('eventhubs eventhub list') as c:
        c.argument('namespace_name', options_list=['--namespace-name'], id_part=None, help='Name of Namespace')

    # region EventHub Authorizationrule
    for scope in ['eventhubs eventhub authorization-rule', 'eventhubs eventhub authorization-rule keys renew']:
        with self.argument_context(scope) as c:
            c.argument('authorization_rule_name', arg_type=name_type, id_part='child_name_2', help='Name of EventHub AuthorizationRule')
            c.argument('event_hub_name', id_part='child_name_1', arg_type=event_hub_name_arg_type)

    for scope in ['eventhubs eventhub authorization-rule create', 'eventhubs eventhub authorization-rule update']:
        with self.argument_context(scope) as c:
            c.argument('rights', arg_type=rights_arg_type)

    with self.argument_context('eventhubs eventhub authorization-rule keys renew') as c:
        c.argument('key_type', arg_type=key_arg_type)
        c.argument('key', arg_type=keyvalue_arg_type)

    with self.argument_context('eventhubs eventhub authorization-rule list') as c:
        c.argument('namespace_name', options_list=['--namespace-name'], id_part=None, help='Name of Namespace')
        c.argument('event_hub_name', id_part=None, arg_type=event_hub_name_arg_type)

    with self.argument_context('eventhubs eventhub authorization-rule keys list') as c:
        c.argument('namespace_name', options_list=['--namespace-name'], id_part=None, help='Name of Namespace')
        c.argument('event_hub_name', id_part=None, arg_type=event_hub_name_arg_type)
        c.argument('authorization_rule_name', arg_type=name_type, id_part=None, help='Name of EventHub AuthorizationRule')


# - ConsumerGroup Region
    with self.argument_context('eventhubs eventhub consumer-group') as c:
        c.argument('event_hub_name', arg_type=event_hub_name_arg_type)
        c.argument('consumer_group_name', arg_type=name_type, id_part='child_name_2', completer=get_consumergroup_command_completion_list, help='Name of ConsumerGroup')

    for scope in ['eventhubs eventhub consumer-group create', 'eventhubs eventhub consumer-group update']:
        with self.argument_context(scope) as c:
            c.argument('user_metadata', help='Usermetadata is a placeholder to store user-defined string data with maximum length 1024. e.g. it can be used to store descriptive data, such as list of teams and their contact information also user-defined configuration settings can be stored.')

    with self.argument_context('eventhubs eventhub consumer-group list') as c:
        c.argument('event_hub_name', arg_type=event_hub_name_arg_type, id_part=None)
        c.argument('namespace_name', options_list=['--namespace-name'], id_part=None, help='Name of Namespace')

#   : Region Geo DR Configuration
    with self.argument_context('eventhubs georecovery-alias') as c:
        c.argument('alias', options_list=['--alias', '-a'], id_part='child_name_1', help='Name of Geo-Disaster Recovery Configuration Alias')

    with self.argument_context('eventhubs georecovery-alias exists') as c:
        c.argument('name', options_list=['--alias', '-a'], arg_type=name_type, help='Name of Geo Recovery Configs - Alias to check availability')
        c.argument('namespace_name', options_list=['--namespace-name'], id_part=None, help='Name of Namespace')

    with self.argument_context('eventhubs georecovery-alias set') as c:
        c.argument('partner_namespace', required=True, validator=validate_partner_namespace, help='Name (if within the same resource group) or ARM Id of the Primary/Secondary eventhub namespace name, which is part of GEO DR pairing')
        c.argument('alternate_name', help='Alternate Name for the Alias, when the Namespace name and Alias name are same')

    for scope in ['eventhubs georecovery-alias authorization-rule show']:
        with self.argument_context(scope)as c:
            c.argument('authorization_rule_name', arg_type=name_type, id_part='child_name_2', help='Name of Namespace AuthorizationRule')

    with self.argument_context('eventhubs georecovery-alias list') as c:
        c.argument('namespace_name', options_list=['--namespace-name'], id_part=None, help='Name of Namespace')

    with self.argument_context('eventhubs georecovery-alias authorization-rule list') as c:
        c.argument('alias', options_list=['--alias', '-a'], help='Name of Geo-Disaster Recovery Configuration Alias')
        c.argument('namespace_name', options_list=['--namespace-name'], id_part=None, help='Name of Namespace')

    with self.argument_context('eventhubs georecovery-alias authorization-rule keys list') as c:
        c.argument('alias', options_list=['--alias', '-a'], id_part=None, help='Name of Geo-Disaster Recovery Configuration Alias')
        c.argument('namespace_name', options_list=['--namespace-name'], id_part=None, help='Name of Namespace')
        c.argument('authorization_rule_name', arg_type=name_type, help='Name of Namespace AuthorizationRule')

# Region Namespace NetworkRuleSet
    with self.argument_context('eventhubs namespace network-rule', resource_type=ResourceType.MGMT_EVENTHUB, min_api='2017-04-01') as c:
        c.argument('namespace_name', options_list=['--namespace-name'], id_part=None, help='Name of the Namespace')

    for scope in ['eventhubs namespace network-rule add', 'eventhubs namespace network-rule remove']:
        with self.argument_context(scope, resource_type=ResourceType.MGMT_EVENTHUB, min_api='2017-04-01') as c:
            c.argument('subnet', arg_group='Virtual Network Rule', options_list=['--subnet'], help='Name or ID of subnet. If name is supplied, `--vnet-name` must be supplied.')
            c.argument('ip_mask', arg_group='IP Address Rule', options_list=['--ip-address'], help='IPv4 address or CIDR range - 10.6.0.0/24')
            c.argument('namespace_name', options_list=['--namespace-name'], id_part=None, help='Name of the Namespace')
            c.extra('vnet_name', arg_group='Virtual Network Rule', options_list=['--vnet-name'], help='Name of the Virtual Network')

    with self.argument_context('eventhubs namespace network-rule add', resource_type=ResourceType.MGMT_EVENTHUB, min_api='2017-04-01') as c:
        c.argument('ignore_missing_vnet_service_endpoint', arg_group='Virtual Network Rule', options_list=['--ignore-missing-endpoint'], arg_type=get_three_state_flag(), help='A boolean value that indicates whether to ignore missing vnet Service Endpoint')
        c.argument('action', arg_group='IP Address Rule', options_list=['--action'], arg_type=get_enum_type(['Allow']), help='Action of the IP rule')
