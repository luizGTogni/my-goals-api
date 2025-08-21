from src.models.settings.sqlite_connection import sqlite_connection_handler
from src.models.repositories.goals_repository import GoalsRepository
from src.controllers.goal.update_status import UpdateStatusGoal
from src.views.goal.update_status_view import UpdateStatusGoalView
from src.views.interfaces.view import IView

def update_status_goal_composer() -> IView:
    goals_repository = GoalsRepository(db_conn=sqlite_connection_handler)
    controller = UpdateStatusGoal(
        goals_repository=goals_repository
    )
    view = UpdateStatusGoalView(update_status_controller=controller)
    return view
