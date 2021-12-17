from flask import request
from werkzeug.exceptions import BadRequest, Forbidden
from marshmallow import Schema, validate
from managers.auth import auth


def validate_schema(schema_name):
    def wrapper_func(func):
        def decorated_func(*args, **kwargs):
            data = request.get_json()
            schema = schema_name()
            errors = schema.validate(data)
            if errors:
                raise BadRequest(errors)
            return func(*args, **kwargs)

        return decorated_func

    return wrapper_func


def permission_required(permission):
    def wrapper(func):
        def decorated_func(*args, **kwargs):
            user = auth.current_user()
            role = user.role
            if not role == permission:
                raise Forbidden("You do not have access to this resource")
            return func(*args, **kwargs)

        return decorated_func

    return wrapper
