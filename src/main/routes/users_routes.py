from flask import Blueprint, request, jsonify
from src.main.composer.create_user_composer import create_user_composer

users_routes_bp = Blueprint("users_routes_bp", __name__)

@users_routes_bp.route("/users", methods=["POST"])
def create_user():
    http_request = request.json
    view = create_user_composer()
    http_response = view.handle(http_request)

    return jsonify(http_response.body), http_response.status_code
