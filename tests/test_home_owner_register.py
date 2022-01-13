import json

from flask_testing import TestCase

from config import create_app
from db import db
from models import UserModel, HomeOwnerModel
from services.stripe_service import StripeService
from tests.factory_users import AdminFactory
from tests.helpers import object_as_dict, generate_token
from unittest.mock import patch


class TestHomeOwnerRegister(TestCase):
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
    def test_register_home_owner(self, stripe_mock):
        """
        Test when register a user, if it is written in the database
        Assure that the role is a User role
        """
        url = "/admin/create_home_owner"

        data = {
            "first_name": "Test",
            "last_name": "Test",
            "email": "test@test.com",
            "password": "123456",
            "phone": "1234567891011",
        }

        home_owners = HomeOwnerModel.query.all()
        assert len(home_owners) == 0
        admin = AdminFactory()
        token = generate_token(admin)

        self.headers.update({"Authorization": f"Bearer {token}"})
        resp = self.client.post(url, data=json.dumps(data), headers=self.headers)

        assert resp.status_code == 200
        assert "token" in resp.json

        home_owners = HomeOwnerModel.query.all()
        assert len(home_owners) == 1
        home_owner = object_as_dict(home_owners[0])
        home_owner.pop("password")
        data.pop("password")

        assert home_owner == {
            "id": home_owner["id"],
            "role": home_owner["role"],
            "created_on": home_owner["created_on"],
            "updated_on": home_owner["updated_on"],
            "payment_provider_id": "test_number_007",
            **data,
        }

    def test_user_already_exists_raises(self):

        url = "/admin/create_home_owner"
        data = {
            "first_name": "Test",
            "last_name": "Test",
            "email": "test@test.com",
            "password": "123456",
            "phone": "1234567891011",
        }
        admin = AdminFactory()
        token = generate_token(admin)
        self.headers.update({"Authorization": f"Bearer {token}"})

        resp = self.client.post(url, data=json.dumps(data), headers=self.headers)

        assert resp.status_code == 200

        # Make the same request but user already exists

        resp = self.client.post(url, data=json.dumps(data), headers=self.headers)
        assert resp.status_code == 400
        assert resp.json == {
            "message": "Username with this email already registered! Please login!"
        }

    def test_user_missing_data_raises(self):
        url = "/admin/create_home_owner"
        data = {
            "first_name": "Test",
            "last_name": "Test",
            "email": "test@test.com",
            "password": "123456",
            "phone": "1234567891011",
        }

        admin = AdminFactory()
        token = generate_token(admin)
        self.headers.update({"Authorization": f"Bearer {token}"})

        for k in data:
            current_data = data.copy()
            current_data.pop(k)

            resp = self.client.post(
                url,
                data=json.dumps(current_data),
                headers=self.headers,
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
