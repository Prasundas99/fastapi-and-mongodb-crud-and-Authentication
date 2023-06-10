from fastapi import APIRouter, Depends
from auth.authBearer import JWTBearer
from models.userModel import GetAllUserResponseSchema
from database.entity.userEntity import User
from util.ResponseSchema import successResponse

user = APIRouter() 

@user.get('/', response_model=GetAllUserResponseSchema)
async def find_all_users(current_user = Depends(JWTBearer())): 
    print("current_user:", current_user)
    data = await User.find_all_users()
    return successResponse("All Users", data)

                        
    
