from decouple import config
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from db import db
from resources.route import routes
hhh

class DevApplication:

    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}"
        f"@localhost:{config('DB_PORT')}/{config('DB_NAME')}"
    )

class TestApplication:
    pass

    # DEBUG = True
    # TESTING = True
    # SQLALCHEMY_DATABASE_URI = (
    #     f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}"
    #     f"@localhost:{config('DB_PORT')}/{config('TEST_DB_NAME')}"
    # )

def create_app(config = "config.DevApplication"):
    app = Flask(__name__)
    app.config.from_object(DevApplication)
    migrate = Migrate(app, db)
    api = Api(app)
    [api.add_resource(*r) for r in routes]
    return app