import enum


class RoleType(enum.Enum):
    user = "user"
    home_owner = "home_owner"
    home_owner_manager = "home_owner_manager"
    admin = "admin"


class State(enum.Enum):
    pending = "Pending"
    closed = "Closed"
    raised = "Raised"


class PaymentMethodType(enum.Enum):
    card = ("card",)
    alipay = ("alipay",)
    sepa_debit = "sepa_debit"
