from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException
from datetime import datetime

from auth.authBearer import JWTBearer
from database.entity.userEntity import User
from database.collections import init_db
from middlewares.errorException import custom_exception_handler

from routes.user import user as userRouter
from routes.auth import auth as authRouter
from util.ResponseSchema import successResponse

app = FastAPI()

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
   return custom_exception_handler(request, exc)


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
    return successResponse("Welcome to FastAPI", {
        "deployedTime": deployedTime
    })

app.include_router(authRouter, tags=['auth'], prefix='/auth')
app.include_router(userRouter, tags=['user'], prefix='/users' , dependencies=[Depends(get_token_header)])
