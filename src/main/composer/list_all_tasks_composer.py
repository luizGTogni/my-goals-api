from src.models.settings.connection import db_connection_handler
from src.models.repositories.goals_repository import GoalsRepository
from src.models.repositories.tasks_repository import TasksRepository
from src.controllers.task.list_all_controller import ListAllController
from src.views.task.list_all_view import ListAllView
from src.views.interfaces.view import IView

def list_all_tasks_composer() -> IView:
    tasks_repository = TasksRepository(db_conn=db_connection_handler)
    goals_repository = GoalsRepository(db_conn=db_connection_handler)
    controller = ListAllController(
        goals_repository=goals_repository,
        tasks_repository=tasks_repository,
    )
    view = ListAllView(list_all_controller=controller)
    return view
