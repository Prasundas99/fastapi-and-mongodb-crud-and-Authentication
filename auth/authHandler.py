from os import environ
import jwt
import time


def decodeJWT(token: str) -> dict:
    JWT_SECRET = environ.get("JWT_SECRET")
    JWT_ALGORITHM = environ.get("JWT_ALGORITHM")

    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["exp"] >= time.time() else None
    except:
        print("------------------Error in decoding JWT---------------------")
        return {}
