import json

from flask_testing import TestCase

from config import create_app
from db import db
from models import UserModel
from services.stripe_service import StripeService
from tests.helpers import object_as_dict
from unittest.mock import patch


class TestAuth(TestCase):
    def create_app(self):
        self.headers = {"Content-Type": "application/json"}
        return create_app("config.TestApplicationConfiguration")

    def setUp(self):
        db.init_app(self.app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    @patch.object(StripeService, "create_customer", return_value="test_number_007")
    def test_register(self, stripe_mock):
        """
        Test when register a user, if it is written in the database
        Assure that the role is a User role
        """
        url = "/register"

        data = {
            "first_name": "Test",
            "last_name": "Test",
            "email": "test@test.com",
            "password": "123456",
            "phone": "1234567891011",
        }

        users = UserModel.query.all()
        assert len(users) == 0

        resp = self.client.post(url, data=json.dumps(data), headers=self.headers)

        assert resp.status_code == 201
        assert "token" in resp.json

        users = UserModel.query.all()
        assert len(users) == 1
        user = object_as_dict(users[0])
        user.pop("password")
        data.pop("password")

        assert user == {
            "id": user["id"],
            "role": user["role"],
            "created_on": user["created_on"],
            "updated_on": user["updated_on"],
            "payment_method": user["payment_method"],
            "payment_provider_id": "test_number_007",
            **data,
        }

    def test_user_already_exists_raises(self):
        url = "/register"
        data = {
            "first_name": "Test",
            "last_name": "Test",
            "email": "test@test.com",
            "password": "123456",
            "phone": "1234567891011",
        }

        resp = self.client.post(
            url, data=json.dumps(data), headers={"Content-Type": "application/json"}
        )

        assert resp.status_code == 201

        # Make the same request but user already exists

        resp = self.client.post(
            url, data=json.dumps(data), headers={"Content-Type": "application/json"}
        )
        assert resp.status_code == 400
        assert resp.json == {
            "message": "Username with this email already registered! Please login!"
        }

    def test_user_missing_data_raises(self):
        url = "/register"
        data = {
            "first_name": "Test",
            "last_name": "Test",
            "email": "test@test.com",
            "password": "123456",
            "phone": "1234567891011",
        }

        for k in data:
            current_data = data.copy()
            current_data.pop(k)
            resp = self.client.post(
                url,
                data=json.dumps(current_data),
                headers={"Content-Type": "application/json"},
            )

            assert resp.status_code == 400
            resp_actual = resp.json
            resp_actual = str(resp_actual).strip()
            assert (
                resp_actual
                == "{'message': {"
                + f"'{k}': "
                + "['Missing data for required field.']}}"
            )
