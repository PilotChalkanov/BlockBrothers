from datetime import datetime, timedelta

import jwt
from decouple import config
from flask_httpauth import HTTPTokenAuth
from werkzeug.exceptions import BadRequest

from models.users import (
    HomeOwnerModel,
    UserModel,
    HomeOwnerManagerModel,
    AdministratorModel,
)

mapper = {
    "UserModel": lambda x: UserModel.query.filter_by(id=x).first(),
    "HomeOwnerModel": lambda x: HomeOwnerModel.query.filter_by(id=x).first(),
    "HomeOwnerManagerModel": lambda x: HomeOwnerManagerModel.query.filter_by(
        id=x
    ).first(),
    "AdministratorModel": lambda x: AdministratorModel().query.filter_by(id=x).first(),
}


class JWT_key_time:
    pass


class AuthManager:
    @staticmethod
    def encode_token(user):
        """
        Create JWT Token
        :param data: user_data: dict
        :return: token
        """

        payload = {
            "sub": user.id,
            "exp": datetime.utcnow() + timedelta(days=int(config("JWT_KEY_EXP"))),
            "role": user.__class__.__name__,
        }
        return jwt.encode(payload, key=config("JWT_KEY"), algorithm="HS256")

    @staticmethod
    def decode_token(token):
        try:
            data = jwt.decode(token, key=config("JWT_KEY"), algorithms=["HS256"])
            return data["sub"], data["role"]
        except jwt.ExpiredSignatureError:
            raise BadRequest("Token has expired")
        except jwt.InvalidSignatureError:
            raise BadRequest("Invalid token")
        except jwt.DecodeError:
            raise BadRequest("Invalid token")


auth = HTTPTokenAuth(scheme="Bearer")


@auth.verify_token
def verify_token(token):
    user_id, role = AuthManager.decode_token(token)
    user = mapper[role](user_id)
    return user
