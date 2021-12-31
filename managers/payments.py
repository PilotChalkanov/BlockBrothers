from datetime import datetime

from db import db
from models import SubscriptionModel
from services.stripe_service import StripeService

stripe_service = StripeService()


class PaymentManager:
    @staticmethod
    def create_card(user, card_data):
        customer_id = user.payment_provider_id
        card = stripe_service.create_card(customer_id, card_data)
        return card

    @staticmethod
    def subscribe(user, period):
        customer_id = user.payment_provider_id
        subscription = stripe_service.add_subscription(customer_id, period)

        subs = {
            "provider_subs_id": subscription.id,
            f"{user.role.value}_id": user.id,
            "type": period,
        }
        subs = SubscriptionModel(**subs)
        db.session.add(subs)
        db.session.flush()
        return subscription
