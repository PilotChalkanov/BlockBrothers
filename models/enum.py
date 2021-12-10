import enum


class RoleType(enum.Enum):
    user = "user"
    home_owner = "home_owner"
    home_owner_manager = "home_owner_manager"
    admin = "admin"
