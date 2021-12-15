from db import db

from models.enum import RoleType


class BaseUserModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(13), nullable=False)

class UserModel(BaseUserModel):
    __tablename__ = "users"

    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum(RoleType), default=RoleType.user, nullable=False)


class HomeOwnerModel(BaseUserModel):
    __tablename__ = "home_owner"

    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum(RoleType), default=RoleType.home_owner, nullable=False)
    bank_details = db.Column(db.String(22))


class HomeOwnerManagerModel(BaseUserModel):
    __tablename__ = "home_owner_manager"

    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    role = db.Column(
        db.Enum(RoleType), default=RoleType.home_owner_manager, nullable=False
    )


class AdministratorModel(BaseUserModel):
    __tablename__ = "admins"

    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum(RoleType), default=RoleType.admin, nullable=False)
