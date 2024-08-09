from pymongo import MongoClient
from config import Config

client = MongoClient(Config.MONGO_URI)
db = client.get_database()

def get_user_collection():
    return db['users']

def get_chat_collection():
    return db['chats']
