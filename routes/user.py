from fastapi import APIRouter, Depends
from auth.authBearer import JWTBearer
from database.collections import get_user_collection, init_db
from models.userModel import GetAllUserResponseSchema
from database.entity.userEntity import User
from util.ResponseSchema import successResponse

user = APIRouter()


@user.get('/', response_model=GetAllUserResponseSchema)
async def find_all_users(userEntity=Depends(get_user_collection)):
    # print("current_user:", current_user)
    data = await User.find_all_users(userEntity)
    return successResponse("All Users " + str(len(data)), data)
