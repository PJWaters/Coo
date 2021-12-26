import motor.motor_asyncio, asyncio
from config import MONGO_URI, MONGO_DB_NAME

def connect_to_mongo(uri, db_name):
    client = motor.motor_asyncio.AsyncIOMotorClient(uri)
    client.get_io_loop = asyncio.get_running_loop
    db = client.get_database(db_name)
    return db

db = connect_to_mongo(MONGO_URI, MONGO_DB_NAME)