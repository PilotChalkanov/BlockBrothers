from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from managers.auth import AuthManager
from models import AdministratorModel


class AdminManager:
    @staticmethod
    def create_admin(data):
        """
        Hash the plain password
        :param data: admin_data: dict
        :return: user_data

        """

        data["password"] = generate_password_hash(data["password"], method="sha256")
        admin = AdministratorModel(**data)
        try:
            db.session.add(admin)
            db.session.flush()
        except Exception as ex:
            raise BadRequest(str(ex))

    @staticmethod
    def login(data):
        """
        Checks the email and password (hashes the plain password)
        :param data: dict -> email, password
        :return: token
        """
        try:
            admin = AdministratorModel.query.filter_by(email=data["email"]).first()
            if admin and check_password_hash(admin.password, data["password"]):
                return AuthManager.encode_token(admin)
            raise Exception
        except Exception:
            raise BadRequest("Invalid user name or password!")
