# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class ApplyFlags(p.MessageType):
    MESSAGE_WIRE_TYPE = 28

    def __init__(
        self,
        flags: int = None,
    ) -> None:
        self.flags = flags

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('flags', p.UVarintType, 0),
        }
