import stripe
from decouple import config
from stripe.error import AuthenticationError, APIConnectionError, CardError
from werkzeug.exceptions import BadRequest


class StripeService:
    """
    Singleton class for the payment service
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def create_customer(self, user):
        try:
            stripe.api_key = config("STRIPE_API_KEY")
            customer = stripe.Customer.create(
                email=user.email,
                name=f"{user.first_name} {user.last_name}",
                description="simple_user",
                phone=user.phone,
            )

            return customer.id
        except AuthenticationError as e:
            raise BadRequest(str(e))
        except APIConnectionError as e:
            raise BadRequest(str(e))

    def create_card(self, customer_id, user_data):
        try:
            stripe.api_key = config("STRIPE_API_KEY")
            card_token = stripe.Token.create(
                card={
                    "number": user_data["number"].strip(),
                    "name": user_data["card_holder"],
                    "exp_month": user_data["exp_month"],
                    "exp_year": user_data["exp_year"],
                    "cvc": user_data["cvc"],
                },
            )

            card = stripe.Customer.create_source(customer_id, source=card_token)
            return card

        except AuthenticationError as e:
            raise BadRequest(str(e))
        except APIConnectionError as e:
            raise BadRequest(str(e))
        except CardError as e:
            raise BadRequest(str(e))

    def add_subscription(customer_id, period):
        try:
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

        except AuthenticationError as e:
            raise BadRequest(str(e))
        except APIConnectionError as e:
            raise BadRequest(str(e))
