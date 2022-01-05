import json

from flask_testing import TestCase

from config import create_app
from db import db
from models import HomeOwnerModel
from tests.helpers import object_as_dict


class TestApp(TestCase):
    def create_app(self):
        self.headers = {"Content-Type": "application/json"}
        return create_app("config.TestApplicationConfiguration")

    def setUp(self):
        db.init_app(self.app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_home_owner(self):
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

        users = HomeOwnerModel.query.all()
        assert len(users) == 0

        resp = self.client.post(url, data=json.dumps(data), headers=self.headers)

        assert resp.status_code == 201
        assert "token" in resp.json

        users = HomeOwnerModel.query.all()
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
            "payment_provider_id": user["payment_provider_id"],
            **data,
        }
