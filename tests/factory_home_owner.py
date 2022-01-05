from db import db
from random import randint

import factory

from models import MaintenanceEventModel, RoleType, PaymentMethodType, HomeOwnerModel
from resources.maintenance_event import MaintenanceEvent


class BaseFactory(factory.Factory):
    @classmethod
    def create(cls, **kwargs):
        object = super().create(**kwargs)
        db.session.add(object)
        db.session.flush()
        return object


class HomeOwnerFactory(BaseFactory):
    class Meta:
        model = HomeOwnerModel

    id = factory.Sequence(lambda n: n)
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    phone = str(randint(100000, 200000))
    password = factory.Faker("password")
    role = RoleType.home_owner
    payment_provider_id = str(randint(100000, 200000))
