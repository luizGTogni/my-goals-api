from src.models.repositories.interfaces.goals_repository import IGoalsRepository
from src.controllers.interfaces.goal.update_status import IUpdateStatusGoal
from src.models.entities.goal import StatusEnum
from src.types.errors import HttpNotFoundError, HttpBadRequestError

class UpdateStatusGoal(IUpdateStatusGoal):
    def __init__(self, goals_repository: IGoalsRepository) -> None:
        self.__goals_repository = goals_repository

    def update_status(self, goal_id: str, new_status: StatusEnum) -> dict:
        self.__verify_if_goal_exists(goal_id)
        self.__update_in_db(goal_id, new_status)
        return self.__format_response()

    def __verify_if_goal_exists(self, goal_id: str) -> None:
        goal = self.__goals_repository.find_by_id(goal_id)

        if not goal:
            raise HttpNotFoundError("Goal not found")

    def __update_in_db(self, goal_id: str, new_status: StatusEnum) -> None:
        if new_status not in StatusEnum:
            raise HttpBadRequestError("New status invalid")

        self.__goals_repository.update_status(goal_id, new_status)

    def __format_response(self) -> dict:
        return {
            "data": {
                "type": "Goal",
                "count": 1,
                "message": "Update status successfully"
            }
        }
