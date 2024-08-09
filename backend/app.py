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

# SocketIO Setup
socketio = SocketIO(app, cors_allowed_origins="*")

# MongoDB Setup
client = MongoClient(app.config['MONGO_URI'])
db = client.get_database()

# Register Blueprints
from auth import auth_bp
from chat import chat_bp

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(chat_bp, url_prefix='/api/chat')

if __name__ == "__main__":
    socketio.run(app, debug=True)
