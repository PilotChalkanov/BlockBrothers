from psycopg2.errorcodes import UNIQUE_VIOLATION
from werkzeug.exceptions import BadRequest, InternalServerError
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from models.users import (
    UserModel,
)
from services.stripe_service import StripeService

stripe_service = StripeService()


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

        # creating a stripe account

        stripe_customer_id = stripe_service.create_customer(user)
        user.payment_provider_id = stripe_customer_id
        try:
            db.session.add(user)
            db.session.flush()
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
