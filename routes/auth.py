from fastapi import APIRouter
from models.authModel import UserLoginSchema, UserRegisterSchema, UserRegisterResponseSchema
from controllers.authController import registerController, loginController

auth = APIRouter()

@auth.post('/register', response_model=UserRegisterResponseSchema)
async def register(user: UserRegisterSchema):
    return await registerController(user.username, user.email, user.password)
    

@auth.post('/login')
async def login(user: UserLoginSchema):
    return await loginController(user.email, user.password)