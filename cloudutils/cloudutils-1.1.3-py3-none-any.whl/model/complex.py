# Copyright © 2020 Noel Kaczmarek
from spyne import String, Integer
from spyne.model.complex import ComplexModel


class UUID(String):
    __namespace__ = 'cloud'
    __type_name__ = 'UUID'

    class Attributes(String.Attributes):
        max_length = 32


class Username(String):
    __namespace__ = 'cloud'
    __type_name__ = 'Username'

    class Attributes(String.Attributes):
        max_length = 20


class ServiceType(ComplexModel):
    __namespace__ = 'cloud'

    id = Integer
    name = String
    port = Integer


class Service(ComplexModel):
    __namespace__ = 'cloud'

    id = UUID
    host = String
    type = ServiceType


MandatoryServiceType = ServiceType.customize(nullable=False, min_occurs=1)
MandatoryService = Service.customize(nullable=False, min_occurs=1)


class Session(ComplexModel):
    __namespace__ = 'cloud'

    id = UUID
    user = UUID
    username = Username
    key = String


MandatorySession = Session.customize(nullable=False, min_occurs=1)