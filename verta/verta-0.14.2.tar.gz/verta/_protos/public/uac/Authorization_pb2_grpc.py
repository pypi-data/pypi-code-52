# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from ...public.uac import Authorization_pb2 as protos_dot_public_dot_uac_dot_Authorization__pb2


class AuthzServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.isAllowed = channel.unary_unary(
        '/ai.verta.uac.AuthzService/isAllowed',
        request_serializer=protos_dot_public_dot_uac_dot_Authorization__pb2.IsAllowed.SerializeToString,
        response_deserializer=protos_dot_public_dot_uac_dot_Authorization__pb2.IsAllowed.Response.FromString,
        )
    self.getAllowedEntities = channel.unary_unary(
        '/ai.verta.uac.AuthzService/getAllowedEntities',
        request_serializer=protos_dot_public_dot_uac_dot_Authorization__pb2.GetAllowedEntities.SerializeToString,
        response_deserializer=protos_dot_public_dot_uac_dot_Authorization__pb2.GetAllowedEntities.Response.FromString,
        )
    self.getAllowedResources = channel.unary_unary(
        '/ai.verta.uac.AuthzService/getAllowedResources',
        request_serializer=protos_dot_public_dot_uac_dot_Authorization__pb2.GetAllowedResources.SerializeToString,
        response_deserializer=protos_dot_public_dot_uac_dot_Authorization__pb2.GetAllowedResources.Response.FromString,
        )
    self.getDireclyAllowedResources = channel.unary_unary(
        '/ai.verta.uac.AuthzService/getDireclyAllowedResources',
        request_serializer=protos_dot_public_dot_uac_dot_Authorization__pb2.GetAllowedResources.SerializeToString,
        response_deserializer=protos_dot_public_dot_uac_dot_Authorization__pb2.GetAllowedResources.Response.FromString,
        )
    self.isSelfAllowed = channel.unary_unary(
        '/ai.verta.uac.AuthzService/isSelfAllowed',
        request_serializer=protos_dot_public_dot_uac_dot_Authorization__pb2.IsSelfAllowed.SerializeToString,
        response_deserializer=protos_dot_public_dot_uac_dot_Authorization__pb2.IsSelfAllowed.Response.FromString,
        )
    self.getSelfAllowedResources = channel.unary_unary(
        '/ai.verta.uac.AuthzService/getSelfAllowedResources',
        request_serializer=protos_dot_public_dot_uac_dot_Authorization__pb2.GetSelfAllowedResources.SerializeToString,
        response_deserializer=protos_dot_public_dot_uac_dot_Authorization__pb2.GetSelfAllowedResources.Response.FromString,
        )
    self.getSelfDirectlyAllowedResources = channel.unary_unary(
        '/ai.verta.uac.AuthzService/getSelfDirectlyAllowedResources',
        request_serializer=protos_dot_public_dot_uac_dot_Authorization__pb2.GetSelfAllowedResources.SerializeToString,
        response_deserializer=protos_dot_public_dot_uac_dot_Authorization__pb2.GetSelfAllowedResources.Response.FromString,
        )
    self.getSelfAllowedActionsBatch = channel.unary_unary(
        '/ai.verta.uac.AuthzService/getSelfAllowedActionsBatch',
        request_serializer=protos_dot_public_dot_uac_dot_Authorization__pb2.GetSelfAllowedActionsBatch.SerializeToString,
        response_deserializer=protos_dot_public_dot_uac_dot_Authorization__pb2.GetSelfAllowedActionsBatch.Response.FromString,
        )


class AuthzServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def isAllowed(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getAllowedEntities(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getAllowedResources(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getDireclyAllowedResources(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def isSelfAllowed(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getSelfAllowedResources(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getSelfDirectlyAllowedResources(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getSelfAllowedActionsBatch(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AuthzServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'isAllowed': grpc.unary_unary_rpc_method_handler(
          servicer.isAllowed,
          request_deserializer=protos_dot_public_dot_uac_dot_Authorization__pb2.IsAllowed.FromString,
          response_serializer=protos_dot_public_dot_uac_dot_Authorization__pb2.IsAllowed.Response.SerializeToString,
      ),
      'getAllowedEntities': grpc.unary_unary_rpc_method_handler(
          servicer.getAllowedEntities,
          request_deserializer=protos_dot_public_dot_uac_dot_Authorization__pb2.GetAllowedEntities.FromString,
          response_serializer=protos_dot_public_dot_uac_dot_Authorization__pb2.GetAllowedEntities.Response.SerializeToString,
      ),
      'getAllowedResources': grpc.unary_unary_rpc_method_handler(
          servicer.getAllowedResources,
          request_deserializer=protos_dot_public_dot_uac_dot_Authorization__pb2.GetAllowedResources.FromString,
          response_serializer=protos_dot_public_dot_uac_dot_Authorization__pb2.GetAllowedResources.Response.SerializeToString,
      ),
      'getDireclyAllowedResources': grpc.unary_unary_rpc_method_handler(
          servicer.getDireclyAllowedResources,
          request_deserializer=protos_dot_public_dot_uac_dot_Authorization__pb2.GetAllowedResources.FromString,
          response_serializer=protos_dot_public_dot_uac_dot_Authorization__pb2.GetAllowedResources.Response.SerializeToString,
      ),
      'isSelfAllowed': grpc.unary_unary_rpc_method_handler(
          servicer.isSelfAllowed,
          request_deserializer=protos_dot_public_dot_uac_dot_Authorization__pb2.IsSelfAllowed.FromString,
          response_serializer=protos_dot_public_dot_uac_dot_Authorization__pb2.IsSelfAllowed.Response.SerializeToString,
      ),
      'getSelfAllowedResources': grpc.unary_unary_rpc_method_handler(
          servicer.getSelfAllowedResources,
          request_deserializer=protos_dot_public_dot_uac_dot_Authorization__pb2.GetSelfAllowedResources.FromString,
          response_serializer=protos_dot_public_dot_uac_dot_Authorization__pb2.GetSelfAllowedResources.Response.SerializeToString,
      ),
      'getSelfDirectlyAllowedResources': grpc.unary_unary_rpc_method_handler(
          servicer.getSelfDirectlyAllowedResources,
          request_deserializer=protos_dot_public_dot_uac_dot_Authorization__pb2.GetSelfAllowedResources.FromString,
          response_serializer=protos_dot_public_dot_uac_dot_Authorization__pb2.GetSelfAllowedResources.Response.SerializeToString,
      ),
      'getSelfAllowedActionsBatch': grpc.unary_unary_rpc_method_handler(
          servicer.getSelfAllowedActionsBatch,
          request_deserializer=protos_dot_public_dot_uac_dot_Authorization__pb2.GetSelfAllowedActionsBatch.FromString,
          response_serializer=protos_dot_public_dot_uac_dot_Authorization__pb2.GetSelfAllowedActionsBatch.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ai.verta.uac.AuthzService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
