from flask import Blueprint
from src.main.composer.create_task_composer import create_task_composer
from src.middlewares.decorators import protected_route
from src.adapters import FlaskAdapter

tasks_routes_bp = Blueprint("tasks_routes_bp", __name__)

@tasks_routes_bp.route("/goals/<goal_id>/tasks", methods=["POST"])
@protected_route
def create_user(goal_id: str, token_info: dict):
    view = create_task_composer()
    adapter = FlaskAdapter(view)
    return adapter.route_handler(
        params={ "goal_id": goal_id },
        token_info=token_info
    )
