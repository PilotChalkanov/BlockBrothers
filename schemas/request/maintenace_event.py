from marshmallow import Schema, fields, validate


class MaintenanceEventRequestSchema(Schema):
    title = fields.String(required=True, validate=validate.Length(max=100))
    content = fields.String(required=True, validate=validate.Length(max=255))
    photo_url = fields.String(required=False, validate=validate.Length(max=255))
    created_on = fields.DateTime(required=True)

