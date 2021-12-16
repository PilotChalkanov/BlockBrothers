from flask import request
from flask_restful import Resource

from managers.auth import AuthManager
from managers.user_manager import UserManager, HomeOwnerManager
from schemas.request.user import UserRegisterRequestSchema, UserLoginRequestSchema, HomeOwnerLoginRequestSchema
from utils.decorators import validate_schema


class Register(Resource):
    @validate_schema(UserRegisterRequestSchema)
    def post(self):
        user = UserManager.register(request.get_json())
        token = AuthManager.encode_token(user)
        return {"token": token}, 201


class Login(Resource):
    @validate_schema(UserLoginRequestSchema)
    def post(self):
        user = UserManager.login(request.get_json())
        token = AuthManager.encode_token(user)
        return {"token": token}, 200

class LoginHomeOwner(Resource):
    @validate_schema(HomeOwnerLoginRequestSchema)
    def post(self):
        token = HomeOwnerManager.login(request.get_json())
        return {"token": token, "role": "homeowner"}, 200