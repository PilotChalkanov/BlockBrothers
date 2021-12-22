from services.stripe_service import StripeService


class PaymentManager:

    @staticmethod
    def create_card(user, card_data):
        customer_id = user.payment_provider_id
        card = StripeService.create_card(customer_id, card_data)
        return card

    @staticmethod
    def subscribe(user, period):
        customer_id = user.payment_provider_id
        subscription = StripeService.add_subscription(customer_id,period)
        return subscription

