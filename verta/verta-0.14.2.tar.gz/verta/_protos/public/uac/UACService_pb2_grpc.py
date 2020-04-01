# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from ...public.uac import UACService_pb2 as protos_dot_public_dot_uac_dot_UACService__pb2


class UACServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.getCurrentUser = channel.unary_unary(
        '/ai.verta.uac.UACService/getCurrentUser',
        request_serializer=protos_dot_public_dot_uac_dot_UACService__pb2.Empty.SerializeToString,
        response_deserializer=protos_dot_public_dot_uac_dot_UACService__pb2.UserInfo.FromString,
        )
    self.getUser = channel.unary_unary(
        '/ai.verta.uac.UACService/getUser',
        request_serializer=protos_dot_public_dot_uac_dot_UACService__pb2.GetUser.SerializeToString,
        response_deserializer=protos_dot_public_dot_uac_dot_UACService__pb2.UserInfo.FromString,
        )
    self.getUsers = channel.unary_unary(
        '/ai.verta.uac.UACService/getUsers',
        request_serializer=protos_dot_public_dot_uac_dot_UACService__pb2.GetUsers.SerializeToString,
        response_deserializer=protos_dot_public_dot_uac_dot_UACService__pb2.GetUsers.Response.FromString,
        )
    self.createUser = channel.unary_unary(
        '/ai.verta.uac.UACService/createUser',
        request_serializer=protos_dot_public_dot_uac_dot_UACService__pb2.CreateUser.SerializeToString,
        response_deserializer=protos_dot_public_dot_uac_dot_UACService__pb2.CreateUser.Response.FromString,
        )
    self.updateUser = channel.unary_unary(
        '/ai.verta.uac.UACService/updateUser',
        request_serializer=protos_dot_public_dot_uac_dot_UACService__pb2.UpdateUser.SerializeToString,
        response_deserializer=protos_dot_public_dot_uac_dot_UACService__pb2.UpdateUser.Response.FromString,
        )
    self.deleteUser = channel.unary_unary(
        '/ai.verta.uac.UACService/deleteUser',
        request_serializer=protos_dot_public_dot_uac_dot_UACService__pb2.DeleteUser.SerializeToString,
        response_deserializer=protos_dot_public_dot_uac_dot_UACService__pb2.DeleteUser.Response.FromString,
        )


class UACServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def getCurrentUser(self, request, context):
    """Get the current user information verifying JWT token
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getUser(self, request, context):
    """Get the current user information verifying JWT token
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getUsers(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def createUser(self, request, context):
    """For now, any user can create a new user
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def updateUser(self, request, context):
    """Only current user can update themselves
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def deleteUser(self, request, context):
    """Only current user can delete themselves
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_UACServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'getCurrentUser': grpc.unary_unary_rpc_method_handler(
          servicer.getCurrentUser,
          request_deserializer=protos_dot_public_dot_uac_dot_UACService__pb2.Empty.FromString,
          response_serializer=protos_dot_public_dot_uac_dot_UACService__pb2.UserInfo.SerializeToString,
      ),
      'getUser': grpc.unary_unary_rpc_method_handler(
          servicer.getUser,
          request_deserializer=protos_dot_public_dot_uac_dot_UACService__pb2.GetUser.FromString,
          response_serializer=protos_dot_public_dot_uac_dot_UACService__pb2.UserInfo.SerializeToString,
      ),
      'getUsers': grpc.unary_unary_rpc_method_handler(
          servicer.getUsers,
          request_deserializer=protos_dot_public_dot_uac_dot_UACService__pb2.GetUsers.FromString,
          response_serializer=protos_dot_public_dot_uac_dot_UACService__pb2.GetUsers.Response.SerializeToString,
      ),
      'createUser': grpc.unary_unary_rpc_method_handler(
          servicer.createUser,
          request_deserializer=protos_dot_public_dot_uac_dot_UACService__pb2.CreateUser.FromString,
          response_serializer=protos_dot_public_dot_uac_dot_UACService__pb2.CreateUser.Response.SerializeToString,
      ),
      'updateUser': grpc.unary_unary_rpc_method_handler(
          servicer.updateUser,
          request_deserializer=protos_dot_public_dot_uac_dot_UACService__pb2.UpdateUser.FromString,
          response_serializer=protos_dot_public_dot_uac_dot_UACService__pb2.UpdateUser.Response.SerializeToString,
      ),
      'deleteUser': grpc.unary_unary_rpc_method_handler(
          servicer.deleteUser,
          request_deserializer=protos_dot_public_dot_uac_dot_UACService__pb2.DeleteUser.FromString,
          response_serializer=protos_dot_public_dot_uac_dot_UACService__pb2.DeleteUser.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ai.verta.uac.UACService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
