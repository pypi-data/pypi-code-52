# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/public/uac/UACService.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/public/uac/UACService.proto',
  package='ai.verta.uac',
  syntax='proto3',
  serialized_options=b'P\001Z:github.com/VertaAI/modeldb/protos/gen/go/protos/public/uac',
  serialized_pb=b'\n\"protos/public/uac/UACService.proto\x12\x0c\x61i.verta.uac\x1a\x1cgoogle/api/annotations.proto\"\x07\n\x05\x45mpty\";\n\x07GetUser\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x10\n\x08username\x18\x03 \x01(\t\"w\n\x08GetUsers\x12\x10\n\x08user_ids\x18\x01 \x03(\t\x12\x0e\n\x06\x65mails\x18\x02 \x03(\t\x12\x11\n\tusernames\x18\x03 \x03(\t\x1a\x36\n\x08Response\x12*\n\nuser_infos\x18\x01 \x03(\x0b\x32\x16.ai.verta.uac.UserInfo\"k\n\x15IdServiceProviderEnum\"R\n\x11IdServiceProvider\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06GITHUB\x10\x01\x12\r\n\tBITBUCKET\x10\x02\x12\n\n\x06GOOGLE\x10\x03\x12\t\n\x05VERTA\x10\x04\"\xb3\x01\n\rVertaUserInfo\x12\x17\n\x0findividual_user\x18\x01 \x01(\x08\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x19\n\x11refresh_timestamp\x18\x03 \x01(\x04\x12\x1c\n\x14last_login_timestamp\x18\x04 \x01(\x04\x12\x0f\n\x07user_id\x18\x05 \x01(\t\x12-\n\rpublicProfile\x18\x06 \x01(\x0e\x32\x16.ai.verta.uac.FlagEnum\"\x9c\x02\n\x08UserInfo\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x11\n\tfull_name\x18\x02 \x01(\t\x12\x12\n\nfirst_name\x18\x03 \x01(\t\x12\x11\n\tlast_name\x18\x04 \x01(\t\x12\r\n\x05\x65mail\x18\x05 \x01(\t\x12R\n\x13id_service_provider\x18\x06 \x01(\x0e\x32\x35.ai.verta.uac.IdServiceProviderEnum.IdServiceProvider\x12\r\n\x05roles\x18\x07 \x03(\t\x12\x11\n\timage_url\x18\x08 \x01(\t\x12\x0f\n\x07\x64\x65v_key\x18\t \x01(\t\x12/\n\nverta_info\x18\n \x01(\x0b\x32\x1b.ai.verta.uac.VertaUserInfo\"v\n\nCreateUser\x12$\n\x04info\x18\x01 \x01(\x0b\x32\x16.ai.verta.uac.UserInfo\x12\x10\n\x08password\x18\x02 \x01(\t\x1a\x30\n\x08Response\x12$\n\x04info\x18\x01 \x01(\x0b\x32\x16.ai.verta.uac.UserInfo\"v\n\nUpdateUser\x12$\n\x04info\x18\x01 \x01(\x0b\x32\x16.ai.verta.uac.UserInfo\x12\x10\n\x08password\x18\x02 \x01(\t\x1a\x30\n\x08Response\x12$\n\x04info\x18\x01 \x01(\x0b\x32\x16.ai.verta.uac.UserInfo\"9\n\nDeleteUser\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x1a\x1a\n\x08Response\x12\x0e\n\x06status\x18\x01 \x01(\x08*.\n\x08\x46lagEnum\x12\r\n\tUNDEFINED\x10\x00\x12\x08\n\x04TRUE\x10\x01\x12\t\n\x05\x46\x41LSE\x10\x02\x32\xde\x04\n\nUACService\x12]\n\x0egetCurrentUser\x12\x13.ai.verta.uac.Empty\x1a\x16.ai.verta.uac.UserInfo\"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/v1/uac/getCurrentUser\x12Q\n\x07getUser\x12\x15.ai.verta.uac.GetUser\x1a\x16.ai.verta.uac.UserInfo\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/v1/uac/getUser\x12`\n\x08getUsers\x12\x16.ai.verta.uac.GetUsers\x1a\x1f.ai.verta.uac.GetUsers.Response\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x10/v1/uac/getUsers:\x01*\x12h\n\ncreateUser\x12\x18.ai.verta.uac.CreateUser\x1a!.ai.verta.uac.CreateUser.Response\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x12/v1/uac/createUser:\x01*\x12h\n\nupdateUser\x12\x18.ai.verta.uac.UpdateUser\x1a!.ai.verta.uac.UpdateUser.Response\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x12/v1/uac/updateUser:\x01*\x12h\n\ndeleteUser\x12\x18.ai.verta.uac.DeleteUser\x1a!.ai.verta.uac.DeleteUser.Response\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x12/v1/uac/deleteUser:\x01*B>P\x01Z:github.com/VertaAI/modeldb/protos/gen/go/protos/public/uacb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])

