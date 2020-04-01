# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spaceone/api/secret/v1/secret_group.proto

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
from spaceone.api.secret.v1 import secret_pb2 as spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='spaceone/api/secret/v1/secret_group.proto',
  package='spaceone.api.secret.v1',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n)spaceone/api/secret/v1/secret_group.proto\x12\x16spaceone.api.secret.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\x1a spaceone/api/core/v1/query.proto\x1a#spaceone/api/secret/v1/secret.proto\"b\n\x18\x43reateSecretGroupRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12%\n\x04tags\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x03 \x01(\t\"{\n\x18UpdateSecretGroupRequest\x12\x17\n\x0fsecret_group_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12%\n\x04tags\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x04 \x01(\t\"@\n\x12SecretGroupRequest\x12\x17\n\x0fsecret_group_id\x18\x01 \x01(\t\x12\x11\n\tdomain_id\x18\x02 \x01(\t\"Y\n\x18SecretGroupSecretRequest\x12\x17\n\x0fsecret_group_id\x18\x01 \x01(\t\x12\x11\n\tsecret_id\x18\x02 \x01(\t\x12\x11\n\tdomain_id\x18\x05 \x01(\t\"\x8b\x01\n\x10SecretGroupQuery\x12*\n\x05query\x18\x01 \x01(\x0b\x32\x1b.spaceone.api.core.v1.Query\x12\x17\n\x0fsecret_group_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x11\n\tsecret_id\x18\x04 \x01(\t\x12\x11\n\tdomain_id\x18\x05 \x01(\t\"\xa7\x01\n\x15SecretGroupSecretInfo\x12\x42\n\x11secret_group_info\x18\x01 \x01(\x0b\x32\'.spaceone.api.secret.v1.SecretGroupInfo\x12\x37\n\x0bsecret_info\x18\x02 \x01(\x0b\x32\".spaceone.api.secret.v1.SecretInfo\x12\x11\n\tdomain_id\x18\x05 \x01(\t\"\xa2\x01\n\x0fSecretGroupInfo\x12\x17\n\x0fsecret_group_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12%\n\x04tags\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x11\n\tdomain_id\x18\x05 \x01(\t\x12.\n\ncreated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"a\n\x10SecretGroupsInfo\x12\x38\n\x07results\x18\x01 \x03(\x0b\x32\'.spaceone.api.secret.v1.SecretGroupInfo\x12\x13\n\x0btotal_count\x18\x02 \x01(\x05\x32\xad\x08\n\x0bSecretGroup\x12\x85\x01\n\x06\x63reate\x12\x30.spaceone.api.secret.v1.CreateSecretGroupRequest\x1a\'.spaceone.api.secret.v1.SecretGroupInfo\" \x82\xd3\xe4\x93\x02\x1a\"\x18/secret/v1/secret-groups\x12\x96\x01\n\x06update\x12\x30.spaceone.api.secret.v1.UpdateSecretGroupRequest\x1a\'.spaceone.api.secret.v1.SecretGroupInfo\"1\x82\xd3\xe4\x93\x02+\x1a)/secret/v1/secret-group/{secret_group_id}\x12\xa8\x01\n\nadd_secret\x12\x30.spaceone.api.secret.v1.SecretGroupSecretRequest\x1a-.spaceone.api.secret.v1.SecretGroupSecretInfo\"9\x82\xd3\xe4\x93\x02\x33\"1/secret/v1/secret-group/{secret_group_id}/secrets\x12\x9f\x01\n\rremove_secret\x12\x30.spaceone.api.secret.v1.SecretGroupSecretRequest\x1a\x16.google.protobuf.Empty\"D\x82\xd3\xe4\x93\x02>*</secret/v1/secret-group/{secret_group_id}/secret/{secret_id}\x12\x7f\n\x06\x64\x65lete\x12*.spaceone.api.secret.v1.SecretGroupRequest\x1a\x16.google.protobuf.Empty\"1\x82\xd3\xe4\x93\x02+*)/secret/v1/secret-group/{secret_group_id}\x12\x8d\x01\n\x03get\x12*.spaceone.api.secret.v1.SecretGroupRequest\x1a\'.spaceone.api.secret.v1.SecretGroupInfo\"1\x82\xd3\xe4\x93\x02+\x12)/secret/v1/secret-group/{secret_group_id}\x12\x9e\x01\n\x04list\x12(.spaceone.api.secret.v1.SecretGroupQuery\x1a(.spaceone.api.secret.v1.SecretGroupsInfo\"B\x82\xd3\xe4\x93\x02<\x12\x18/secret/v1/secret-groupsZ \"\x1e/secret/v1/secret-groups/queryb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,spaceone_dot_api_dot_core_dot_v1_dot_query__pb2.DESCRIPTOR,spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.DESCRIPTOR,])




