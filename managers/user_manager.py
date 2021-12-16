import algorithm as algorithm
from psycopg2.errorcodes import UNIQUE_VIOLATION
from werkzeug.exceptions import BadRequest, InternalServerError
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from managers.auth import AuthManager
from models.users import UserModel, HomeOwnerModel, HomeOwnerManagerModel, AdministratorModel


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
            db.session.commit()
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

class UserManager:
    @staticmethod
    def register(user_data):

        """
        Hash the plain password
        :param data: user_data: dict
        :return: user_data

        """

        user_data["password"] = generate_password_hash(user_data["password"])
        user = UserModel(**user_data)
        db.session.add(user)
        try:
            db.session.commit()
        except Exception as ex:
            if ex.orig.pgcode == UNIQUE_VIOLATION:
                raise BadRequest(
                    "Username with this email already registered! Please login!"
                )
            else:
                raise InternalServerError("Server is not available")
        return user

    @staticmethod
    def login(user_data):
        user = UserModel.query.filter_by(email=user_data["email"]).first()
        if not user:
            raise BadRequest("Invalid user name or password!")
        if not check_password_hash(user.password, user_data["password"]):
            raise BadRequest("Invalid user name or password!")
        return user

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

