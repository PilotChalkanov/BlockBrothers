import stripe
from decouple import config


class StripeService:
    @staticmethod
    def create_customer(user):
        stripe.api_key = config("STRIPE_API_KEY")
        customer = stripe.Customer.create(
            email=user.email,
            name=f"{user.first_name} {user.last_name}",
            description="simple_user",
            phone=user.phone,
        )
        print(customer)
        return customer.id

    @staticmethod
    def create_card(customer_id, user_data):

        stripe.api_key = config("STRIPE_API_KEY")
        card_token = stripe.Token.create(
            card={
                "number": user_data["number"],
                "name": user_data["card_holder"],
                "exp_month": user_data["exp_month"],
                "exp_year": user_data["exp_year"],
                "cvc": user_data["cvc"],
            },
        )

        card = stripe.Customer.create_source(customer_id, source=card_token)

        return card

    @staticmethod
    def add_subscription(customer_id, period):
        stripe.api_key = config("STRIPE_API_KEY")
        products = {
            "monthly_subscription": "price_1K9PjgEhDaRjEbuca4bO4ZqT",
            "yearly_subscription": "price_1K9Tp2EhDaRjEbuc7suNTR6q",
        }
        subscription = stripe.Subscription.create(
            customer=customer_id,
            items=[
                {
                    "price": products["monthly_subscription"]
                    if period == "monthly"
                    else products["yearly_subscription"]
                }
            ],
        )
        return subscription
