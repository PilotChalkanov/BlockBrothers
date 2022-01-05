import json

from flask_testing import TestCase

from config import create_app
from db import db
from models import MaintenanceEventModel, State

from tests.factory_home_owner import HomeOwnerFactory
from tests.helpers import generate_token
from unittest.mock import patch


class TestMaintEvent(TestCase):
    def create_app(self):
        self.headers = {"Content-Type": "application/json"}
        return create_app("config.TestApplicationConfiguration")

    def setUp(self):
        db.init_app(self.app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_maint_event(self):
        url = "/home_owners/maint_event"
        data = {
            "title": "Broken fan",
            "content": "third Floor fan - broken",
            "photo_url": "https://www.something.sn",
        }

        home_owner = HomeOwnerFactory()
        token = generate_token(home_owner)
        self.headers.update({"Authorization": f"Bearer {token}"})
        maint_event = MaintenanceEventModel.query.all()
        assert len(maint_event) == 0

        resp = self.client.post(url, data=json.dumps(data), headers=self.headers)

        maint_event = MaintenanceEventModel.query.all()
        assert len(maint_event) == 1
        expected_resp = {
            "id": maint_event[0].id,
            "status": State.pending.value,
            # "home_owner_id": maint_event[0].home_owner_id,
            **data,
        }
        actual_resp = resp.json
        actual_resp.pop("created_on")
        actual_resp.pop("updated_on")
        assert resp.status_code == 201
        assert actual_resp == expected_resp
