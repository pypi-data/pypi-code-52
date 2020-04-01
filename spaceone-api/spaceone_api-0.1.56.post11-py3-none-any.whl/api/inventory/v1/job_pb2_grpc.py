# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from spaceone.api.inventory.v1 import job_pb2 as spaceone_dot_api_dot_inventory_dot_v1_dot_job__pb2


class JobStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.list = channel.unary_unary(
        '/spaceone.api.inventory.v1.Job/list',
        request_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_job__pb2.JobsQuery.SerializeToString,
        response_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_job__pb2.JobsInfo.FromString,
        )


class JobServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def list(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_JobServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'list': grpc.unary_unary_rpc_method_handler(
          servicer.list,
          request_deserializer=spaceone_dot_api_dot_inventory_dot_v1_dot_job__pb2.JobsQuery.FromString,
          response_serializer=spaceone_dot_api_dot_inventory_dot_v1_dot_job__pb2.JobsInfo.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'spaceone.api.inventory.v1.Job', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
