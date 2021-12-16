from flask_restful import Resource
from flask import request
from werkzeug.security import check_password_hash

from managers.auth import auth, AuthManager
from managers.user_manager import HomeOwnerManager, AdminManager
from models import RoleType
from schemas.request.user import HomeOwnerRequestSchema, AdminLoginRequestSchema, AdminRequestSchema
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
    @validate_schema(HomeOwnerRequestSchema)
    def post(self):
        home_owner = HomeOwnerManager.create_home_owner_manager(request.get_json())
        return 201