_FLAGENUM = _descriptor.EnumDescriptor(
  name='FlagEnum',
  full_name='ai.verta.uac.FlagEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRUE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FALSE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1150,
  serialized_end=1196,
)
_sym_db.RegisterEnumDescriptor(_FLAGENUM)

FlagEnum = enum_type_wrapper.EnumTypeWrapper(_FLAGENUM)
UNDEFINED = 0
TRUE = 1
FALSE = 2


_IDSERVICEPROVIDERENUM_IDSERVICEPROVIDER = _descriptor.EnumDescriptor(
  name='IdServiceProvider',
  full_name='ai.verta.uac.IdServiceProviderEnum.IdServiceProvider',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GITHUB', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BITBUCKET', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GOOGLE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VERTA', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=298,
  serialized_end=380,
)
_sym_db.RegisterEnumDescriptor(_IDSERVICEPROVIDERENUM_IDSERVICEPROVIDER)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='ai.verta.uac.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=82,
  serialized_end=89,
)


_GETUSER = _descriptor.Descriptor(
  name='GetUser',
  full_name='ai.verta.uac.GetUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='ai.verta.uac.GetUser.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='ai.verta.uac.GetUser.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='ai.verta.uac.GetUser.username', index=2,
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
  serialized_start=91,
  serialized_end=150,
)


_GETUSERS_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='ai.verta.uac.GetUsers.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_infos', full_name='ai.verta.uac.GetUsers.Response.user_infos', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=217,
  serialized_end=271,
)

_GETUSERS = _descriptor.Descriptor(
  name='GetUsers',
  full_name='ai.verta.uac.GetUsers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_ids', full_name='ai.verta.uac.GetUsers.user_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='emails', full_name='ai.verta.uac.GetUsers.emails', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='usernames', full_name='ai.verta.uac.GetUsers.usernames', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETUSERS_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=152,
  serialized_end=271,
)


_IDSERVICEPROVIDERENUM = _descriptor.Descriptor(
  name='IdServiceProviderEnum',
  full_name='ai.verta.uac.IdServiceProviderEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _IDSERVICEPROVIDERENUM_IDSERVICEPROVIDER,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=273,
  serialized_end=380,
)


_VERTAUSERINFO = _descriptor.Descriptor(
  name='VertaUserInfo',
  full_name='ai.verta.uac.VertaUserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='individual_user', full_name='ai.verta.uac.VertaUserInfo.individual_user', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='ai.verta.uac.VertaUserInfo.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='refresh_timestamp', full_name='ai.verta.uac.VertaUserInfo.refresh_timestamp', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_login_timestamp', full_name='ai.verta.uac.VertaUserInfo.last_login_timestamp', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='ai.verta.uac.VertaUserInfo.user_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publicProfile', full_name='ai.verta.uac.VertaUserInfo.publicProfile', index=5,
      number=6, type=14, cpp_type=8, label=1,
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
  serialized_start=383,
  serialized_end=562,
)


_USERINFO = _descriptor.Descriptor(
  name='UserInfo',
  full_name='ai.verta.uac.UserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='ai.verta.uac.UserInfo.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='full_name', full_name='ai.verta.uac.UserInfo.full_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='ai.verta.uac.UserInfo.first_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='ai.verta.uac.UserInfo.last_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='ai.verta.uac.UserInfo.email', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id_service_provider', full_name='ai.verta.uac.UserInfo.id_service_provider', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roles', full_name='ai.verta.uac.UserInfo.roles', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image_url', full_name='ai.verta.uac.UserInfo.image_url', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dev_key', full_name='ai.verta.uac.UserInfo.dev_key', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='verta_info', full_name='ai.verta.uac.UserInfo.verta_info', index=9,
      number=10, type=11, cpp_type=10, label=1,
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
  serialized_start=565,
  serialized_end=849,
)


_CREATEUSER_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='ai.verta.uac.CreateUser.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='info', full_name='ai.verta.uac.CreateUser.Response.info', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=921,
  serialized_end=969,
)

_CREATEUSER = _descriptor.Descriptor(
  name='CreateUser',
  full_name='ai.verta.uac.CreateUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='info', full_name='ai.verta.uac.CreateUser.info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='ai.verta.uac.CreateUser.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CREATEUSER_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=851,
  serialized_end=969,
)


