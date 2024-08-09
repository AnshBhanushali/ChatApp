from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from pymongo import MongoClient
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# CORS Setup
CORS(app)

# SocketIO Setup
socketio = SocketIO(app, cors_allowed_origins="*")

# MongoDB Setup
client = MongoClient(app.config['MONGO_URI'])
db = client.get_database()

# Register blueprints (without auth)
from chat import chat_bp

app.register_blueprint(chat_bp, url_prefix='/api/chat')

if __name__ == "__main__":
    socketio.run(app, debug=True)
