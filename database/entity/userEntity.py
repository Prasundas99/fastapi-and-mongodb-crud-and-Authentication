from fastapi import HTTPException
from bson.objectid import ObjectId
from passlib.hash import bcrypt
from pydantic import BaseModel, EmailStr
from datetime import datetime

from database.collections import userEntity

class User(BaseModel):
    id: str
    name: str
    email: EmailStr
    password: str
    createdAt: datetime
    updatedAt: datetime

    @staticmethod
    async def create_user(name: str, email: str, password: str):
        hashed_password = bcrypt.hash(password)
        current_time = datetime.now()
        user_data = {
            "name": name,
            "email": email,
            "password": hashed_password,
            "createdAt": current_time,
            "updatedAt": current_time
        }
        result = await userEntity.insert_one(user_data)
        user_id = str(result.inserted_id)
        return User(id=user_id, name=name, email=email, password=hashed_password, createdAt=current_time, updatedAt=current_time)

    @staticmethod
    async def delete_user(user_id: str):
        result = await userEntity.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count > 0

    @staticmethod
    async def find_all_users():
        cursor = userEntity.find()
        users = []
        async for document in cursor:
            user_id = str(document["_id"])
            item = User(
                id=user_id,
                name=document["name"],
                email=document["email"],
                password=document["password"],
                createdAt=document["createdAt"],
                updatedAt=document["updatedAt"]
            )
            users.append(item.dict())
        return users

    @staticmethod
    async def find_one_user_by_id(user_id: str):
        document = await userEntity.find_one({"_id": ObjectId(user_id)})
        if not document:
            raise HTTPException(status_code=404, detail="User not found")
        return User(
            id=str(document["_id"]),
            name=document["name"],
            email=document["email"],
            password=document["password"],
            createdAt=document["createdAt"],
            updatedAt=document["updatedAt"]
        )

    @staticmethod
    async def find_one_user_by_email(user_email: str):
        return await userEntity.find_one({"email": user_email})
    
    @staticmethod
    async def update_user(user_id: str, name: str, email: str):
        current_time = datetime.now()
        update_data = {"name": name, "email": email, "updatedAt": current_time}
        result = await userEntity.update_one({"_id": ObjectId(user_id)}, {"$set": update_data})
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="User not found")
        return True


    # Create indexes on id and email fields
    async def create_indexes():
        await userEntity.create_index("id")
        await userEntity.create_index("email", unique=True)