_UPDATEUSER_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='ai.verta.uac.UpdateUser.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='info', full_name='ai.verta.uac.UpdateUser.Response.info', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=921,
  serialized_end=969,
)

_UPDATEUSER = _descriptor.Descriptor(
  name='UpdateUser',
  full_name='ai.verta.uac.UpdateUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='info', full_name='ai.verta.uac.UpdateUser.info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='ai.verta.uac.UpdateUser.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_UPDATEUSER_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=971,
  serialized_end=1089,
)


_DELETEUSER_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='ai.verta.uac.DeleteUser.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ai.verta.uac.DeleteUser.Response.status', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1122,
  serialized_end=1148,
)

_DELETEUSER = _descriptor.Descriptor(
  name='DeleteUser',
  full_name='ai.verta.uac.DeleteUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='ai.verta.uac.DeleteUser.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DELETEUSER_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1091,
  serialized_end=1148,
)

_GETUSERS_RESPONSE.fields_by_name['user_infos'].message_type = _USERINFO
_GETUSERS_RESPONSE.containing_type = _GETUSERS
_IDSERVICEPROVIDERENUM_IDSERVICEPROVIDER.containing_type = _IDSERVICEPROVIDERENUM
_VERTAUSERINFO.fields_by_name['publicProfile'].enum_type = _FLAGENUM
_USERINFO.fields_by_name['id_service_provider'].enum_type = _IDSERVICEPROVIDERENUM_IDSERVICEPROVIDER
_USERINFO.fields_by_name['verta_info'].message_type = _VERTAUSERINFO
_CREATEUSER_RESPONSE.fields_by_name['info'].message_type = _USERINFO
_CREATEUSER_RESPONSE.containing_type = _CREATEUSER
_CREATEUSER.fields_by_name['info'].message_type = _USERINFO
_UPDATEUSER_RESPONSE.fields_by_name['info'].message_type = _USERINFO
_UPDATEUSER_RESPONSE.containing_type = _UPDATEUSER
_UPDATEUSER.fields_by_name['info'].message_type = _USERINFO
_DELETEUSER_RESPONSE.containing_type = _DELETEUSER
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['GetUser'] = _GETUSER
DESCRIPTOR.message_types_by_name['GetUsers'] = _GETUSERS
DESCRIPTOR.message_types_by_name['IdServiceProviderEnum'] = _IDSERVICEPROVIDERENUM
DESCRIPTOR.message_types_by_name['VertaUserInfo'] = _VERTAUSERINFO
DESCRIPTOR.message_types_by_name['UserInfo'] = _USERINFO
DESCRIPTOR.message_types_by_name['CreateUser'] = _CREATEUSER
DESCRIPTOR.message_types_by_name['UpdateUser'] = _UPDATEUSER
DESCRIPTOR.message_types_by_name['DeleteUser'] = _DELETEUSER
DESCRIPTOR.enum_types_by_name['FlagEnum'] = _FLAGENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'protos.public.uac.UACService_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.uac.Empty)
  })
_sym_db.RegisterMessage(Empty)

GetUser = _reflection.GeneratedProtocolMessageType('GetUser', (_message.Message,), {
  'DESCRIPTOR' : _GETUSER,
  '__module__' : 'protos.public.uac.UACService_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.uac.GetUser)
  })
_sym_db.RegisterMessage(GetUser)

GetUsers = _reflection.GeneratedProtocolMessageType('GetUsers', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _GETUSERS_RESPONSE,
    '__module__' : 'protos.public.uac.UACService_pb2'
    # @@protoc_insertion_point(class_scope:ai.verta.uac.GetUsers.Response)
    })
  ,
  'DESCRIPTOR' : _GETUSERS,
  '__module__' : 'protos.public.uac.UACService_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.uac.GetUsers)
  })
_sym_db.RegisterMessage(GetUsers)
_sym_db.RegisterMessage(GetUsers.Response)

IdServiceProviderEnum = _reflection.GeneratedProtocolMessageType('IdServiceProviderEnum', (_message.Message,), {
  'DESCRIPTOR' : _IDSERVICEPROVIDERENUM,
  '__module__' : 'protos.public.uac.UACService_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.uac.IdServiceProviderEnum)
  })
_sym_db.RegisterMessage(IdServiceProviderEnum)

VertaUserInfo = _reflection.GeneratedProtocolMessageType('VertaUserInfo', (_message.Message,), {
  'DESCRIPTOR' : _VERTAUSERINFO,
  '__module__' : 'protos.public.uac.UACService_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.uac.VertaUserInfo)
  })
