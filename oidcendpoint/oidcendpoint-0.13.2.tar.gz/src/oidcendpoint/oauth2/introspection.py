"""Implements RFC7662"""
import logging

from oidcmsg import oauth2
from oidcmsg.time_util import utc_time_sans_frac

from oidcendpoint.endpoint import Endpoint

LOGGER = logging.getLogger(__name__)


class Introspection(Endpoint):
    """Implements RFC 7662"""

    request_cls = oauth2.TokenIntrospectionRequest
    response_cls = oauth2.TokenIntrospectionResponse
    request_format = "urlencoded"
    response_format = "json"
    endpoint_name = "introspection_endpoint"
    name = "introspection"

    def __init__(self, **kwargs):
        Endpoint.__init__(self, **kwargs)
        self.offset = kwargs.get("offset", 0)

    def get_client_id_from_token(self, endpoint_context, token, request=None):
        """
        Will try to match tokens against information in the session DB.

        :param endpoint_context:
        :param token:
        :param request:
        :return: client_id if there was a match
        """
        sinfo = endpoint_context.sdb[token]
        return sinfo["authn_req"]["client_id"]

    def _introspect(self, token):
        try:
            info = self.endpoint_context.sdb[token]
        except KeyError:
            return None

        # Make sure that the token is an access_token or a refresh_token
        if token not in info.get("access_token") and token != info.get(
            "refresh_token"
        ):
            return None

        eat = info.get("expires_at")
        if eat and eat < utc_time_sans_frac():
            return None

        if info:  # Now what can be returned ?
            ret = info.to_dict()
            ret["iss"] = self.endpoint_context.issuer

            if "scope" not in ret:
                ret["scope"] = " ".join(info["authn_req"]["scope"])

            return ret

    def process_request(self, request=None, **kwargs):
        """

        :param request: The authorization request as a dictionary
        :param kwargs:
        :return:
        """
        _introspect_request = self.request_cls(**request)
        if "error" in _introspect_request:
            return _introspect_request

        _token = _introspect_request["token"]
        _resp = self.response_cls(active=False)

        _info = self._introspect(_token)
        if _info is None:
            return {"response_args": _resp}

        if "release" in self.kwargs:
            if "username" in self.kwargs["release"]:
                try:
                    _info["username"] = self.endpoint_context.userinfo.search(
                        sub=_info["sub"]
                    )
                except KeyError:
                    pass

        _resp.update(_info)
        _resp.weed()
        _resp["active"] = True

        return {"response_args": _resp}
