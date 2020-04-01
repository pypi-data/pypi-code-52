# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class DebugLinkMemoryRead(p.MessageType):
    MESSAGE_WIRE_TYPE = 110

    def __init__(
        self,
        address: int = None,
        length: int = None,
    ) -> None:
        self.address = address
        self.length = length

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('address', p.UVarintType, 0),
            2: ('length', p.UVarintType, 0),
        }
