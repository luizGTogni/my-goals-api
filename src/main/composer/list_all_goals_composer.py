from src.models.settings.connection import db_connection_handler
from src.models.repositories.goals_repository import GoalsRepository
from src.controllers.goal.list_all_controller import ListAllController
from src.views.goal.list_all_view import ListAllView
from src.views.interfaces.view import IView

def list_all_goals_composer() -> IView:
    goals_repository = GoalsRepository(db_conn=db_connection_handler)
    controller = ListAllController(
        goals_repository=goals_repository,
    )
    view = ListAllView(list_all_controller=controller)
    return view
