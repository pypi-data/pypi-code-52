# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: gv_services/proto/interface.proto
# plugin: grpclib.plugin.main
import abc

import grpclib.const
import grpclib.client

import google.protobuf.any_pb2
import google.protobuf.empty_pb2
import gv_services.proto.archivist_pb2
import gv_services.proto.broadcaster_pb2
import gv_services.proto.common_pb2
import gv_services.proto.geographer_pb2
import gv_services.proto.interface_pb2


class InterfaceBase(abc.ABC):

    @abc.abstractmethod
    async def publish(self, stream):
        pass

    @abc.abstractmethod
    async def subscribe(self, stream):
        pass

    @abc.abstractmethod
    async def get_data(self, stream):
        pass

    @abc.abstractmethod
    async def add_mapping_roads_data_points(self, stream):
        pass

    @abc.abstractmethod
    async def add_data_points(self, stream):
        pass

    @abc.abstractmethod
    async def import_shapefile_to_db(self, stream):
        pass

    @abc.abstractmethod
    async def get_data_points(self, stream):
        pass

    @abc.abstractmethod
    async def get_roads(self, stream):
        pass

    @abc.abstractmethod
    async def get_mapping_roads_data_points(self, stream):
        pass

    @abc.abstractmethod
    async def get_mapping_zones_roads(self, stream):
        pass

    @abc.abstractmethod
    async def update_roads_freeflow_speed(self, stream):
        pass

    def __mapping__(self):
        return {
            '/gv_services.proto.Interface/publish': grpclib.const.Handler(
                self.publish,
                grpclib.const.Cardinality.UNARY_UNARY,
                gv_services.proto.broadcaster_pb2.PubRequest,
                gv_services.proto.common_pb2.Ack,
            ),
            '/gv_services.proto.Interface/subscribe': grpclib.const.Handler(
                self.subscribe,
                grpclib.const.Cardinality.UNARY_STREAM,
                gv_services.proto.broadcaster_pb2.SubRequest,
                google.protobuf.any_pb2.Any,
            ),
            '/gv_services.proto.Interface/get_data': grpclib.const.Handler(
                self.get_data,
                grpclib.const.Cardinality.UNARY_STREAM,
                gv_services.proto.archivist_pb2.TrafficDataRequest,
                gv_services.proto.archivist_pb2.TrafficData,
            ),
            '/gv_services.proto.Interface/add_mapping_roads_data_points': grpclib.const.Handler(
                self.add_mapping_roads_data_points,
                grpclib.const.Cardinality.UNARY_UNARY,
                gv_services.proto.geographer_pb2.Mapping,
                gv_services.proto.common_pb2.Ack,
            ),
            '/gv_services.proto.Interface/add_data_points': grpclib.const.Handler(
                self.add_data_points,
                grpclib.const.Cardinality.UNARY_UNARY,
                gv_services.proto.geographer_pb2.Locations,
                gv_services.proto.common_pb2.Ack,
            ),
            '/gv_services.proto.Interface/import_shapefile_to_db': grpclib.const.Handler(
                self.import_shapefile_to_db,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.protobuf.empty_pb2.Empty,
                gv_services.proto.common_pb2.Ack,
            ),
            '/gv_services.proto.Interface/get_data_points': grpclib.const.Handler(
                self.get_data_points,
                grpclib.const.Cardinality.UNARY_UNARY,
                gv_services.proto.geographer_pb2.LocationsRequest,
                gv_services.proto.geographer_pb2.Locations,
            ),
            '/gv_services.proto.Interface/get_roads': grpclib.const.Handler(
                self.get_roads,
                grpclib.const.Cardinality.UNARY_UNARY,
                gv_services.proto.geographer_pb2.LocationsRequest,
                gv_services.proto.geographer_pb2.Locations,
            ),
            '/gv_services.proto.Interface/get_mapping_roads_data_points': grpclib.const.Handler(
                self.get_mapping_roads_data_points,
                grpclib.const.Cardinality.UNARY_UNARY,
                gv_services.proto.geographer_pb2.MappingRequest,
                gv_services.proto.geographer_pb2.Mapping,
            ),
            '/gv_services.proto.Interface/get_mapping_zones_roads': grpclib.const.Handler(
                self.get_mapping_zones_roads,
                grpclib.const.Cardinality.UNARY_UNARY,
                gv_services.proto.geographer_pb2.MappingRequest,
                gv_services.proto.geographer_pb2.Mapping,
            ),
            '/gv_services.proto.Interface/update_roads_freeflow_speed': grpclib.const.Handler(
                self.update_roads_freeflow_speed,
                grpclib.const.Cardinality.UNARY_UNARY,
                gv_services.proto.geographer_pb2.FreeflowSpeeds,
                gv_services.proto.common_pb2.Ack,
            ),
        }


class InterfaceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.publish = grpclib.client.UnaryUnaryMethod(
            channel,
            '/gv_services.proto.Interface/publish',
            gv_services.proto.broadcaster_pb2.PubRequest,
            gv_services.proto.common_pb2.Ack,
        )
        self.subscribe = grpclib.client.UnaryStreamMethod(
            channel,
            '/gv_services.proto.Interface/subscribe',
            gv_services.proto.broadcaster_pb2.SubRequest,
            google.protobuf.any_pb2.Any,
        )
        self.get_data = grpclib.client.UnaryStreamMethod(
            channel,
            '/gv_services.proto.Interface/get_data',
            gv_services.proto.archivist_pb2.TrafficDataRequest,
            gv_services.proto.archivist_pb2.TrafficData,
        )
        self.add_mapping_roads_data_points = grpclib.client.UnaryUnaryMethod(
            channel,
            '/gv_services.proto.Interface/add_mapping_roads_data_points',
            gv_services.proto.geographer_pb2.Mapping,
            gv_services.proto.common_pb2.Ack,
        )
        self.add_data_points = grpclib.client.UnaryUnaryMethod(
            channel,
            '/gv_services.proto.Interface/add_data_points',
            gv_services.proto.geographer_pb2.Locations,
            gv_services.proto.common_pb2.Ack,
        )
        self.import_shapefile_to_db = grpclib.client.UnaryUnaryMethod(
            channel,
            '/gv_services.proto.Interface/import_shapefile_to_db',
            google.protobuf.empty_pb2.Empty,
            gv_services.proto.common_pb2.Ack,
        )
        self.get_data_points = grpclib.client.UnaryUnaryMethod(
            channel,
            '/gv_services.proto.Interface/get_data_points',
            gv_services.proto.geographer_pb2.LocationsRequest,
            gv_services.proto.geographer_pb2.Locations,
        )
        self.get_roads = grpclib.client.UnaryUnaryMethod(
            channel,
            '/gv_services.proto.Interface/get_roads',
            gv_services.proto.geographer_pb2.LocationsRequest,
            gv_services.proto.geographer_pb2.Locations,
        )
        self.get_mapping_roads_data_points = grpclib.client.UnaryUnaryMethod(
            channel,
            '/gv_services.proto.Interface/get_mapping_roads_data_points',
            gv_services.proto.geographer_pb2.MappingRequest,
            gv_services.proto.geographer_pb2.Mapping,
        )
        self.get_mapping_zones_roads = grpclib.client.UnaryUnaryMethod(
            channel,
            '/gv_services.proto.Interface/get_mapping_zones_roads',
            gv_services.proto.geographer_pb2.MappingRequest,
            gv_services.proto.geographer_pb2.Mapping,
        )
        self.update_roads_freeflow_speed = grpclib.client.UnaryUnaryMethod(
            channel,
            '/gv_services.proto.Interface/update_roads_freeflow_speed',
            gv_services.proto.geographer_pb2.FreeflowSpeeds,
            gv_services.proto.common_pb2.Ack,
        )
