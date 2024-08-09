from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import get_chat_collection
from utils import analyze_sentiment, translate_message, generate_ai_response

chat_bp = Blueprint('chat', __name__)