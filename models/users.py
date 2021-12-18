from db import db
from sqlalchemy import func
from models.enum import RoleType


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


class HomeOwnerModel(BaseUserModel):
    __tablename__ = "home_owner"

    bank_details = db.Column(db.String(16), nullable=False)
    role = db.Column(db.Enum(RoleType), default=RoleType.home_owner, nullable=False)
    maint_events = db.relationship("MaintenanceEventModel", backref="maintenance_event", lazy="dynamic")

class HomeOwnerManagerModel(BaseUserModel):
    __tablename__ = "home_owner_manager"
    bank_details = db.Column(db.String(16), nullable=False)

    role = db.Column(
        db.Enum(RoleType), default=RoleType.home_owner_manager, nullable=False
    )


class AdministratorModel(BaseUserModel):
    __tablename__ = "admins"

    role = db.Column(db.Enum(RoleType), default=RoleType.admin, nullable=False)
