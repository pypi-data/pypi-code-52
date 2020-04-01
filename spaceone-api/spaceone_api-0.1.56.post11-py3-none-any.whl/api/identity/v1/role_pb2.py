# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/identity/v1/role.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from spaceone.api.core.v1 import query_pb2 as spaceone_dot_api_dot_core_dot_v1_dot_query__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='spaceone/api/identity/v1/role.proto',
  package='spaceone.api.identity.v1',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n#spaceone/api/identity/v1/role.proto\x12\x18spaceone.api.identity.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\"\xb6\x01\n\nRolePolicy\x12\x44\n\x0bpolicy_type\x18\x01 \x01(\x0e\x32/.spaceone.api.identity.v1.RolePolicy.PolicyType\x12\r\n\x03url\x18\x02 \x01(\tH\x00\x12\x13\n\tpolicy_id\x18\x03 \x01(\tH\x00\"/\n\nPolicyType\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07MANAGED\x10\x01\x12\n\n\x06\x43USTOM\x10\x02\x42\r\n\x0bpolicy_info\"\xca\x01\n\x11\x43reateRoleRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\x12\x35\n\trole_type\x18\x03 \x01(\x0e\x32\".spaceone.api.identity.v1.RoleType\x12\x36\n\x08policies\x18\x04 \x03(\x0b\x32$.spaceone.api.identity.v1.RolePolicy\x12%\n\x04tags\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\"\xa4\x01\n\x11UpdateRoleRequest\x12\x0f\n\x07role_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tdomain_id\x18\x03 \x01(\t\x12\x36\n\x08policies\x18\x04 \x03(\x0b\x32$.spaceone.api.identity.v1.RolePolicy\x12%\n\x04tags\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\"1\n\x0bRoleRequest\x12\x0f\n\x07role_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\"\xb2\x02\n\x08RoleInfo\x12\x0f\n\x07role_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x35\n\trole_type\x18\x03 \x01(\x0e\x32\".spaceone.api.identity.v1.RoleType\x12\x36\n\x08policies\x18\x04 \x03(\x0b\x32$.spaceone.api.identity.v1.RolePolicy\x12%\n\x04tags\x18\x05 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x0b \x01(\t\x12.\n\ncreated_at\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\ndeleted_at\x18\x16 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xa0\x01\n\tRoleQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12\x0f\n\x07role_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x35\n\trole_type\x18\x05 \x01(\x0e\x32\".spaceone.api.identity.v1.RoleType\x12\x11\n\tdomain_id\x18\x0b \x01(\t\"U\n\tRolesInfo\x12\x33\n\x07results\x18\x01 \x03(\x0b\x32\".spaceone.api.identity.v1.RoleInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05*9\n\x08RoleType\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06SYSTEM\x10\x01\x12\n\n\x06\x44OMAIN\x10\x02\x12\x0b\n\x07PROJECT\x10\x03\x32\xf0\x04\n\x04Role\x12u\n\x06\x63reate\x12+.spaceone.api.identity.v1.CreateRoleRequest\x1a\".spaceone.api.identity.v1.RoleInfo\"\x1a\x82\xd3\xe4\x93\x02\x14\"\x12/identity/v1/roles\x12\x7f\n\x06update\x12+.spaceone.api.identity.v1.UpdateRoleRequest\x1a\".spaceone.api.identity.v1.RoleInfo\"$\x82\xd3\xe4\x93\x02\x1e\x1a\x1c/identity/v1/roles/{role_id}\x12m\n\x06\x64\x65lete\x12%.spaceone.api.identity.v1.RoleRequest\x1a\x16.google.protobuf.Empty\"$\x82\xd3\xe4\x93\x02\x1e*\x1c/identity/v1/roles/{role_id}\x12v\n\x03get\x12%.spaceone.api.identity.v1.RoleRequest\x1a\".spaceone.api.identity.v1.RoleInfo\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/identity/v1/roles/{role_id}\x12\x88\x01\n\x04list\x12#.spaceone.api.identity.v1.RoleQuery\x1a#.spaceone.api.identity.v1.RolesInfo\"6\x82\xd3\xe4\x93\x02\x30\x12\x12/identity/v1/rolesZ\x1a\"\x18/identity/v1/roles/queryb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,spaceone_dot_api_dot_core_dot_v1_dot_query__pb2.DESCRIPTOR,])

