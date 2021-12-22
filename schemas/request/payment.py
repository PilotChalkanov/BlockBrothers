from datetime import datetime

from marshmallow import Schema, fields, validate


class CreateCardRequestSchema(Schema):

    number = fields.String(required=True, validate=validate.Length(min=16,max=16))
    card_holder = fields.String(required=True, validate=validate.Length(min=10,max=20))
    exp_month = fields.Integer(required=True, validate=validate.Range(min=1,max=12))
    exp_year = fields.Integer(required=True, validate=validate.Range(min=datetime.now().year,max=datetime.now().year+10))
    cvc = fields.String(required=True, validate=validate.Length(min=3, max=3))

class CreateSubscriptionRequestSchema(Schema):
    type = fields.String(required=True, validate=validate.OneOf(choices="monthly, yearly"))

    
