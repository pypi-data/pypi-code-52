# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from ...public.modeldb import Comment_pb2 as protos_dot_public_dot_modeldb_dot_Comment__pb2


class CommentServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.addExperimentRunComment = channel.unary_unary(
        '/ai.verta.modeldb.CommentService/addExperimentRunComment',
        request_serializer=protos_dot_public_dot_modeldb_dot_Comment__pb2.AddComment.SerializeToString,
        response_deserializer=protos_dot_public_dot_modeldb_dot_Comment__pb2.AddComment.Response.FromString,
        )
    self.updateExperimentRunComment = channel.unary_unary(
        '/ai.verta.modeldb.CommentService/updateExperimentRunComment',
        request_serializer=protos_dot_public_dot_modeldb_dot_Comment__pb2.UpdateComment.SerializeToString,
        response_deserializer=protos_dot_public_dot_modeldb_dot_Comment__pb2.UpdateComment.Response.FromString,
        )
    self.getExperimentRunComments = channel.unary_unary(
        '/ai.verta.modeldb.CommentService/getExperimentRunComments',
        request_serializer=protos_dot_public_dot_modeldb_dot_Comment__pb2.GetComments.SerializeToString,
        response_deserializer=protos_dot_public_dot_modeldb_dot_Comment__pb2.GetComments.Response.FromString,
        )
    self.deleteExperimentRunComment = channel.unary_unary(
        '/ai.verta.modeldb.CommentService/deleteExperimentRunComment',
        request_serializer=protos_dot_public_dot_modeldb_dot_Comment__pb2.DeleteComment.SerializeToString,
        response_deserializer=protos_dot_public_dot_modeldb_dot_Comment__pb2.DeleteComment.Response.FromString,
        )


class CommentServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def addExperimentRunComment(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def updateExperimentRunComment(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getExperimentRunComments(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def deleteExperimentRunComment(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CommentServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'addExperimentRunComment': grpc.unary_unary_rpc_method_handler(
          servicer.addExperimentRunComment,
          request_deserializer=protos_dot_public_dot_modeldb_dot_Comment__pb2.AddComment.FromString,
          response_serializer=protos_dot_public_dot_modeldb_dot_Comment__pb2.AddComment.Response.SerializeToString,
      ),
      'updateExperimentRunComment': grpc.unary_unary_rpc_method_handler(
          servicer.updateExperimentRunComment,
          request_deserializer=protos_dot_public_dot_modeldb_dot_Comment__pb2.UpdateComment.FromString,
          response_serializer=protos_dot_public_dot_modeldb_dot_Comment__pb2.UpdateComment.Response.SerializeToString,
      ),
      'getExperimentRunComments': grpc.unary_unary_rpc_method_handler(
          servicer.getExperimentRunComments,
          request_deserializer=protos_dot_public_dot_modeldb_dot_Comment__pb2.GetComments.FromString,
          response_serializer=protos_dot_public_dot_modeldb_dot_Comment__pb2.GetComments.Response.SerializeToString,
      ),
      'deleteExperimentRunComment': grpc.unary_unary_rpc_method_handler(
          servicer.deleteExperimentRunComment,
          request_deserializer=protos_dot_public_dot_modeldb_dot_Comment__pb2.DeleteComment.FromString,
          response_serializer=protos_dot_public_dot_modeldb_dot_Comment__pb2.DeleteComment.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ai.verta.modeldb.CommentService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
