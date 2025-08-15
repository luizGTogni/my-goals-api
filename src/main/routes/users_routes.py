from flask import Blueprint
from src.main.composer.create_user_composer import create_user_composer
from src.main.composer.login_composer import login_composer
from src.middlewares.decorators import error_handler
from src.adapters import FlaskAdapter

users_routes_bp = Blueprint("users_routes_bp", __name__)

@users_routes_bp.route("/users", methods=["POST"])
@error_handler
def create_user():
    view = create_user_composer()
    adapter = FlaskAdapter(view)
    return adapter.route_handler()

@users_routes_bp.route("/session", methods=["POST"])
@error_handler
def login():
    view = login_composer()
    adapter = FlaskAdapter(view)
    return adapter.route_handler()
