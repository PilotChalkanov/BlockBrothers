from marshmallow import Schema, fields, validate
from marshmallow_enum import EnumField

from models.enum import State


class MaintenanceEventCreateResponseSchema(Schema):
    id = fields.Integer(requied=True)
    title = fields.String(required=True, validate=validate.Length(max=100))
    content = fields.String(required=True, validate=validate.Length(max=255))
    photo_url = fields.String(required=False, validate=validate.Length(max=255))
    created_on = fields.DateTime(required=True)
    updated_on = fields.DateTime(required=True)
    status = EnumField(State, by_value=True)