_CREATESECRETGROUPREQUEST = _descriptor.Descriptor(
  name='CreateSecretGroupRequest',
  full_name='spaceone.api.secret.v1.CreateSecretGroupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='spaceone.api.secret.v1.CreateSecretGroupRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='spaceone.api.secret.v1.CreateSecretGroupRequest.tags', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.secret.v1.CreateSecretGroupRequest.domain_id', index=2,
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
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=262,
  serialized_end=360,
)


_UPDATESECRETGROUPREQUEST = _descriptor.Descriptor(
  name='UpdateSecretGroupRequest',
  full_name='spaceone.api.secret.v1.UpdateSecretGroupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='secret_group_id', full_name='spaceone.api.secret.v1.UpdateSecretGroupRequest.secret_group_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='spaceone.api.secret.v1.UpdateSecretGroupRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='spaceone.api.secret.v1.UpdateSecretGroupRequest.tags', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.secret.v1.UpdateSecretGroupRequest.domain_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=362,
  serialized_end=485,
)


_SECRETGROUPREQUEST = _descriptor.Descriptor(
  name='SecretGroupRequest',
  full_name='spaceone.api.secret.v1.SecretGroupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='secret_group_id', full_name='spaceone.api.secret.v1.SecretGroupRequest.secret_group_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.secret.v1.SecretGroupRequest.domain_id', index=1,
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
  serialized_start=487,
  serialized_end=551,
)


_SECRETGROUPSECRETREQUEST = _descriptor.Descriptor(
  name='SecretGroupSecretRequest',
  full_name='spaceone.api.secret.v1.SecretGroupSecretRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='secret_group_id', full_name='spaceone.api.secret.v1.SecretGroupSecretRequest.secret_group_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secret_id', full_name='spaceone.api.secret.v1.SecretGroupSecretRequest.secret_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.secret.v1.SecretGroupSecretRequest.domain_id', index=2,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=553,
  serialized_end=642,
)


_SECRETGROUPQUERY = _descriptor.Descriptor(
  name='SecretGroupQuery',
  full_name='spaceone.api.secret.v1.SecretGroupQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='spaceone.api.secret.v1.SecretGroupQuery.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secret_group_id', full_name='spaceone.api.secret.v1.SecretGroupQuery.secret_group_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='spaceone.api.secret.v1.SecretGroupQuery.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secret_id', full_name='spaceone.api.secret.v1.SecretGroupQuery.secret_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.secret.v1.SecretGroupQuery.domain_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=645,
  serialized_end=784,
)


_SECRETGROUPSECRETINFO = _descriptor.Descriptor(
  name='SecretGroupSecretInfo',
  full_name='spaceone.api.secret.v1.SecretGroupSecretInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='secret_group_info', full_name='spaceone.api.secret.v1.SecretGroupSecretInfo.secret_group_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secret_info', full_name='spaceone.api.secret.v1.SecretGroupSecretInfo.secret_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.secret.v1.SecretGroupSecretInfo.domain_id', index=2,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=787,
  serialized_end=954,
)


_SECRETGROUPINFO = _descriptor.Descriptor(
  name='SecretGroupInfo',
  full_name='spaceone.api.secret.v1.SecretGroupInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='secret_group_id', full_name='spaceone.api.secret.v1.SecretGroupInfo.secret_group_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='spaceone.api.secret.v1.SecretGroupInfo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='spaceone.api.secret.v1.SecretGroupInfo.tags', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_id', full_name='spaceone.api.secret.v1.SecretGroupInfo.domain_id', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='spaceone.api.secret.v1.SecretGroupInfo.created_at', index=4,
      number=6, type=11, cpp_type=10, label=1,
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
  serialized_start=957,
  serialized_end=1119,
)


