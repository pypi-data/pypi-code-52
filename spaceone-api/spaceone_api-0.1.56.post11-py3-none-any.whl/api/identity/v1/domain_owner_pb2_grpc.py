# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from spaceone.api.identity.v1 import domain_owner_pb2 as spaceone_dot_api_dot_identity_dot_v1_dot_domain__owner__pb2


class DomainOwnerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.create = channel.unary_unary(
        '/spaceone.api.identity.v1.DomainOwner/create',
        request_serializer=spaceone_dot_api_dot_identity_dot_v1_dot_domain__owner__pb2.CreateDomainOwner.SerializeToString,
        response_deserializer=spaceone_dot_api_dot_identity_dot_v1_dot_domain__owner__pb2.DomainOwnerInfo.FromString,
        )
    self.update = channel.unary_unary(
        '/spaceone.api.identity.v1.DomainOwner/update',
        request_serializer=spaceone_dot_api_dot_identity_dot_v1_dot_domain__owner__pb2.UpdateDomainOwner.SerializeToString,
        response_deserializer=spaceone_dot_api_dot_identity_dot_v1_dot_domain__owner__pb2.DomainOwnerInfo.FromString,
        )
    self.delete = channel.unary_unary(
        '/spaceone.api.identity.v1.DomainOwner/delete',
        request_serializer=spaceone_dot_api_dot_identity_dot_v1_dot_domain__owner__pb2.DomainOwnerRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.get = channel.unary_unary(
        '/spaceone.api.identity.v1.DomainOwner/get',
        request_serializer=spaceone_dot_api_dot_identity_dot_v1_dot_domain__owner__pb2.DomainOwnerRequest.SerializeToString,
        response_deserializer=spaceone_dot_api_dot_identity_dot_v1_dot_domain__owner__pb2.DomainOwnerInfo.FromString,
        )


class DomainOwnerServicer(object):
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


def add_DomainOwnerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'create': grpc.unary_unary_rpc_method_handler(
          servicer.create,
          request_deserializer=spaceone_dot_api_dot_identity_dot_v1_dot_domain__owner__pb2.CreateDomainOwner.FromString,
          response_serializer=spaceone_dot_api_dot_identity_dot_v1_dot_domain__owner__pb2.DomainOwnerInfo.SerializeToString,
      ),
      'update': grpc.unary_unary_rpc_method_handler(
          servicer.update,
          request_deserializer=spaceone_dot_api_dot_identity_dot_v1_dot_domain__owner__pb2.UpdateDomainOwner.FromString,
          response_serializer=spaceone_dot_api_dot_identity_dot_v1_dot_domain__owner__pb2.DomainOwnerInfo.SerializeToString,
      ),
      'delete': grpc.unary_unary_rpc_method_handler(
          servicer.delete,
          request_deserializer=spaceone_dot_api_dot_identity_dot_v1_dot_domain__owner__pb2.DomainOwnerRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'get': grpc.unary_unary_rpc_method_handler(
          servicer.get,
          request_deserializer=spaceone_dot_api_dot_identity_dot_v1_dot_domain__owner__pb2.DomainOwnerRequest.FromString,
          response_serializer=spaceone_dot_api_dot_identity_dot_v1_dot_domain__owner__pb2.DomainOwnerInfo.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'spaceone.api.identity.v1.DomainOwner', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
