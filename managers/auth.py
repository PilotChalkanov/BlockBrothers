from datetime import datetime, timedelta

import jwt
from decouple import config


class JWT_key_time:
    pass


class AuthManager:
    @staticmethod
    def encode_token(user):
        payload = {"sub": user.id, "exp": datetime.utcnow() + timedelta(days=int(config("JWT_KEY_EXP")))}
        return jwt.encode(payload, key=config("JWT_KEY"), algorithm="HS256")
