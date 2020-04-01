# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from spaceone.api.secret.v1 import secret_pb2 as spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2


class SecretStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.create = channel.unary_unary(
        '/spaceone.api.secret.v1.Secret/create',
        request_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.CreateSecretRequest.SerializeToString,
        response_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretInfo.FromString,
        )
    self.update = channel.unary_unary(
        '/spaceone.api.secret.v1.Secret/update',
        request_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.UpdateSecretRequest.SerializeToString,
        response_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretInfo.FromString,
        )
    self.delete = channel.unary_unary(
        '/spaceone.api.secret.v1.Secret/delete',
        request_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.get_data = channel.unary_unary(
        '/spaceone.api.secret.v1.Secret/get_data',
        request_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretRequest.SerializeToString,
        response_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretDataInfo.FromString,
        )
    self.get = channel.unary_unary(
        '/spaceone.api.secret.v1.Secret/get',
        request_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretRequest.SerializeToString,
        response_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretInfo.FromString,
        )
    self.list = channel.unary_unary(
        '/spaceone.api.secret.v1.Secret/list',
        request_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretQuery.SerializeToString,
        response_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretsInfo.FromString,
        )


class SecretServicer(object):
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

  def get_data(self, request, context):
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

  def list(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SecretServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'create': grpc.unary_unary_rpc_method_handler(
          servicer.create,
          request_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.CreateSecretRequest.FromString,
          response_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretInfo.SerializeToString,
      ),
      'update': grpc.unary_unary_rpc_method_handler(
          servicer.update,
          request_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.UpdateSecretRequest.FromString,
          response_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretInfo.SerializeToString,
      ),
      'delete': grpc.unary_unary_rpc_method_handler(
          servicer.delete,
          request_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'get_data': grpc.unary_unary_rpc_method_handler(
          servicer.get_data,
          request_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretRequest.FromString,
          response_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretDataInfo.SerializeToString,
      ),
      'get': grpc.unary_unary_rpc_method_handler(
          servicer.get,
          request_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretRequest.FromString,
          response_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretInfo.SerializeToString,
      ),
      'list': grpc.unary_unary_rpc_method_handler(
          servicer.list,
          request_deserializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretQuery.FromString,
          response_serializer=spaceone_dot_api_dot_secret_dot_v1_dot_secret__pb2.SecretsInfo.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'spaceone.api.secret.v1.Secret', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
