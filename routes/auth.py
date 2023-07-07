from fastapi import APIRouter, Depends
from database.collections import get_user_collection, init_db
from models.authModel import UserLoginSchema, UserRegisterSchema, UserRegisterResponseSchema
from controllers.authController import registerController, loginController

auth = APIRouter()


@auth.post('/register', response_model=UserRegisterResponseSchema)
async def register(user: UserRegisterSchema, userEntity=Depends(get_user_collection)):
    return await registerController(user.username, user.email, user.password, userEntity)


@auth.post('/login')
async def login(user: UserLoginSchema, userEntity=Depends(get_user_collection)):
    return await loginController(user.email, user.password, userEntity)
