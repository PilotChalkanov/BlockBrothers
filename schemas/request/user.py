from marshmallow import Schema, fields, validate, ValidationError
from sqlalchemy.sql.coercions import schema


class BaseUserSchema(Schema):
    email = fields.Email(requied=True)
    password = fields.String(min_length=6,max_length=100,required=True)
    first_name = fields.String(min_length=2,max_length=100,required=True)
    last_name = fields.String(min_length=2,max_length=100,required=True)
    phone = fields.String(min_length=13,max_length=13,required=True)

class UserLoginRequestSchema(Schema):
    email = fields.Email(requied=True)
    password = fields.String(min_length=6, max_length=100, required=True)

class HomeOwnerLoginRequestSchema(UserLoginRequestSchema):
    pass

class UserRegisterRequestSchema(BaseUserSchema):
    pass

class HomeOwnerRequestSchema(BaseUserSchema):
   bank_details = fields.String(required=True, validate=validate.Length(min=16, max=16))

class AdminRequestSchema(BaseUserSchema):
    pass
class AdminLoginRequestSchema(UserLoginRequestSchema):
    pass