from flask_restful import Resource
from flask import request

from managers.auth import auth
from managers.home_owner_managers import  HomeOwnerManager
from models import RoleType
from schemas.request.user import HomeOwnerRequestSchema
from utils.decorators import permission_required, validate_schema


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

