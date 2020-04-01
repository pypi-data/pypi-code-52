# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from spaceone.api.inventory.v1 import region_pb2 as spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2


class RegionStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.create = channel.unary_unary(
        '/spaceone.api.inventory.v1.Region/create',
        request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2.CreateRegionRequest.SerializeToString,
        response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2.RegionInfo.FromString,
        )
    self.update = channel.unary_unary(
        '/spaceone.api.inventory.v1.Region/update',
        request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2.UpdateRegionRequest.SerializeToString,
        response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2.RegionInfo.FromString,
        )
    self.delete = channel.unary_unary(
        '/spaceone.api.inventory.v1.Region/delete',
        request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2.RegionRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.get = channel.unary_unary(
        '/spaceone.api.inventory.v1.Region/get',
        request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2.RegionRequest.SerializeToString,
        response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2.RegionInfo.FromString,
        )
    self.add_member = channel.unary_unary(
        '/spaceone.api.inventory.v1.Region/add_member',
        request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2.RegionMemberRequest.SerializeToString,
        response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2.RegionMemberInfo.FromString,
        )
    self.modify_member = channel.unary_unary(
        '/spaceone.api.inventory.v1.Region/modify_member',
        request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2.RegionMemberRequest.SerializeToString,
        response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2.RegionMemberInfo.FromString,
        )
    self.remove_member = channel.unary_unary(
        '/spaceone.api.inventory.v1.Region/remove_member',
        request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2.RemoveRegionMemberRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.list_members = channel.unary_unary(
        '/spaceone.api.inventory.v1.Region/list_members',
        request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2.RegionMemberQuery.SerializeToString,
        response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2.RegionMembersInfo.FromString,
        )
    self.list = channel.unary_unary(
        '/spaceone.api.inventory.v1.Region/list',
        request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2.RegionQuery.SerializeToString,
        response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2.RegionsInfo.FromString,
        )


class RegionServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def create(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def update(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def delete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def get(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def add_member(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def modify_member(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def remove_member(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def list_members(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def list(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RegionServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'create': grpc.unary_unary_rpc_method_handler(
          servicer.create,
          request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2.CreateRegionRequest.FromString,
          response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2.RegionInfo.SerializeToString,
      ),
      'update': grpc.unary_unary_rpc_method_handler(
          servicer.update,
          request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2.UpdateRegionRequest.FromString,
          response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2.RegionInfo.SerializeToString,
      ),
      'delete': grpc.unary_unary_rpc_method_handler(
          servicer.delete,
          request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2.RegionRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'get': grpc.unary_unary_rpc_method_handler(
          servicer.get,
          request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2.RegionRequest.FromString,
          response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2.RegionInfo.SerializeToString,
      ),
      'add_member': grpc.unary_unary_rpc_method_handler(
          servicer.add_member,
          request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2.RegionMemberRequest.FromString,
          response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2.RegionMemberInfo.SerializeToString,
      ),
      'modify_member': grpc.unary_unary_rpc_method_handler(
          servicer.modify_member,
          request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2.RegionMemberRequest.FromString,
          response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2.RegionMemberInfo.SerializeToString,
      ),
      'remove_member': grpc.unary_unary_rpc_method_handler(
          servicer.remove_member,
          request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2.RemoveRegionMemberRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'list_members': grpc.unary_unary_rpc_method_handler(
          servicer.list_members,
          request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2.RegionMemberQuery.FromString,
          response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2.RegionMembersInfo.SerializeToString,
      ),
      'list': grpc.unary_unary_rpc_method_handler(
          servicer.list,
          request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2.RegionQuery.FromString,
          response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_region__pb2.RegionsInfo.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'spaceone.api.inventory.v1.Region', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
