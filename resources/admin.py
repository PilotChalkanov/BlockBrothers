from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.home_owner_manager import HomeOwnerManager
from managers.admin_manager import AdminManager
from models import RoleType
from schemas.request.user import (
    HomeOwnerRequestSchema,
    AdminLoginRequestSchema,
    AdminRequestSchema,
    HomeOwnerManagerLoginRequestSchema,
    HomeOwnerManagerRequestSchema,
)
from utils.decorators import permission_required, validate_schema


class CreateAdmin(Resource):
    @auth.login_required
    @permission_required(RoleType.admin)
    @validate_schema(AdminRequestSchema)
    def post(self):
        admin = AdminManager.create_admin(request.get_json())
        return 201


class LoginAdmin(Resource):
    @validate_schema(AdminLoginRequestSchema)
    def post(self):
        admin_token = AdminManager.login(request.get_json())
        return {"token": admin_token}, 200


class LoginHomeOwnerManager(Resource):
    @validate_schema(HomeOwnerManagerLoginRequestSchema)
    def post(self):
        token = HomeOwnerManager.login_home_owner_manager(request.get_json())
        return {"token": token, "role": "homeowner_manager"}, 200


class CreateHomeOwner(Resource):
    @auth.login_required
    @permission_required(RoleType.admin)
    @validate_schema(HomeOwnerRequestSchema)
    def post(self):
        home_owner = HomeOwnerManager.create_home_owner(request.get_json())
        return 201


class CreateHomeOwnerManager(Resource):
    @auth.login_required
    @permission_required(RoleType.admin)
    @validate_schema(HomeOwnerManagerRequestSchema)
    def post(self):
        home_owner_manager = HomeOwnerManager.create_home_owner_manager(
            request.get_json()
        )
        return 201
