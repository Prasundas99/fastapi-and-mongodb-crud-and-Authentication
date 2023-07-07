from enum import Enum
from fastapi import Depends
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from config.globals import DB_URI, DB_NAME


class Collections(Enum):
    USERS = "users"


def init_db():
    mongo_client = MongoClient(DB_URI)
    db = mongo_client[DB_NAME]
    return db


def get_user_collection(db=Depends(init_db)):
    return db[Collections.USERS.value]
