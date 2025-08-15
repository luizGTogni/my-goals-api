from flask import Blueprint
from src.main.composer.create_user_composer import create_user_composer
from src.middlewares.decorators.error_handler import error_handler
from src.adapters import FlaskAdapter

users_routes_bp = Blueprint("users_routes_bp", __name__)

@users_routes_bp.route("/users", methods=["POST"])
@error_handler
def create_user():
    view = create_user_composer()
    flask_adapter = FlaskAdapter(view)
    return flask_adapter.route_handler()