_ROLETYPE = _descriptor.EnumDescriptor(
  name='RoleType',
  full_name='spaceone.api.identity.v1.RoleType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYSTEM', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOMAIN', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROJECT', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1388,
  serialized_end=1445,
)
_sym_db.RegisterEnumDescriptor(_ROLETYPE)

RoleType = enum_type_wrapper.EnumTypeWrapper(_ROLETYPE)
NONE = 0
SYSTEM = 1
DOMAIN = 2
PROJECT = 3


_ROLEPOLICY_POLICYTYPE = _descriptor.EnumDescriptor(
  name='PolicyType',
  full_name='spaceone.api.identity.v1.RolePolicy.PolicyType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MANAGED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=342,
  serialized_end=389,
)
_sym_db.RegisterEnumDescriptor(_ROLEPOLICY_POLICYTYPE)


_ROLEPOLICY = _descriptor.Descriptor(
  name='RolePolicy',
  full_name='spaceone.api.identity.v1.RolePolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='policy_type', full_name='spaceone.api.identity.v1.RolePolicy.policy_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='spaceone.api.identity.v1.RolePolicy.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='policy_id', full_name='spaceone.api.identity.v1.RolePolicy.policy_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ROLEPOLICY_POLICYTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='policy_info', full_name='spaceone.api.identity.v1.RolePolicy.policy_info',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=222,
  serialized_end=404,
)


_CREATEROLEREQUEST = _descriptor.Descriptor(
  name='CreateRoleRequest',
  full_name='spaceone.api.identity.v1.CreateRoleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='spaceone.api.identity.v1.CreateRoleRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.identity.v1.CreateRoleRequest.domain_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role_type', full_name='spaceone.api.identity.v1.CreateRoleRequest.role_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='policies', full_name='spaceone.api.identity.v1.CreateRoleRequest.policies', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='spaceone.api.identity.v1.CreateRoleRequest.tags', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=407,
  serialized_end=609,
)


_UPDATEROLEREQUEST = _descriptor.Descriptor(
  name='UpdateRoleRequest',
  full_name='spaceone.api.identity.v1.UpdateRoleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='role_id', full_name='spaceone.api.identity.v1.UpdateRoleRequest.role_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='spaceone.api.identity.v1.UpdateRoleRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.identity.v1.UpdateRoleRequest.domain_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='policies', full_name='spaceone.api.identity.v1.UpdateRoleRequest.policies', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='spaceone.api.identity.v1.UpdateRoleRequest.tags', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=612,
  serialized_end=776,
)


_ROLEREQUEST = _descriptor.Descriptor(
  name='RoleRequest',
  full_name='spaceone.api.identity.v1.RoleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='role_id', full_name='spaceone.api.identity.v1.RoleRequest.role_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.identity.v1.RoleRequest.domain_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=778,
  serialized_end=827,
)


_ROLEINFO = _descriptor.Descriptor(
  name='RoleInfo',
  full_name='spaceone.api.identity.v1.RoleInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='role_id', full_name='spaceone.api.identity.v1.RoleInfo.role_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='spaceone.api.identity.v1.RoleInfo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role_type', full_name='spaceone.api.identity.v1.RoleInfo.role_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='policies', full_name='spaceone.api.identity.v1.RoleInfo.policies', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='spaceone.api.identity.v1.RoleInfo.tags', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.identity.v1.RoleInfo.domain_id', index=5,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='spaceone.api.identity.v1.RoleInfo.created_at', index=6,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deleted_at', full_name='spaceone.api.identity.v1.RoleInfo.deleted_at', index=7,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=830,
  serialized_end=1136,
)


