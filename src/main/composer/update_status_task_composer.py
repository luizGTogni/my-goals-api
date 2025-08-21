from src.models.settings.sqlite_connection import sqlite_connection_handler
from src.models.repositories.goals_repository import GoalsRepository
from src.models.repositories.tasks_repository import TasksRepository
from src.controllers.task.update_status import UpdateStatusTask
from src.views.task.update_status_view import UpdateStatusTaskView
from src.views.interfaces.view import IView

def update_status_task_composer() -> IView:
    goals_repository = GoalsRepository(db_conn=sqlite_connection_handler)
    tasks_repository = TasksRepository(db_conn=sqlite_connection_handler)
    controller = UpdateStatusTask(
        goals_repository=goals_repository,
        tasks_repository=tasks_repository,
    )
    view = UpdateStatusTaskView(update_status_controller=controller)
    return view
