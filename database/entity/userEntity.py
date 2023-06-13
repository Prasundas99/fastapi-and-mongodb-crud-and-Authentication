from fastapi import HTTPException
from bson.objectid import ObjectId
from passlib.hash import bcrypt
from pydantic import BaseModel, EmailStr

from database.collections import userEntity

class User(BaseModel):
    id: str
    name: str
    email: EmailStr
    password: str

    @staticmethod
    async def create_user(name: str, email: str, password: str):
        hashed_password = bcrypt.hash(password)
        user_data = {"name": name, "email": email, "password": hashed_password}
        print(user_data)
        result = await userEntity.insert_one(user_data)
        print(result)
        user_id = str(result.inserted_id)
        return User(id=user_id, name=name, email=email, password=hashed_password)

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
            item = User(id=user_id, name=document["name"], email=document["email"], password=document["password"])
            users.append(item.dict())
        return users

    @staticmethod
    async def find_one_user_by_id(user_id: str):
        document = await userEntity.find_one({"_id": ObjectId(user_id)})
        if not document:
            raise HTTPException(status_code=404, detail="User not found")
        return User(id=str(document["_id"]), name=document["name"], email=document["email"], password=document["password"])

    @staticmethod
    async def find_one_user_by_email(user_email: str):
        return  await userEntity.find_one({"email": user_email})
    # Create indexes on id and email fields
    async def create_indexes():
        await userEntity.create_index("id")
        await userEntity.create_index("email", unique=True)