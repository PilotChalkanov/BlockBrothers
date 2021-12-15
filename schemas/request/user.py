from marshmallow import Schema, fields, validate, ValidationError

class BaseUserSchema(Schema):
    email = fields.Email(requied=True)
    password = fields.String(required=True, validate=validate.Length(min=6, max=255))

class UserLoginRequestSchema(BaseUserSchema):
    pass

class UserRegisterRequestSchema(BaseUserSchema,Schema):
    first_name = fields.String(required=True, validate=validate.Length(min=2, max=255))
    last_name = fields.String(required=True, validate=validate.Length(min=2, max=255))
    phone = fields.String(required=True, validate=validate.Length(min=13, max=13))

class HomeOwnerRequestSchema(UserRegisterRequestSchema,Schema):
    bank_details = fields.String(required=True, validate=validate.Length(min=16, max=16))