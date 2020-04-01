import inspect as p_inspect
import logging

logger = logging.getLogger('restless-client')


class ModelMeta:
    def __init__(self, client, class_name, pk_name, attributes, properties,
                 relations, methods, base_url, method_url, polymorphic,
                 relhelper):
        self.client = client
        self.connection = client.connection

        self.base_url = base_url
        self.method_url = method_url

        self.class_name = class_name
        self.pk_name = pk_name

        self.properties = properties
        self._attributes = attributes
        self._relations = relations
        self._methods = methods

        self.deserializer = client.deserializer
        self.serializer = client.serializer
        self.polymorphic = polymorphic
        self.relhelper = relhelper

    def attributes(self):
        return list(self._attributes.keys())

    def relations(self):
        return list(self._relations.keys())

    def methods(self):
        return list(self._methods)


class InstanceState:
    def __init__(self, instance):
        self.instance = instance
        self.meta = instance._rlc
        self.dirty = set()
        self.values = {}

    def __getattribute__(self, attrib):
        meta = super().__getattribute__('meta')
        if hasattr(meta, attrib):
            return getattr(meta, attrib)
        return super().__getattribute__(attrib)

    @property
    def pk_val(self):
        return getattr(self.instance, self.meta.pk_name)

    @property
    def is_new(self):
        return str(self.pk_val).startswith('C')

    def delete(self):
        self.connection.delete(self.instance)

    def save(self):
        if self.is_new:
            self.connection.create(self.instance)
        elif self.dirty:
            self.connection.update(self.instance)
        else:
            logger.debug("No action needed")
        self.dirty = set()


def inspect(obj):
    meta = obj._rlc
    if isinstance(meta, InstanceState):
        return meta
    if p_inspect.isclass(obj):
        return meta
    return InstanceState(obj)
