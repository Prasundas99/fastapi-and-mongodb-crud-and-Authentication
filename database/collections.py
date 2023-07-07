from pymongo import MongoClient
from pymongo.errors import PyMongoError
from config.globals import DB_URI, DB_NAME


def init_db():
    mongo_client = MongoClient(DB_URI)
    db = mongo_client[DB_NAME]
    return db
