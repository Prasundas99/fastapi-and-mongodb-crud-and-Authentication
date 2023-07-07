from fastapi import FastAPI, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import JSONResponse
from datetime import datetime

from database.entity.userEntity import User

from auth.authBearer import JWTBearer
from database.collections import init_db

from routes.user import user as userRouter
from routes.auth import auth as authRouter

app = FastAPI()


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(exc.detail, status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(exc, status_code=status.HTTP_400_BAD_REQUEST)

# startup event


@app.on_event("startup")
async def startup_event():
    db = init_db()
    await User.create_indexes(db)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

get_token_header = JWTBearer()
deployedTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@app.get('/')
async def index():
    return {
        "message": "Welcome to FastAPI",
        "success": True,
        "data": {
            "deployedTime": deployedTime
        }
    }

app.include_router(authRouter, tags=['auth'], prefix='/auth')
app.include_router(userRouter, tags=['user'], prefix='/user')
