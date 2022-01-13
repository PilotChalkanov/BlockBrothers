import json

from flask_testing import TestCase

from config import create_app
from db import db
from models import MaintenanceEventModel, State
from tests.factory_users import HomeOwnerFactory
from tests.helpers import generate_token


class TestMaintEvent(TestCase):
    url = "/home_owners/maint_event"

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

        resp = self.client.post(self.url, data=json.dumps(data), headers=self.headers)

        maint_event = MaintenanceEventModel.query.all()
        assert len(maint_event) == 1
        expected_resp = {
            "id": maint_event[0].id,
            "status": State.pending.value,
            **data,
        }
        actual_resp = resp.json
        actual_resp.pop("created_on")
        actual_resp.pop("updated_on")
        assert resp.status_code == 201
        assert actual_resp == expected_resp

    def test_complaint_missing_input_fields_raises(self):
        home_owner = HomeOwnerFactory()
        token = generate_token(home_owner)

        maint_event = MaintenanceEventModel.query.all()
        assert len(maint_event) == 0
        data = {
            "title": "Test",
            "content": "Test test",
            "photo_url": "https://example.com",
        }

        for k in data:
            current_data = data.copy()
            current_data.pop(k)
            resp = self.client.post(
                self.url,
                data=json.dumps(current_data),
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {token}",
                },
            )

            self.assert400(resp)

            resp_actual = resp.json
            resp_actual = str(resp_actual).strip()
            assert (
                resp_actual
                == "{'message': {"
                + f"'{k}': "
                + "['Missing data for required field.']}}"
            )
