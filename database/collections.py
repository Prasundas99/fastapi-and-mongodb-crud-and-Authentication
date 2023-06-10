from motor.motor_asyncio import AsyncIOMotorClient
from config.globals import DB_URI , DB_NAME

client = AsyncIOMotorClient(DB_URI)
db = client[DB_NAME]

userEntity = db['users']


