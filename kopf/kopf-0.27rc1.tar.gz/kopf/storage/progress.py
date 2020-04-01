"""
State stores are used to track the handlers' states across handling cycles.

Specifically, they track which handlers are finished, which are not yet,
and how many retries were there, and some other information.

There could be more than one low-level k8s watch-events per one actual
high-level kopf-event (a cause). The handlers are called at different times,
and the overall handling routine should persist the handler status somewhere.

When the full event cycle is executed (possibly including multiple re-runs),
the state of all involved handlers is purged. The life-long persistence of state
is not intended: otherwise, multiple distinct causes will clutter the status
and collide with each other (especially critical for multiple updates).

Other unrelated handlers (e.g. from other operators) can co-exist with
the involved handlers (if stored in the resource itself), as the handler states
are independent of each other, and are purged individually, not all at once.

---

Originally, the handlers' state was persisted in ``.status.kopf.progress``.
But due to stricter Kubernetes schemas for built-in resources, they had to
move to annotations. As part of such move, any state persistence engines
are made possible by inheriting and overriding the base classes, though it is
considered an advanced use-case and is only briefly mentioned in the docs.

In all cases, the persisted state for each handler is a fixed-structure dict
with the following keys:

* ``started`` is a timestamp when the handler was first called.
* ``stopped`` is a timestamp when the handler either finished or failed.
* ``delayed`` is a timestamp when the handler should be invoked again (retried).
* ``retries`` is a number of retries so far or in total (if succeeded/failed).
* ``success`` is a boolean flag for a final success (no re-executions).
* ``failure`` is a boolean flag for a final failure (no retries).
* ``message`` is a descriptive message of the last error (an exception).

All timestamps are strings in ISO8601 format in UTC (no explicit ``Z`` suffix).
"""
import abc
import copy
import json
from typing import Optional, Collection, Mapping, Dict, Any, cast

from typing_extensions import TypedDict

from kopf.structs import bodies
from kopf.structs import dicts
from kopf.structs import handlers
from kopf.structs import patches


class ProgressRecord(TypedDict, total=True):
    """ A single record stored for persistence of a single handler. """
    started: Optional[str]
    stopped: Optional[str]
    delayed: Optional[str]
    retries: Optional[int]
    success: Optional[bool]
    failure: Optional[bool]
    message: Optional[str]


class ProgressStorage(metaclass=abc.ABCMeta):
    """
    Base class and an interface for all persistent states.

    The state is persisted strict per-handler, not for all handlers at once:
    to support overlapping operators (assuming different handler ids) storing
    their state on the same fields of the resource (e.g. ``state.kopf``).

    This also ensures that no extra logic for state merges will be needed:
    the handler states are atomic (i.e. state fields are not used separately)
    but independent: i.e. handlers should be persisted on their own, unrelated
    to other handlers; i.e. never combined to other atomic structures.

    If combining is still needed with performance optimization in mind (e.g.
    for relational/transactional databases), the keys can be cached in memory
    for short time, and ``flush()`` can be overridden to actually store them.
    """

    @abc.abstractmethod
    def fetch(
            self,
            *,
            key: handlers.HandlerId,
            body: bodies.Body,
    ) -> Optional[ProgressRecord]:
        raise NotImplementedError

    @abc.abstractmethod
    def store(
            self,
            *,
            key: handlers.HandlerId,
            record: ProgressRecord,
            body: bodies.Body,
            patch: patches.Patch,
    ) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def purge(
            self,
            *,
            key: handlers.HandlerId,
            body: bodies.Body,
            patch: patches.Patch,
    ) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def clear(self, *, essence: bodies.BodyEssence) -> bodies.BodyEssence:
        return copy.deepcopy(essence)

    def flush(self) -> None:
        pass


class AnnotationsProgressStorage(ProgressStorage):
    """
    State storage in ``.metadata.annotations`` with JSON-serialised content.

    An example without a prefix:

    .. code-block: yaml

        metadata:
          annotations:
            create_fn_1: '{"started": "2020-02-14T16:58:25.396364", "stopped":
                           "2020-02-14T16:58:25.401844", "retries": 1, "success": true}'
            create_fn_2: '{"started": "2020-02-14T16:58:25.396421", "retries": 0}'
        spec: ...
        status: ...

    An example with a prefix:

    .. code-block: yaml

        metadata:
          annotations:
            kopf.zalando.org/create_fn_1: '{"started": "2020-02-14T16:58:25.396364", "stopped":
                                    "2020-02-14T16:58:25.401844", "retries": 1, "success": true}'
            kopf.zalando.org/create_fn_2: '{"started": "2020-02-14T16:58:25.396421", "retries": 0}'
        spec: ...
        status: ...
    """

    def __init__(
            self,
            *,
            prefix: Optional[str] = 'kopf.zalando.org',
            verbose: bool = False,
    ) -> None:
        super().__init__()
        self.prefix = prefix
        self.verbose = verbose

    def fetch(
            self,
            *,
            key: handlers.HandlerId,
            body: bodies.Body,
    ) -> Optional[ProgressRecord]:
        safe_key = key.replace('/', '.')
        full_key = f'{self.prefix}/{safe_key}' if self.prefix else safe_key
        value = body.metadata.annotations.get(full_key, None)
        content = json.loads(value) if value is not None else None
        return cast(Optional[ProgressRecord], content)

    def store(
            self,
            *,
            key: handlers.HandlerId,
            record: ProgressRecord,
            body: bodies.Body,
            patch: patches.Patch,
    ) -> None:
        safe_key = key.replace('/', '.')
        full_key = f'{self.prefix}/{safe_key}' if self.prefix else safe_key
        clean_data = {key: val for key, val in record.items() if self.verbose or val is not None}
        patch.meta.annotations[full_key] = json.dumps(clean_data)

    def purge(
            self,
            *,
            key: handlers.HandlerId,
            body: bodies.Body,
            patch: patches.Patch,
    ) -> None:
        safe_key = key.replace('/', '.')
        full_key = f'{self.prefix}/{safe_key}' if self.prefix else safe_key
        if full_key in body.metadata.annotations or full_key in patch.meta.annotations:
            patch.meta.annotations[full_key] = None

    def clear(self, *, essence: bodies.BodyEssence) -> bodies.BodyEssence:
        essence = super().clear(essence=essence)
        annotations = essence.get('metadata', {}).get('annotations', {})
        for name in list(annotations.keys()):
            if name.startswith(f'{self.prefix}/'):
                del annotations[name]
        return essence


