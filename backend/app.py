from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_socketio import SocketIO
from pymongo import MongoClient
from config import Config
import spacy