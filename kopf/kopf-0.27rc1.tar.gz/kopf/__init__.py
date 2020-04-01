"""
The main Kopf module for all the exported functions & classes.
"""

# Unlike all other places, where we import other modules and refer
# the functions via the modules, this is the framework's top-level interface,
# as it is seen by the users. So, we export the individual functions.

from kopf import (
    on,  # as a separate name on the public namespace
)
from kopf.config import (
    LOGLEVEL_INFO,  # deprecated
    LOGLEVEL_WARNING,  # deprecated
    LOGLEVEL_ERROR,  # deprecated
    LOGLEVEL_CRITICAL,  # deprecated
    EventsConfig,  # deprecated
    WorkersConfig,  # deprecated
)
from kopf.engines.logging import (
    configure,
)
from kopf.engines.posting import (
    event,
    info,
    warn,
    exception,
)
from kopf.on import (
    daemon,
    timer,
)
from kopf.on import (
    register,
)
from kopf.reactor import (
    lifecycles,  # as a separate name on the public namespace
)
from kopf.reactor.handling import (
    TemporaryError,
    PermanentError,
    HandlerTimeoutError,
    HandlerRetriesError,
    execute,
)
from kopf.reactor.lifecycles import (
    get_default_lifecycle,
    set_default_lifecycle,
)
from kopf.reactor.registries import (
    ActivityRegistry,
    ResourceRegistry,
    ResourceWatchingRegistry,
    ResourceChangingRegistry,
    OperatorRegistry,
    get_default_registry,
    set_default_registry,
)
from kopf.reactor.running import (
    spawn_tasks,
    run_tasks,
    operator,
    run,
    login,  # deprecated
    create_tasks,  # deprecated
)
from kopf.storage.diffbase import (
    DiffBaseStorage,
    AnnotationsDiffBaseStorage,
    StatusDiffBaseStorage,
    MultiDiffBaseStorage,
)
from kopf.storage.progress import (
    ProgressStorage,
    AnnotationsProgressStorage,
    StatusProgressStorage,
    MultiProgressStorage,
    SmartProgressStorage,
)
from kopf.structs.bodies import (
    build_object_reference,
    build_owner_reference,
)
from kopf.structs.configuration import (
    OperatorSettings,
)
from kopf.structs.credentials import (
    LoginError,
    ConnectionInfo,
)
from kopf.structs.filters import (
    ABSENT,
    PRESENT,
)
from kopf.structs.handlers import (
    ErrorsMode,
)
from kopf.structs.primitives import (
    DaemonStoppingReason,
)
from kopf.toolkits.hierarchies import (
    adopt,
    label,
    harmonize_naming,
    adjust_namespace,
    append_owner_reference,
    remove_owner_reference,
)
from kopf.toolkits.legacy_registries import (
    BaseRegistry,
    SimpleRegistry,
    GlobalRegistry,
)
from kopf.utilities.piggybacking import (
    login_via_pykube,
    login_via_client,
)

HandlerFatalError = PermanentError  # a backward-compatibility alias
HandlerRetryError = TemporaryError  # a backward-compatibility alias

__all__ = [
    'on', 'lifecycles', 'register', 'execute', 'daemon', 'timer',
    'configure',
    'login', 'LoginError', 'ConnectionInfo',
    'login_via_pykube', 'login_via_client',
    'event', 'info', 'warn', 'exception',
    'spawn_tasks', 'run_tasks', 'operator', 'run', 'create_tasks',
    'adopt', 'label',
    'get_default_lifecycle', 'set_default_lifecycle',
    'build_object_reference', 'build_owner_reference',
    'append_owner_reference', 'remove_owner_reference',
    'ErrorsMode',
    'PermanentError', 'HandlerFatalError',
    'TemporaryError', 'HandlerRetryError',
    'HandlerTimeoutError',
    'HandlerRetriesError',
    'BaseRegistry',  # deprecated
    'SimpleRegistry',  # deprecated
    'GlobalRegistry',  # deprecated
    'ActivityRegistry',
    'ResourceRegistry',
    'ResourceWatchingRegistry',
    'ResourceChangingRegistry',
    'OperatorRegistry',
    'get_default_registry',
    'set_default_registry',
    'PRESENT', 'ABSENT',
    'OperatorSettings',
    'DiffBaseStorage',
    'AnnotationsDiffBaseStorage',
    'StatusDiffBaseStorage',
    'MultiDiffBaseStorage',
    'ProgressStorage',
    'AnnotationsProgressStorage',
    'StatusProgressStorage',
    'MultiProgressStorage',
    'SmartProgressStorage',
    'DaemonStoppingReason',
]