_sym_db.RegisterMessage(VertaUserInfo)

UserInfo = _reflection.GeneratedProtocolMessageType('UserInfo', (_message.Message,), {
  'DESCRIPTOR' : _USERINFO,
  '__module__' : 'protos.public.uac.UACService_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.uac.UserInfo)
  })
_sym_db.RegisterMessage(UserInfo)

CreateUser = _reflection.GeneratedProtocolMessageType('CreateUser', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _CREATEUSER_RESPONSE,
    '__module__' : 'protos.public.uac.UACService_pb2'
    # @@protoc_insertion_point(class_scope:ai.verta.uac.CreateUser.Response)
    })
  ,
  'DESCRIPTOR' : _CREATEUSER,
  '__module__' : 'protos.public.uac.UACService_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.uac.CreateUser)
  })
_sym_db.RegisterMessage(CreateUser)
_sym_db.RegisterMessage(CreateUser.Response)

UpdateUser = _reflection.GeneratedProtocolMessageType('UpdateUser', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _UPDATEUSER_RESPONSE,
    '__module__' : 'protos.public.uac.UACService_pb2'
    # @@protoc_insertion_point(class_scope:ai.verta.uac.UpdateUser.Response)
    })
  ,
  'DESCRIPTOR' : _UPDATEUSER,
  '__module__' : 'protos.public.uac.UACService_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.uac.UpdateUser)
  })
_sym_db.RegisterMessage(UpdateUser)
_sym_db.RegisterMessage(UpdateUser.Response)

DeleteUser = _reflection.GeneratedProtocolMessageType('DeleteUser', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _DELETEUSER_RESPONSE,
    '__module__' : 'protos.public.uac.UACService_pb2'
    # @@protoc_insertion_point(class_scope:ai.verta.uac.DeleteUser.Response)
    })
  ,
  'DESCRIPTOR' : _DELETEUSER,
  '__module__' : 'protos.public.uac.UACService_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.uac.DeleteUser)
  })
_sym_db.RegisterMessage(DeleteUser)
_sym_db.RegisterMessage(DeleteUser.Response)


DESCRIPTOR._options = None

_UACSERVICE = _descriptor.ServiceDescriptor(
  name='UACService',
  full_name='ai.verta.uac.UACService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1199,
  serialized_end=1805,
  methods=[
  _descriptor.MethodDescriptor(
    name='getCurrentUser',
    full_name='ai.verta.uac.UACService.getCurrentUser',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_USERINFO,
    serialized_options=b'\202\323\344\223\002\030\022\026/v1/uac/getCurrentUser',
  ),
  _descriptor.MethodDescriptor(
    name='getUser',
    full_name='ai.verta.uac.UACService.getUser',
    index=1,
    containing_service=None,
    input_type=_GETUSER,
    output_type=_USERINFO,
    serialized_options=b'\202\323\344\223\002\021\022\017/v1/uac/getUser',
  ),
  _descriptor.MethodDescriptor(
    name='getUsers',
    full_name='ai.verta.uac.UACService.getUsers',
    index=2,
    containing_service=None,
    input_type=_GETUSERS,
    output_type=_GETUSERS_RESPONSE,
    serialized_options=b'\202\323\344\223\002\025\"\020/v1/uac/getUsers:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='createUser',
    full_name='ai.verta.uac.UACService.createUser',
    index=3,
    containing_service=None,
    input_type=_CREATEUSER,
    output_type=_CREATEUSER_RESPONSE,
    serialized_options=b'\202\323\344\223\002\027\"\022/v1/uac/createUser:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='updateUser',
    full_name='ai.verta.uac.UACService.updateUser',
    index=4,
    containing_service=None,
    input_type=_UPDATEUSER,
    output_type=_UPDATEUSER_RESPONSE,
    serialized_options=b'\202\323\344\223\002\027\"\022/v1/uac/updateUser:\001*',
  ),
  _descriptor.MethodDescriptor(
    name='deleteUser',
    full_name='ai.verta.uac.UACService.deleteUser',
    index=5,
    containing_service=None,
    input_type=_DELETEUSER,
    output_type=_DELETEUSER_RESPONSE,
    serialized_options=b'\202\323\344\223\002\027\"\022/v1/uac/deleteUser:\001*',
  ),
])
_sym_db.RegisterServiceDescriptor(_UACSERVICE)

DESCRIPTOR.services_by_name['UACService'] = _UACSERVICE

# @@protoc_insertion_point(module_scope)
