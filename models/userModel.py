from typing import List
from pydantic import BaseModel, EmailStr

class DataResponseBody(BaseModel):
    id: str 
    name: str 
    email: EmailStr 
    password: str


class GetAllUserResponseSchema(BaseModel):
    success: bool
    message: str
    data: List[DataResponseBody]