class StatusProgressStorage(ProgressStorage):
    """
    State storage in ``.status`` stanza with deep structure.

    The structure is this:

    .. code-block: yaml

        metadata: ...
        spec: ...
        status: ...
            kopf:
                progress:
                    handler1:
                        started: 2018-12-31T23:59:59,999999
                        stopped: 2018-01-01T12:34:56,789000
                        success: true
                    handler2:
                        started: 2018-12-31T23:59:59,999999
                        stopped: 2018-01-01T12:34:56,789000
                        failure: true
                        message: "Error message."
                    handler3:
                        started: 2018-12-31T23:59:59,999999
                        retries: 30
                    handler3/sub1:
                        started: 2018-12-31T23:59:59,999999
                        delayed: 2018-01-01T12:34:56,789000
                        retries: 10
                        message: "Not ready yet."
                    handler3/sub2:
                        started: 2018-12-31T23:59:59,999999
    """

    def __init__(
            self,
            *,
            name: str = 'kopf',
            field: dicts.FieldSpec = 'status.{name}.progress',
    ) -> None:
        super().__init__()
        self._name = name
        real_field = field.format(name=self._name) if isinstance(field, str) else field
        self._field = dicts.parse_field(real_field)

    @property
    def field(self) -> dicts.FieldPath:
        return self._field

    @field.setter
    def field(self, field: dicts.FieldSpec) -> None:
        real_field = field.format(name=self._name) if isinstance(field, str) else field
        self._field = dicts.parse_field(real_field)

    def fetch(
            self,
            *,
            key: handlers.HandlerId,
            body: bodies.Body,
    ) -> Optional[ProgressRecord]:
        container: Mapping[handlers.HandlerId, ProgressRecord]
        container = dicts.resolve(body, self.field, {})
        return container.get(key, None)

    def store(
            self,
            *,
            key: handlers.HandlerId,
            record: ProgressRecord,
            body: bodies.Body,
            patch: patches.Patch,
    ) -> None:
        # Nones are cleaned by K8s API itself.
        dicts.ensure(patch, self.field + (key,), record)

    def purge(
            self,
            *,
            key: handlers.HandlerId,
            body: bodies.Body,
            patch: patches.Patch,
    ) -> None:
        absent = object()
        key_field = self.field + (key,)
        body_value = dicts.resolve(body, key_field, absent, assume_empty=True)
        patch_value = dicts.resolve(patch, key_field, absent, assume_empty=True)
        if body_value is not absent:
            dicts.ensure(patch, key_field, None)
        elif patch_value is not absent:
            dicts.remove(patch, key_field)

    def clear(self, *, essence: bodies.BodyEssence) -> bodies.BodyEssence:
        essence = super().clear(essence=essence)

        # Work around an issue with mypy not treating TypedDicts as MutableMappings.
        essence_dict = cast(Dict[Any, Any], essence)
        dicts.remove(essence_dict, self.field)

        return essence


class MultiProgressStorage(ProgressStorage):

    def __init__(
            self,
            storages: Collection[ProgressStorage],
    ) -> None:
        super().__init__()
        self.storages = storages

    def fetch(
            self,
            *,
            key: handlers.HandlerId,
            body: bodies.Body,
    ) -> Optional[ProgressRecord]:
        for storage in self.storages:
            content = storage.fetch(key=key, body=body)
            if content is not None:
                return content
        return None

    def store(
            self,
            *,
            key: handlers.HandlerId,
            record: ProgressRecord,
            body: bodies.Body,
            patch: patches.Patch,
    ) -> None:
        for storage in self.storages:
            storage.store(key=key, record=record, body=body, patch=patch)

    def purge(
            self,
            *,
            key: handlers.HandlerId,
            body: bodies.Body,
            patch: patches.Patch,
    ) -> None:
        for storage in self.storages:
            storage.purge(key=key, body=body, patch=patch)

    def clear(self, *, essence: bodies.BodyEssence) -> bodies.BodyEssence:
        for storage in self.storages:
            essence = storage.clear(essence=essence)
        return essence


class SmartProgressStorage(MultiProgressStorage):

    def __init__(
            self,
            *,
            name: str = 'kopf',
            field: dicts.FieldSpec = 'status.{name}.progress',
            prefix: str = 'kopf.zalando.org',
            verbose: bool = False,
    ) -> None:
        super().__init__([
            AnnotationsProgressStorage(prefix=prefix, verbose=verbose),
            StatusProgressStorage(name=name, field=field),
        ])
