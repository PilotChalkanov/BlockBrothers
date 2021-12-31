import json

from flask_testing import TestCase

from config import create_app
from db import db


class TestApp(TestCase):
    def create_app(self):
        return create_app("config.TestApplication")

    def setUp(self):
        db.init_app(self.app)
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_protected_endpoints_without_token_or_with_invalid_token(self):
        for method, url in  [
            ("POST", "/аdmin/create_admin"),
            ("POST", "/admin/create_home_owner"),
            ("POST", "/admin/create_home_owner_manager"),
            ("POST", "/home_owners/maint_event"),
            ("POST", "/login/add_card"),
            ("DELETE", "/home_owners/maint_event/1"),
            ("PUT", "/home_owners/maint_event/1"),

        ]:
            if method == "POST":
                resp = self.client.post(url, data=json.dumps({}))
            elif method == "GET":
                resp = self.client.get(url)
            elif method == "PUT":
                resp = self.client.put(url, data=json.dumps({}))
            else:
                resp = self.client.delete(url)
            self.assert400(resp, {'message': 'Invalid token'})



