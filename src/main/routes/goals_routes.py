from flask import Blueprint
from src.main.composer.create_goal_composer import create_goal_composer
from src.main.composer.list_all_goals_composer import list_all_goals_composer
from src.middlewares.decorators import protected_route
from src.adapters import FlaskAdapter

goals_routes_bp = Blueprint("goals_routes_bp", __name__)

@goals_routes_bp.route("/goals", methods=["POST"])
@protected_route
def create_goal(token_info: dict):
    view = create_goal_composer()
    adapter = FlaskAdapter(view)
    return adapter.route_handler(token_info=token_info)

@goals_routes_bp.route("/goals", methods=["GET"])
@protected_route
def list_all_goals(token_info: dict):
    view = list_all_goals_composer()
    adapter = FlaskAdapter(view)
    return adapter.route_handler(token_info=token_info)