_ROLEQUERY = _descriptor.Descriptor(
  name='RoleQuery',
  full_name='spaceone.api.identity.v1.RoleQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='spaceone.api.identity.v1.RoleQuery.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role_id', full_name='spaceone.api.identity.v1.RoleQuery.role_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='spaceone.api.identity.v1.RoleQuery.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role_type', full_name='spaceone.api.identity.v1.RoleQuery.role_type', index=3,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.identity.v1.RoleQuery.domain_id', index=4,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1139,
  serialized_end=1299,
)


_ROLESINFO = _descriptor.Descriptor(
  name='RolesInfo',
  full_name='spaceone.api.identity.v1.RolesInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='spaceone.api.identity.v1.RolesInfo.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_count', full_name='spaceone.api.identity.v1.RolesInfo.total_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1301,
  serialized_end=1386,
)

_ROLEPOLICY.fields_by_name['policy_type'].enum_type = _ROLEPOLICY_POLICYTYPE
_ROLEPOLICY_POLICYTYPE.containing_type = _ROLEPOLICY
_ROLEPOLICY.oneofs_by_name['policy_info'].fields.append(
  _ROLEPOLICY.fields_by_name['url'])
_ROLEPOLICY.fields_by_name['url'].containing_oneof = _ROLEPOLICY.oneofs_by_name['policy_info']
_ROLEPOLICY.oneofs_by_name['policy_info'].fields.append(
  _ROLEPOLICY.fields_by_name['policy_id'])
