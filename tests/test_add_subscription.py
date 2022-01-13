import json
from unittest.mock import patch

from flask_testing import TestCase

from config import create_app
from db import db
from models import UserModel
from services.stripe_service import StripeService
from tests.factory_users import UserFactory
from tests.helpers import generate_token


class Test_Add_Subscription(TestCase):
    url = "/login/subscribe"

    def create_app(self):
        return create_app("config.TestApplicationConfiguration")

    def setUp(self):
        db.init_app(self.app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    @patch.object(StripeService, "add_subscription", return_value={"id":"1111"})
    def test_add_card_to_user(self, mock_subscription):
        user = UserFactory()
        token = generate_token(user)

        users = UserModel.query.all()
        assert len(users) == 1

        data = {
            "type": "monthly",
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
        mock_subscription.assert_called_once_with(
            user.payment_provider_id,
            data["type"],
        )
