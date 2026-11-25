

from datetime import datetime, timedelta
import hashlib
import secrets


from core.database_connection import settings

import jwt

def create_access_token(user_id:int)->str:
    now = datetime.now()

    payload = {
        "sub": str(user_id),
        "iat": now,
        "exp": now + timedelta(minutes=15),
        "type": "access"
    }

    return jwt.encode(
        payload, 
        settings.jwt_secret_key, 
        algorithm="HS256"
    )


def create_refresh_token()->str:
    return secrets.token_urlsafe(32)


def hash_refresh_token(token:str)->str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()