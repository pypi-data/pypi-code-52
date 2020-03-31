import requests
from google.protobuf.empty_pb2 import Empty

from ..grpc import api

from .convert import convert_obj, errStr


class VegaTradingDataClient(object):
    """
    The Vega Trading Data Client talks to a back-end node.
    """

    def __init__(
        self,
        url: str
    ) -> None:
        if url is None:
            raise Exception("Missing node URL")
        self.url = url

        self._httpsession = requests.Session()

    # MarketAccounts,MarketAccountsRequest,MarketAccountsResponse
    # PartyAccounts,PartyAccountsRequest,PartyAccountsResponse
    # Candles,CandlesRequest,CandlesResponse
    # MarketDataByID,MarketDataByIDRequest,MarketDataByIDResponse

    def MarketsData(
        self,
        _: Empty
    ) -> api.trading.MarketsDataResponse:
        r = self._httpsession.get(
            "{}/markets-data".format(self.url))
        if r.status_code != 200:
            raise Exception(errStr(r))
        return convert_obj(r.json(), api.trading.MarketsDataResponse())

    def MarketByID(
        self,
        req: api.trading.MarketByIDRequest
    ) -> api.trading.MarketByIDResponse:
        r = self._httpsession.get(
            "{}/markets/{}".format(self.url, req.marketID))
        if r.status_code != 200:
            raise Exception(errStr(r))
        return convert_obj(r.json(), api.trading.MarketByIDResponse())

    # MarketDepth,MarketDepthRequest,MarketDepthResponse

    def Markets(
        self,
        _: Empty
    ) -> api.trading.MarketsResponse:
        r = self._httpsession.get("{}/markets".format(self.url))
        if r.status_code != 200:
            raise Exception(errStr(r))
        return convert_obj(r.json(), api.trading.MarketsResponse())

    # OrderByMarketAndID,OrderByMarketAndIdRequest,OrderByMarketAndIdResponse
    # OrderByReference,OrderByReferenceRequest,OrderByReferenceResponse
    # OrdersByMarket,OrdersByMarketRequest,OrdersByMarketResponse
    # OrdersByParty,OrdersByPartyRequest,OrdersByPartyResponse
    # MarginLevels,MarginLevelsRequest,MarginLevelsResponse
    # Parties,.google.protobuf.Empty,PartiesResponse
    # PartyByID,PartyByIDRequest,PartyByIDResponse
    # PositionsByParty,PositionsByPartyRequest,PositionsByPartyResponse
    # LastTrade,LastTradeRequest,LastTradeResponse
    # TradesByMarket,TradesByMarketRequest,TradesByMarketResponse
    # TradesByOrder,TradesByOrderRequest,TradesByOrderResponse
    # TradesByParty,TradesByPartyRequest,TradesByPartyResponse
    # Statistics,.google.protobuf.Empty,.vega.Statistics
    # GetVegaTime,.google.protobuf.Empty,VegaTimeResponse
    # AccountsSubscribe,AccountsSubscribeRequest,.vega.Account
    # CandlesSubscribe,CandlesSubscribeRequest,.vega.Candle
    # MarginLevelsSubscribe,MarginLevelsSubscribeRequest,.vega.MarginLevels
    # MarketDepthSubscribe,MarketDepthSubscribeRequest,.vega.MarketDepth
    # MarketsDataSubscribe,MarketsDataSubscribeRequest,.vega.MarketData
    # OrdersSubscribe,OrdersSubscribeRequest,OrdersStream
    # PositionsSubscribe,PositionsSubscribeRequest,.vega.Position
    # TradesSubscribe,TradesSubscribeRequest,TradesStream
    # TransferResponsesSubscribe,.google.protobuf.Empty,.vega.TransferResponse
