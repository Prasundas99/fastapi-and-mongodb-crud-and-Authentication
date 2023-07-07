from fastapi import APIRouter, Depends
from auth.authBearer import JWTBearer
from database.collections import init_db
from models.userModel import GetAllUserResponseSchema
from database.entity.userEntity import User
from util.ResponseSchema import successResponse

user = APIRouter()


@user.get('/', response_model=GetAllUserResponseSchema)
async def find_all_users(db=Depends(init_db)):
    # print("current_user:", current_user)
    data = await User.find_all_users(db)
    return successResponse("All Users " + str(len(data)), data)
