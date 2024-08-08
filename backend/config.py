import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') 
    MONGO_URI = os.environ.get('MONGO_URI') 
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY') 
