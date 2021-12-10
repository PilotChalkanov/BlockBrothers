from flask import request
from werkzeug.exceptions import BadRequest


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
