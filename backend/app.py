from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_socketio import SocketIO
from pymongo import MongoClient
from config import Config
import spacy

nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)
app.config.from_object(Config)

# JWT Setup
jwt = JWTManager(app)

# CORS Setup
CORS(app)