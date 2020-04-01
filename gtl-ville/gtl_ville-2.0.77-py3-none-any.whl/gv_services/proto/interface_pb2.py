# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gv_services/proto/interface.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from gv_services.proto import archivist_pb2 as gv__services_dot_proto_dot_archivist__pb2
from gv_services.proto import broadcaster_pb2 as gv__services_dot_proto_dot_broadcaster__pb2
from gv_services.proto import common_pb2 as gv__services_dot_proto_dot_common__pb2
from gv_services.proto import geographer_pb2 as gv__services_dot_proto_dot_geographer__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='gv_services/proto/interface.proto',
  package='gv_services.proto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n!gv_services/proto/interface.proto\x12\x11gv_services.proto\x1a\x19google/protobuf/any.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a!gv_services/proto/archivist.proto\x1a#gv_services/proto/broadcaster.proto\x1a\x1egv_services/proto/common.proto\x1a\"gv_services/proto/geographer.proto2\xc2\x06\n\tInterface\x12\x42\n\x07publish\x12\x1d.gv_services.proto.PubRequest\x1a\x16.gv_services.proto.Ack\"\x00\x12\x44\n\tsubscribe\x12\x1d.gv_services.proto.SubRequest\x1a\x14.google.protobuf.Any\"\x00\x30\x01\x12U\n\x08get_data\x12%.gv_services.proto.TrafficDataRequest\x1a\x1e.gv_services.proto.TrafficData\"\x00\x30\x01\x12U\n\x1d\x61\x64\x64_mapping_roads_data_points\x12\x1a.gv_services.proto.Mapping\x1a\x16.gv_services.proto.Ack\"\x00\x12I\n\x0f\x61\x64\x64_data_points\x12\x1c.gv_services.proto.Locations\x1a\x16.gv_services.proto.Ack\"\x00\x12J\n\x16import_shapefile_to_db\x12\x16.google.protobuf.Empty\x1a\x16.gv_services.proto.Ack\"\x00\x12V\n\x0fget_data_points\x12#.gv_services.proto.LocationsRequest\x1a\x1c.gv_services.proto.Locations\"\x00\x12P\n\tget_roads\x12#.gv_services.proto.LocationsRequest\x1a\x1c.gv_services.proto.Locations\"\x00\x12`\n\x1dget_mapping_roads_data_points\x12!.gv_services.proto.MappingRequest\x1a\x1a.gv_services.proto.Mapping\"\x00\x12Z\n\x1bupdate_roads_freeflow_speed\x12!.gv_services.proto.FreeflowSpeeds\x1a\x16.gv_services.proto.Ack\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,gv__services_dot_proto_dot_archivist__pb2.DESCRIPTOR,gv__services_dot_proto_dot_broadcaster__pb2.DESCRIPTOR,gv__services_dot_proto_dot_common__pb2.DESCRIPTOR,gv__services_dot_proto_dot_geographer__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_INTERFACE = _descriptor.ServiceDescriptor(
  name='Interface',
  full_name='gv_services.proto.Interface',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=253,
  serialized_end=1087,
  methods=[
  _descriptor.MethodDescriptor(
    name='publish',
    full_name='gv_services.proto.Interface.publish',
    index=0,
    containing_service=None,
    input_type=gv__services_dot_proto_dot_broadcaster__pb2._PUBREQUEST,
    output_type=gv__services_dot_proto_dot_common__pb2._ACK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='subscribe',
    full_name='gv_services.proto.Interface.subscribe',
    index=1,
    containing_service=None,
    input_type=gv__services_dot_proto_dot_broadcaster__pb2._SUBREQUEST,
    output_type=google_dot_protobuf_dot_any__pb2._ANY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='get_data',
    full_name='gv_services.proto.Interface.get_data',
    index=2,
    containing_service=None,
    input_type=gv__services_dot_proto_dot_archivist__pb2._TRAFFICDATAREQUEST,
    output_type=gv__services_dot_proto_dot_archivist__pb2._TRAFFICDATA,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='add_mapping_roads_data_points',
    full_name='gv_services.proto.Interface.add_mapping_roads_data_points',
    index=3,
    containing_service=None,
    input_type=gv__services_dot_proto_dot_geographer__pb2._MAPPING,
    output_type=gv__services_dot_proto_dot_common__pb2._ACK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='add_data_points',
    full_name='gv_services.proto.Interface.add_data_points',
    index=4,
    containing_service=None,
    input_type=gv__services_dot_proto_dot_geographer__pb2._LOCATIONS,
    output_type=gv__services_dot_proto_dot_common__pb2._ACK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='import_shapefile_to_db',
    full_name='gv_services.proto.Interface.import_shapefile_to_db',
    index=5,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=gv__services_dot_proto_dot_common__pb2._ACK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='get_data_points',
    full_name='gv_services.proto.Interface.get_data_points',
    index=6,
    containing_service=None,
    input_type=gv__services_dot_proto_dot_geographer__pb2._LOCATIONSREQUEST,
    output_type=gv__services_dot_proto_dot_geographer__pb2._LOCATIONS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='get_roads',
    full_name='gv_services.proto.Interface.get_roads',
    index=7,
    containing_service=None,
    input_type=gv__services_dot_proto_dot_geographer__pb2._LOCATIONSREQUEST,
    output_type=gv__services_dot_proto_dot_geographer__pb2._LOCATIONS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='get_mapping_roads_data_points',
    full_name='gv_services.proto.Interface.get_mapping_roads_data_points',
    index=8,
    containing_service=None,
    input_type=gv__services_dot_proto_dot_geographer__pb2._MAPPINGREQUEST,
    output_type=gv__services_dot_proto_dot_geographer__pb2._MAPPING,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='update_roads_freeflow_speed',
    full_name='gv_services.proto.Interface.update_roads_freeflow_speed',
    index=9,
    containing_service=None,
    input_type=gv__services_dot_proto_dot_geographer__pb2._FREEFLOWSPEEDS,
    output_type=gv__services_dot_proto_dot_common__pb2._ACK,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_INTERFACE)

DESCRIPTOR.services_by_name['Interface'] = _INTERFACE

# @@protoc_insertion_point(module_scope)
