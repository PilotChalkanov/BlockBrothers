import json
from unittest.mock import patch

from flask_testing import TestCase

from config import create_app
from db import db
from models import UserModel
from services.stripe_service import StripeService
from tests.factory_users import UserFactory
from tests.helpers import generate_token


class Test_Add_Card(TestCase):
    url = "/login/add_card"

    def create_app(self):
        return create_app("config.TestApplicationConfiguration")

    def setUp(self):
        db.init_app(self.app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    @patch.object(StripeService, "create_card", return_value="card_test_num")
    def test_add_card_to_user(self, mock_card):
        user = UserFactory()
        token = generate_token(user)

        users = UserModel.query.all()
        assert len(users) == 1

        data = {
            "number": "4242 4242 4242 4242",
            "card_holder": "Test Test",
            "exp_month": 4,
            "exp_year": 2022,
            "cvc": "314",
        }

        resp = self.client.post(
            self.url,
            data=json.dumps(data),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            },
        )

        assert resp.status_code == 200
