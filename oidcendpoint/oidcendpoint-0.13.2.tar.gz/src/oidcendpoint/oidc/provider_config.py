import logging

from oidcmsg import oidc

from oidcendpoint.endpoint import Endpoint

logger = logging.getLogger(__name__)


class ProviderConfiguration(Endpoint):
    request_cls = oidc.Message
    response_cls = oidc.ProviderConfigurationResponse
    request_format = ""
    response_format = "json"
    name = "provider_config"
    default_capabilities = {"require_request_uri_registration": None}

    def __init__(self, endpoint_context, **kwargs):
        Endpoint.__init__(self, endpoint_context, **kwargs)
        self.pre_construct.append(self.add_endpoints)

    def add_endpoints(self, request, client_id, endpoint_context, **kwargs):
        for endpoint, endp_instance in self.endpoint_context.endpoint.items():
            if endpoint in [
                "authorization_endpoint",
                "registration_endpoint",
                "token_endpoint",
                "userinfo_endpoint",
                "end_session_endpoint",
            ]:
                request[endpoint] = endp_instance.endpoint_path

        return request

    def process_request(self, request=None, **kwargs):
        return {"response_args": self.endpoint_context.provider_info}
