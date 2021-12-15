from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from managers.auth import AuthManager
from models import HomeOwnerModel, HomeOwnerManagerModel


class HomeOwnerManager:
    @staticmethod
    def create_home_owner(data):
        """
        Hash the plain password
        :param data: user_data: dict
        :return: user_data

        """

        data["password"] = generate_password_hash(data["password"], method="sha256")
        home_owner = HomeOwnerModel(**data)
        try:
            db.session.add(home_owner)
            db.session.flush()
        except Exception as ex:
            raise BadRequest(str(ex))

    @staticmethod
    def create_home_owner_manager(data):
        """
        Hash the plain password
        :param data: user_data: dict
        :return: user_data

        """

        data["password"] = generate_password_hash(data["password"], method="sha256")
        home_owner_manager = HomeOwnerManagerModel(**data)
        try:
            db.session.add(home_owner_manager)
            db.session.flush()
        except Exception as ex:
            raise BadRequest(str(ex))


class HomeOwnerLoginManager:
    @staticmethod
    def login(data):
        """
        Checks the email and password (hashes the plain password)
        :param data: dict -> email, password
        :return: token
        """

        try:
            home_owner = HomeOwnerModel.query.filter_by(email=data["email"]).first()
            if home_owner and check_password_hash(home_owner.password, data["password"]):
                return AuthManager.encode_token(home_owner)
            raise Exception
        except Exception:
            raise BadRequest("Invalid username or password")