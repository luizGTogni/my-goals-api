from flask import Blueprint
from src.main.composer.create_task_composer import create_task_composer
from src.middlewares.decorators import protected_route
from src.adapters import FlaskAdapter

tasks_routes_bp = Blueprint("tasks_routes_bp", __name__)

@tasks_routes_bp.route("/tasks", methods=["POST"])
@protected_route
def create_user(token_info: dict):
    view = create_task_composer()
    adapter = FlaskAdapter(view)
    return adapter.route_handler(token_info=token_info)
