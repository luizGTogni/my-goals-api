from src.models.repositories.interfaces.goals_repository import IGoalsRepository
from src.controllers.interfaces.goal.list_all_controller import IListAllController
from src.models.entities import Goal

class ListAllController(IListAllController):
    def __init__(self, goals_repository: IGoalsRepository) -> None:
        self.__goals_repository = goals_repository

    def list_all(self, user_id: str, filters: dict = None) -> dict:
        goals = self.__get_goals(user_id, filters)
        return self.__format_response(goals)

    def __get_goals(self, user_id: str, filters: dict = None) -> list[Goal]:
        goals = self.__goals_repository.find_all(user_id, filters)
        return goals

    def __format_response(self, goals: list[Goal]) -> dict:
        goals_list = [goal.to_dict() for goal in goals]
        return {
            "data": {
                "type": "Goals",
                "count": len(goals_list),
                "goals": goals_list
            }
        }
