
from flask import request
from flask_restful import Resource
from managers.auth import auth
from managers.payments import PaymentManager
from schemas.request.payment import CreateCardRequestSchema, CreateSubscriptionRequestSchema
from utils.decorators import validate_schema


class AddCard(Resource):
    @auth.login_required
    @validate_schema(CreateCardRequestSchema)
    def post(self):
        current_user = auth.current_user()
        card_data = request.get_json()
        card = PaymentManager.create_card(current_user, card_data)

        return f"Successfully added card number **** **** **** {card.last4}"

class CreateSubscription(Resource):
    @auth.login_required
    @validate_schema(CreateSubscriptionRequestSchema)
    def post(self):
        current_user = auth.current_user()
        subscription_data = request.get_json()
        period = subscription_data["type"]
        subscription = PaymentManager.subscribe(current_user, period)
        return {"subscription_id" : subscription.id}

