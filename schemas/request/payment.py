from datetime import datetime

from marshmallow import Schema, fields, validate, ValidationError


def is_card_number_length_valid(value):
    if len(value.replace(" ", "")) != 16:
        raise ValidationError("Not a valid card number.")

class CreateCardRequestSchema(Schema):

    number = fields.String(required=True, validate=is_card_number_length_valid)
    card_holder = fields.String(required=True, validate=validate.Length(min=10, max=20))
    exp_month = fields.Integer(required=True, validate=validate.Range(min=1, max=12))
    exp_year = fields.Integer(
        required=True,
        validate=validate.Range(min=datetime.now().year, max=datetime.now().year + 10),
    )
    cvc = fields.String(required=True, validate=validate.Length(min=3, max=3))


class CreateSubscriptionRequestSchema(Schema):

    type = fields.String(
        required=True, validate=validate.OneOf(choices="monthly, yearly")
    )
