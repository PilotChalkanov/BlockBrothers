from marshmallow import Schema, fields


class BaseUserSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(min_length=6, max_length=100, required=True)
    first_name = fields.String(min_length=2, max_length=100, required=True)
    last_name = fields.String(min_length=2, max_length=100, required=True)
    phone = fields.String(min_length=13, max_length=13, required=True)


class UserLoginRequestSchema(Schema):
    email = fields.Email(requied=True)
    password = fields.String(min_length=6, max_length=100, required=True)


class HomeOwnerLoginRequestSchema(UserLoginRequestSchema):
    pass


class UserRegisterRequestSchema(BaseUserSchema):
    pass


class HomeOwnerRequestSchema(UserRegisterRequestSchema):
    pass


class HomeOwnerManagerRequestSchema(HomeOwnerRequestSchema):
    pass


class HomeOwnerManagerLoginRequestSchema(UserLoginRequestSchema):
    pass


class AdminRequestSchema(BaseUserSchema):
    pass


class AdminLoginRequestSchema(UserLoginRequestSchema):
    pass
