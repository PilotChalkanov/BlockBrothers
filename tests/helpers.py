from sqlalchemy import inspect

from managers.auth import AuthManager


def object_as_dict(obj):
    return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}


def mock_uuid():
    return "1111"


def generate_token(user):
    return AuthManager.encode_token(user)
