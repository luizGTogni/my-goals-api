from src.models.settings.sqlite_connection import sqlite_connection_handler
from src.models.repositories.goals_repository import GoalsRepository
from src.models.repositories.tasks_repository import TasksRepository
from src.controllers.task.create_controller import CreateTaskController
from src.views.task.create_view import CreateTaskView
from src.views.interfaces.view import IView

def create_task_composer() -> IView:
    goals_repository = GoalsRepository(db_conn=sqlite_connection_handler)
    tasks_repository = TasksRepository(db_conn=sqlite_connection_handler)
    controller = CreateTaskController(
        goals_repository=goals_repository,
        tasks_repository=tasks_repository,
    )
    view = CreateTaskView(create_controller=controller)
    return view
