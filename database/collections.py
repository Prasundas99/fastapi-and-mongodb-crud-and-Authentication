from motor.motor_asyncio import AsyncIOMotorClient
from config.globals import DB_URI , DB_NAME

def init_db():
    client = AsyncIOMotorClient(DB_URI)
    db = client[DB_NAME]
    return db



