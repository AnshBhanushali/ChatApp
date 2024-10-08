from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from models import get_user_collection

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"msg": "Missing username or password"}), 400

    user_collection = get_user_collection()
    if user_collection.find_one({"username": username}):
        return jsonify({"msg": "User already exists"}), 400

    hashed_password = generate_password_hash(password)
    user_collection.insert_one({
        "username": username,
        "password": hashed_password
    })

    return jsonify({"msg": "User registered successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user_collection = get_user_collection()
    user = user_collection.find_one({"username": username})

    if not user or not check_password_hash(user['password'], password):
        return jsonify({"msg": "Invalid credentials"}), 401

    access_token = create_access_token(identity=user['username'])
    return jsonify(access_token=access_token), 200