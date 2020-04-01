class EosRpcException(Exception):
    """Base EOS exception"""


class EosAccountExistsException(EosRpcException):
    """Thrown by create_wallet where account with given name already exists"""


class EosAccountDoesntExistException(EosRpcException):
    """Thrown by get_account where account doesn't exist"""


class EosActionValidateException(EosRpcException):
    """Raised when action payload is invalid"""


class EosMissingTaposFieldsException(EosRpcException):
    """TAPOS fields are missing from Transaction object"""


class EosSerializerUnsupportedTypeException(EosRpcException):
    """Our serializer doesn't support provided object type, shouldn't happen"""


class EosDeadlineException(EosRpcException):
    """Transaction timed out"""


class EosTxCpuUsageExceededException(EosRpcException):
    """Not enough EOS were staked for CPU"""


class EosTxNetUsageExceededException(EosRpcException):
    """Not enough EOS were staked for NET"""


class EosRamUsageExceededException(EosRpcException):
    """Transaction requires more RAM than what's available on the account"""


class EosAssertMessageException(EosRpcException):
    """
    Generic assertion error from smart contract, can mean literally anything,
    need to parse C++ traceback to figure out what went wrong.
    """