_SECRETGROUPSINFO = _descriptor.Descriptor(
  name='SecretGroupsInfo',
  full_name='spaceone.api.secret.v1.SecretGroupsInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='spaceone.api.secret.v1.SecretGroupsInfo.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_count', full_name='spaceone.api.secret.v1.SecretGroupsInfo.total_count', index=1,
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
  serialized_start=1121,
  serialized_end=1218,
)

_CREATESECRETGROUPREQUEST.fields_by_name['tags'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_UPDATESECRETGROUPREQUEST.fields_by_name['tags'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SECRETGROUPQUERY.fields_by_name['query'].message_type = spaceone_dot_api_dot_core_dot_v1_dot_query__pb2._QUERY
_SECRETGROUPSECRETINFO.fields_by_name['secret_group_info'].message_type = _SECRETGROUPINFO
_SECRETGROUPSECRETINFO.fields_by_name['secret_info'].message_type = spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2._SECRETINFO
_SECRETGROUPINFO.fields_by_name['tags'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SECRETGROUPINFO.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SECRETGROUPSINFO.fields_by_name['results'].message_type = _SECRETGROUPINFO
DESCRIPTOR.message_types_by_name['CreateSecretGroupRequest'] = _CREATESECRETGROUPREQUEST
DESCRIPTOR.message_types_by_name['UpdateSecretGroupRequest'] = _UPDATESECRETGROUPREQUEST
DESCRIPTOR.message_types_by_name['SecretGroupRequest'] = _SECRETGROUPREQUEST
DESCRIPTOR.message_types_by_name['SecretGroupSecretRequest'] = _SECRETGROUPSECRETREQUEST
DESCRIPTOR.message_types_by_name['SecretGroupQuery'] = _SECRETGROUPQUERY
DESCRIPTOR.message_types_by_name['SecretGroupSecretInfo'] = _SECRETGROUPSECRETINFO
DESCRIPTOR.message_types_by_name['SecretGroupInfo'] = _SECRETGROUPINFO
DESCRIPTOR.message_types_by_name['SecretGroupsInfo'] = _SECRETGROUPSINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateSecretGroupRequest = _reflection.GeneratedProtocolMessageType('CreateSecretGroupRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESECRETGROUPREQUEST,
  '__module__' : 'spaceone.api.secret.v1.secret_group_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.secret.v1.CreateSecretGroupRequest)
  })
_sym_db.RegisterMessage(CreateSecretGroupRequest)

UpdateSecretGroupRequest = _reflection.GeneratedProtocolMessageType('UpdateSecretGroupRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATESECRETGROUPREQUEST,
  '__module__' : 'spaceone.api.secret.v1.secret_group_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.secret.v1.UpdateSecretGroupRequest)
  })
_sym_db.RegisterMessage(UpdateSecretGroupRequest)

SecretGroupRequest = _reflection.GeneratedProtocolMessageType('SecretGroupRequest', (_message.Message,), {
  'DESCRIPTOR' : _SECRETGROUPREQUEST,
  '__module__' : 'spaceone.api.secret.v1.secret_group_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.secret.v1.SecretGroupRequest)
  })
_sym_db.RegisterMessage(SecretGroupRequest)

SecretGroupSecretRequest = _reflection.GeneratedProtocolMessageType('SecretGroupSecretRequest', (_message.Message,), {
  'DESCRIPTOR' : _SECRETGROUPSECRETREQUEST,
  '__module__' : 'spaceone.api.secret.v1.secret_group_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.secret.v1.SecretGroupSecretRequest)
  })
_sym_db.RegisterMessage(SecretGroupSecretRequest)

SecretGroupQuery = _reflection.GeneratedProtocolMessageType('SecretGroupQuery', (_message.Message,), {
  'DESCRIPTOR' : _SECRETGROUPQUERY,
  '__module__' : 'spaceone.api.secret.v1.secret_group_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.secret.v1.SecretGroupQuery)
  })
_sym_db.RegisterMessage(SecretGroupQuery)

SecretGroupSecretInfo = _reflection.GeneratedProtocolMessageType('SecretGroupSecretInfo', (_message.Message,), {
  'DESCRIPTOR' : _SECRETGROUPSECRETINFO,
  '__module__' : 'spaceone.api.secret.v1.secret_group_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.secret.v1.SecretGroupSecretInfo)
  })
_sym_db.RegisterMessage(SecretGroupSecretInfo)

SecretGroupInfo = _reflection.GeneratedProtocolMessageType('SecretGroupInfo', (_message.Message,), {
  'DESCRIPTOR' : _SECRETGROUPINFO,
  '__module__' : 'spaceone.api.secret.v1.secret_group_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.secret.v1.SecretGroupInfo)
  })
_sym_db.RegisterMessage(SecretGroupInfo)

SecretGroupsInfo = _reflection.GeneratedProtocolMessageType('SecretGroupsInfo', (_message.Message,), {
  'DESCRIPTOR' : _SECRETGROUPSINFO,
  '__module__' : 'spaceone.api.secret.v1.secret_group_pb2'
  # @@protoc_insertion_point(class_scope:spaceone.api.secret.v1.SecretGroupsInfo)
  })
_sym_db.RegisterMessage(SecretGroupsInfo)



_SECRETGROUP = _descriptor.ServiceDescriptor(
  name='SecretGroup',
  full_name='spaceone.api.secret.v1.SecretGroup',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1221,
  serialized_end=2290,
  methods=[
  _descriptor.MethodDescriptor(
    name='create',
    full_name='spaceone.api.secret.v1.SecretGroup.create',
    index=0,
    containing_service=None,
    input_type=_CREATESECRETGROUPREQUEST,
    output_type=_SECRETGROUPINFO,
    serialized_options=b'\202\323\344\223\002\032\"\030/secret/v1/secret-groups',
  ),
  _descriptor.MethodDescriptor(
    name='update',
    full_name='spaceone.api.secret.v1.SecretGroup.update',
    index=1,
    containing_service=None,
    input_type=_UPDATESECRETGROUPREQUEST,
    output_type=_SECRETGROUPINFO,
    serialized_options=b'\202\323\344\223\002+\032)/secret/v1/secret-group/{secret_group_id}',
  ),
  _descriptor.MethodDescriptor(
    name='add_secret',
    full_name='spaceone.api.secret.v1.SecretGroup.add_secret',
    index=2,
    containing_service=None,
    input_type=_SECRETGROUPSECRETREQUEST,
    output_type=_SECRETGROUPSECRETINFO,
    serialized_options=b'\202\323\344\223\0023\"1/secret/v1/secret-group/{secret_group_id}/secrets',
  ),
  _descriptor.MethodDescriptor(
    name='remove_secret',
    full_name='spaceone.api.secret.v1.SecretGroup.remove_secret',
    index=3,
    containing_service=None,
    input_type=_SECRETGROUPSECRETREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002>*</secret/v1/secret-group/{secret_group_id}/secret/{secret_id}',
  ),
  _descriptor.MethodDescriptor(
    name='delete',
    full_name='spaceone.api.secret.v1.SecretGroup.delete',
    index=4,
    containing_service=None,
    input_type=_SECRETGROUPREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002+*)/secret/v1/secret-group/{secret_group_id}',
  ),
  _descriptor.MethodDescriptor(
    name='get',
    full_name='spaceone.api.secret.v1.SecretGroup.get',
    index=5,
    containing_service=None,
    input_type=_SECRETGROUPREQUEST,
    output_type=_SECRETGROUPINFO,
    serialized_options=b'\202\323\344\223\002+\022)/secret/v1/secret-group/{secret_group_id}',
  ),
  _descriptor.MethodDescriptor(
    name='list',
    full_name='spaceone.api.secret.v1.SecretGroup.list',
    index=6,
    containing_service=None,
    input_type=_SECRETGROUPQUERY,
    output_type=_SECRETGROUPSINFO,
    serialized_options=b'\202\323\344\223\002<\022\030/secret/v1/secret-groupsZ \"\036/secret/v1/secret-groups/query',
  ),
])
_sym_db.RegisterServiceDescriptor(_SECRETGROUP)

DESCRIPTOR.services_by_name['SecretGroup'] = _SECRETGROUP

# @@protoc_insertion_point(module_scope)
