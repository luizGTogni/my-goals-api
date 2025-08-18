from flask import Blueprint
from src.main.composer.create_task_composer import create_task_composer
from src.main.composer.list_all_tasks_composer import list_all_tasks_composer
from src.main.composer.update_status_task_composer import update_status_task_composer
from src.middlewares.decorators import protected_route
from src.adapters import FlaskAdapter

tasks_routes_bp = Blueprint("tasks_routes_bp", __name__)

@tasks_routes_bp.route("/goals/<goal_id>/tasks", methods=["POST"])
@protected_route
def create_task(goal_id: str, token_info: dict):
    view = create_task_composer()
    adapter = FlaskAdapter(view)
    return adapter.route_handler(
        params={ "goal_id": goal_id },
        token_info=token_info
    )

@tasks_routes_bp.route("/goals/<goal_id>/tasks", methods=["GET"])
@protected_route
def list_all_tasks(goal_id: str, token_info: dict):
    view = list_all_tasks_composer()
    adapter = FlaskAdapter(view)
    return adapter.route_handler(
        params={ "goal_id": goal_id },
        token_info=token_info
    )

@tasks_routes_bp.route("/goals/<goal_id>/tasks/<task_id>/status", methods=["PATCH"])
@protected_route
def update_status_task(goal_id: str, task_id: str, token_info: dict):
    view = update_status_task_composer()
    adapter = FlaskAdapter(view)
    return adapter.route_handler(
        params={ "goal_id": goal_id, "task_id": task_id },
        token_info=token_info
    )
