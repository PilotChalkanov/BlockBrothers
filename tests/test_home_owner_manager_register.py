import json

from flask_testing import TestCase

from config import create_app
from db import db
from models import UserModel, HomeOwnerModel, HomeOwnerManagerModel
from services.stripe_service import StripeService
from tests.factory_users import AdminFactory
from tests.helpers import object_as_dict, generate_token
from unittest.mock import patch


class TestHomeOwnerManagerRegister(TestCase):
    def create_app(self):
        self.headers = {"Content-Type": "application/json"}
        return create_app("config.TestApplicationConfiguration")

    def setUp(self):
        db.init_app(self.app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


    def test_register_home_owner(self):
        """
        Test when register a user, if it is written in the database
        Assure that the role is a User role
        """
        url = "/admin/create_home_owner_manager"

        data = {
            "first_name": "Test",
            "last_name": "Test",
            "email": "test@test.com",
            "password": "123456",
            "phone": "1234567891011",
        }

        home_owner_managers = HomeOwnerManagerModel.query.all()
        assert len(home_owner_managers) == 0
        admin = AdminFactory()
        token = generate_token(admin)

        self.headers.update({"Authorization": f"Bearer {token}"})
        resp = self.client.post(url, data=json.dumps(data), headers=self.headers)

        assert resp.status_code == 200


        home_owner_managers = HomeOwnerManagerModel.query.all()
        assert len(home_owner_managers) == 1
        home_owner_manager = object_as_dict(home_owner_managers[0])
        home_owner_manager.pop("password")
        data.pop("password")
        home_owner_manager.pop("stripe_id")

        assert home_owner_manager == {
            "id": home_owner_manager["id"],
            "role": home_owner_manager["role"],
            "created_on": home_owner_manager["created_on"],
            "updated_on": home_owner_manager["updated_on"],
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

    def test_home_owner_manager_missing_data_raises(self):

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
