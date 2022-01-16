from db import db
from sqlalchemy import func
from models.enumerables import RoleType, PaymentMethodType


class BaseUserModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(13), nullable=False)
    created_on = db.Column(db.DateTime, server_default=func.now())
    updated_on = db.Column(db.DateTime, onupdate=func.now())


class UserModel(BaseUserModel):
    __tablename__ = "users"

    role = db.Column(db.Enum(RoleType), default=RoleType.user, nullable=False)
    payment_method = db.Column(
        db.Enum(PaymentMethodType), default=PaymentMethodType.card, nullable=False
    )
    payment_provider_id = db.Column(db.String(255), nullable=False)


class HomeOwnerModel(BaseUserModel):
    __tablename__ = "home_owner"

    role = db.Column(db.Enum(RoleType), default=RoleType.home_owner, nullable=False)
    maint_events = db.relationship(
        "MaintenanceEventModel", backref="maintenance_event", lazy="dynamic"
    )
    payment_provider_id = db.Column(db.String(255), nullable=False)


class HomeOwnerManagerModel(BaseUserModel):
    __tablename__ = "home_owner_manager"

    role = db.Column(
        db.Enum(RoleType), default=RoleType.home_owner_manager, nullable=False
    )
    stripe_id = db.Column(
        db.Enum(PaymentMethodType), default=PaymentMethodType.card, nullable=False
    )


class AdministratorModel(BaseUserModel):
    __tablename__ = "admins"

    role = db.Column(db.Enum(RoleType), default=RoleType.admin, nullable=False)
