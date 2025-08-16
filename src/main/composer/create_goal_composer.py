from src.models.settings.connection import db_connection_handler
from src.models.repositories.users_repository import UsersRepository
from src.models.repositories.goals_repository import GoalsRepository
from src.controllers.goal.create_controller import CreateGoalController
from src.views.goal.create_view import CreateGoalView
from src.views.interfaces.view import IView

def create_goal_composer() -> IView:
    users_repository = UsersRepository(db_conn=db_connection_handler)
    goals_repository = GoalsRepository(db_conn=db_connection_handler)
    controller = CreateGoalController(
        users_repository=users_repository,
        goals_repository=goals_repository
    )
    view = CreateGoalView(create_controller=controller)
    return view
