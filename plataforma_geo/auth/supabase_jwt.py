import os
from jose import jwt, JWTError

SUPABASE_JWT_SECRET = os.getenv("SUPABASE_JWT_SECRET")
SUPABASE_JWT_ALG = "HS256"

def verify_supabase_jwt(token: str):
    try:
        payload = jwt.decode(
            token,
            SUPABASE_JWT_SECRET,
            algorithms=[SUPABASE_JWT_ALG],
            audience="authenticated",
            options={"verify_exp": True},
        )
        return payload
    except JWTError:
        return None