_ROLEPOLICY.fields_by_name['policy_id'].containing_oneof = _ROLEPOLICY.oneofs_by_name['policy_info']
_CREATEROLEREQUEST.fields_by_name['role_type'].enum_type = _ROLETYPE
_CREATEROLEREQUEST.fields_by_name['policies'].message_type = _ROLEPOLICY
_CREATEROLEREQUEST.fields_by_name['tags'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_UPDATEROLEREQUEST.fields_by_name['policies'].message_type = _ROLEPOLICY
_UPDATEROLEREQUEST.fields_by_name['tags'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_ROLEINFO.fields_by_name['role_type'].enum_type = _ROLETYPE
_ROLEINFO.fields_by_name['policies'].message_type = _ROLEPOLICY
_ROLEINFO.fields_by_name['tags'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_ROLEINFO.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ROLEINFO.fields_by_name['deleted_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ROLEQUERY.fields_by_name['query'].message_type = spaceone_dot_api_dot_core_dot_v1_dot_query__pb2._QUERY
_ROLEQUERY.fields_by_name['role_type'].enum_type = _ROLETYPE
_ROLESINFO.fields_by_name['results'].message_type = _ROLEINFO
DESCRIPTOR.message_types_by_name['RolePolicy'] = _ROLEPOLICY
DESCRIPTOR.message_types_by_name['CreateRoleRequest'] = _CREATEROLEREQUEST
DESCRIPTOR.message_types_by_name['UpdateRoleRequest'] = _UPDATEROLEREQUEST
DESCRIPTOR.message_types_by_name['RoleRequest'] = _ROLEREQUEST
DESCRIPTOR.message_types_by_name['RoleInfo'] = _ROLEINFO
DESCRIPTOR.message_types_by_name['RoleQuery'] = _ROLEQUERY
DESCRIPTOR.message_types_by_name['RolesInfo'] = _ROLESINFO
DESCRIPTOR.enum_types_by_name['RoleType'] = _ROLETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RolePolicy = _reflection.GeneratedProtocolMessageType('RolePolicy', (_message.Message,), {
  'DESCRIPTOR' : _ROLEPOLICY,
  '__module__' : 'spaceone.api.identity.v1.role_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.RolePolicy)
  })
_sym_db.RegisterMessage(RolePolicy)

CreateRoleRequest = _reflection.GeneratedProtocolMessageType('CreateRoleRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEROLEREQUEST,
  '__module__' : 'spaceone.api.identity.v1.role_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.CreateRoleRequest)
  })
_sym_db.RegisterMessage(CreateRoleRequest)

UpdateRoleRequest = _reflection.GeneratedProtocolMessageType('UpdateRoleRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEROLEREQUEST,
  '__module__' : 'spaceone.api.identity.v1.role_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.UpdateRoleRequest)
  })
_sym_db.RegisterMessage(UpdateRoleRequest)

RoleRequest = _reflection.GeneratedProtocolMessageType('RoleRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLEREQUEST,
  '__module__' : 'spaceone.api.identity.v1.role_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.RoleRequest)
  })
_sym_db.RegisterMessage(RoleRequest)

RoleInfo = _reflection.GeneratedProtocolMessageType('RoleInfo', (_message.Message,), {
  'DESCRIPTOR' : _ROLEINFO,
  '__module__' : 'spaceone.api.identity.v1.role_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.RoleInfo)
  })
_sym_db.RegisterMessage(RoleInfo)

RoleQuery = _reflection.GeneratedProtocolMessageType('RoleQuery', (_message.Message,), {
  'DESCRIPTOR' : _ROLEQUERY,
  '__module__' : 'spaceone.api.identity.v1.role_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.RoleQuery)
  })
_sym_db.RegisterMessage(RoleQuery)

RolesInfo = _reflection.GeneratedProtocolMessageType('RolesInfo', (_message.Message,), {
  'DESCRIPTOR' : _ROLESINFO,
  '__module__' : 'spaceone.api.identity.v1.role_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.identity.v1.RolesInfo)
  })
_sym_db.RegisterMessage(RolesInfo)



_ROLE = _descriptor.ServiceDescriptor(
  name='Role',
  full_name='spaceone.api.identity.v1.Role',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1448,
  serialized_end=2072,
  methods=[
  _descriptor.MethodDescriptor(
    name='create',
    full_name='spaceone.api.identity.v1.Role.create',
    index=0,
    containing_service=None,
    input_type=_CREATEROLEREQUEST,
    output_type=_ROLEINFO,
    serialized_options=b'\202\323\344\223\002\024\"\022/identity/v1/roles',
  ),
  _descriptor.MethodDescriptor(
    name='update',
    full_name='spaceone.api.identity.v1.Role.update',
    index=1,
    containing_service=None,
    input_type=_UPDATEROLEREQUEST,
    output_type=_ROLEINFO,
    serialized_options=b'\202\323\344\223\002\036\032\034/identity/v1/roles/{role_id}',
  ),
  _descriptor.MethodDescriptor(
    name='delete',
    full_name='spaceone.api.identity.v1.Role.delete',
    index=2,
    containing_service=None,
    input_type=_ROLEREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002\036*\034/identity/v1/roles/{role_id}',
  ),
  _descriptor.MethodDescriptor(
    name='get',
    full_name='spaceone.api.identity.v1.Role.get',
    index=3,
    containing_service=None,
    input_type=_ROLEREQUEST,
    output_type=_ROLEINFO,
    serialized_options=b'\202\323\344\223\002\036\022\034/identity/v1/roles/{role_id}',
  ),
  _descriptor.MethodDescriptor(
    name='list',
    full_name='spaceone.api.identity.v1.Role.list',
    index=4,
    containing_service=None,
    input_type=_ROLEQUERY,
    output_type=_ROLESINFO,
    serialized_options=b'\202\323\344\223\0020\022\022/identity/v1/rolesZ\032\"\030/identity/v1/roles/query',
  ),
])
_sym_db.RegisterServiceDescriptor(_ROLE)

DESCRIPTOR.services_by_name['Role'] = _ROLE

# @@protoc_insertion_point(module_scope)
