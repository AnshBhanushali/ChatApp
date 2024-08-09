from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import get_chat_collection
from utils import analyze_sentiment, translate_message, generate_ai_response

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/message', methods=['POST'])
@jwt_required()
def save_message():
    data = request.get_json()
    username = get_jwt_identity()
    message = data.get('message')
    target_language = data.get('language', 'en')  # Default to English if no language is specified

    if not message:
        return jsonify({"msg": "Message content is missing"}), 400

    translated_message = translate_message(message, target_language=target_language)
    sentiment = analyze_sentiment(translated_message)
    ai_response = generate_ai_response(translated_message)

    chat_collection = get_chat_collection()
    chat_collection.insert_one({
        "username": username,
        "original_message": message,
        "translated_message": translated_message,
        "sentiment": sentiment,
        "ai_response": ai_response
    })

    return jsonify({"msg": "Message saved", "ai_response": ai_response}), 201

@chat_bp.route('/history', methods=['GET'])
@jwt_required()
def get_chat_history():
    username = get_jwt_identity()
    chat_collection = get_chat_collection()
    history = list(chat_collection.find({"username": username}))

    return jsonify(history), 200
