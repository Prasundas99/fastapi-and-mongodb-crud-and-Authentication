from database.entity.userEntity import User
from fastapi import HTTPException, status
from util.ResponseSchema import successResponse, errorResponse
from database.entity.userEntity import User
from auth.tokenGenerator import generateToken
from passlib.hash import bcrypt
from datetime import datetime, timedelta, timezone

async def registerController(name: str, email: str, password: str):
    user = await User.find_one_user_by_email(user_email=email)
    if user:
        response = errorResponse("User with this email does not exist")
        print("user not found:", response)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response)
    try:
        new_user = await User.create_user(name=name, email=email, password=password)
        return successResponse("User Registered", {
            "id": str(new_user.id),
            "username": new_user.name,
            "email": new_user.email,
        })
    except Exception as ex:
        print("exception under Register controller:", ex)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=errorResponse("Internal Server Error"))


async def loginController(email: str, password: str):
    db_user = await User.find_one_user_by_email(email)
    if not db_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=errorResponse("User with this email does not exist"))    
    try:
        if not bcrypt.verify(password, db_user['password']):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=errorResponse("Invalid password"))

        token = generateToken({"_id": str(db_user['_id']) ,"exp": datetime.now(tz=timezone.utc) + timedelta(days=69)})
        return successResponse("User Logged In",{
            "data": {
                "token": token,
            }
        })
    except Exception as e:
        print("exception under Login controller:", e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=errorResponse("Internal Server Error"), headers={"X-Error": str(e)})
