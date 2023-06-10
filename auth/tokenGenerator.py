from typing import Dict
import jwt
from os import environ
import jwt

JWT_SECRET = environ.get("JWT_SECRET")
JWT_ALGORITHM = environ.get("JWT_ALGORITHM")
JWT_EXP_TIME = environ.get("JWT_EXP_TIME")

def generateToken(payload) -> str:
    encoded_jwt = jwt.encode(
        payload,
        JWT_SECRET,
        algorithm=JWT_ALGORITHM
    )
    return encoded_jwt
