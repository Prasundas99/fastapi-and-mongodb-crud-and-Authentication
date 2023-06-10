from os import environ
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from .authHandler import decodeJWT

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self
        ).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme."
                )

            payload, isTokenValid = self.verify_jwt(credentials.credentials)
            if not isTokenValid:
                raise HTTPException(
                    status_code=403, detail="Invalid token or expired token."
                )
            return payload
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        isTokenValid: bool = False
        try:
            payload = decodeJWT(jwtoken)
        except:
            payload = None
        if payload:
            isTokenValid = True
        return payload, isTokenValid
    
    def generateToken(self, payload: dict) -> str:
        JWT_SECRET = environ.get("JWT_SECRET")
        JWT_ALGORITHM = environ.get("JWT_ALGORITHM")
        JWT_EXP_TIME = environ.get("JWT_EXP_TIME")
        encoded_jwt = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM, exp=JWT_EXP_TIME)
        return encoded_jwt
