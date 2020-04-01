# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import analyzer_pb2 as analyzer__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import plugin_pb2 as plugin__pb2


class AnalyzerStub(object):
  """Analyzer provides a pluggable interface for checking resource definitions against some number of
  resource policies. It is intentionally open-ended, allowing for implementations that check
  everything from raw resource definitions to entire projects/stacks/snapshots for arbitrary
  issues -- style, policy, correctness, security, and so on.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Analyze = channel.unary_unary(
        '/pulumirpc.Analyzer/Analyze',
        request_serializer=analyzer__pb2.AnalyzeRequest.SerializeToString,
        response_deserializer=analyzer__pb2.AnalyzeResponse.FromString,
        )
    self.AnalyzeStack = channel.unary_unary(
        '/pulumirpc.Analyzer/AnalyzeStack',
        request_serializer=analyzer__pb2.AnalyzeStackRequest.SerializeToString,
        response_deserializer=analyzer__pb2.AnalyzeResponse.FromString,
        )
    self.GetAnalyzerInfo = channel.unary_unary(
        '/pulumirpc.Analyzer/GetAnalyzerInfo',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=analyzer__pb2.AnalyzerInfo.FromString,
        )
    self.GetPluginInfo = channel.unary_unary(
        '/pulumirpc.Analyzer/GetPluginInfo',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=plugin__pb2.PluginInfo.FromString,
        )
    self.Configure = channel.unary_unary(
        '/pulumirpc.Analyzer/Configure',
        request_serializer=analyzer__pb2.ConfigureAnalyzerRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class AnalyzerServicer(object):
  """Analyzer provides a pluggable interface for checking resource definitions against some number of
  resource policies. It is intentionally open-ended, allowing for implementations that check
  everything from raw resource definitions to entire projects/stacks/snapshots for arbitrary
  issues -- style, policy, correctness, security, and so on.
  """

  def Analyze(self, request, context):
    """Analyze analyzes a single resource object, and returns any errors that it finds.
    Called with the "inputs" to the resource, before it is updated.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AnalyzeStack(self, request, context):
    """AnalyzeStack analyzes all resources within a stack, at the end of a successful
    preview or update. The provided resources are the "outputs", after any mutations
    have taken place.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAnalyzerInfo(self, request, context):
    """GetAnalyzerInfo returns metadata about the analyzer (e.g., list of policies contained).
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPluginInfo(self, request, context):
    """GetPluginInfo returns generic information about this plugin, like its version.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Configure(self, request, context):
    """Configure configures the analyzer, passing configuration properties for each policy.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AnalyzerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Analyze': grpc.unary_unary_rpc_method_handler(
          servicer.Analyze,
          request_deserializer=analyzer__pb2.AnalyzeRequest.FromString,
          response_serializer=analyzer__pb2.AnalyzeResponse.SerializeToString,
      ),
      'AnalyzeStack': grpc.unary_unary_rpc_method_handler(
          servicer.AnalyzeStack,
          request_deserializer=analyzer__pb2.AnalyzeStackRequest.FromString,
          response_serializer=analyzer__pb2.AnalyzeResponse.SerializeToString,
      ),
      'GetAnalyzerInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetAnalyzerInfo,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=analyzer__pb2.AnalyzerInfo.SerializeToString,
      ),
      'GetPluginInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetPluginInfo,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=plugin__pb2.PluginInfo.SerializeToString,
      ),
      'Configure': grpc.unary_unary_rpc_method_handler(
          servicer.Configure,
          request_deserializer=analyzer__pb2.ConfigureAnalyzerRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'pulumirpc.Analyzer', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
