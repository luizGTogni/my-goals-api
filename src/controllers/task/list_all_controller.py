from src.models.repositories.interfaces.goals_repository import IGoalsRepository
from src.models.repositories.interfaces.tasks_repository import ITasksRepository
from src.controllers.interfaces.task.list_all_controller import IListAllController
from src.types.errors import HttpUnauthorizedError, HttpNotFoundError
from src.models.entities import Task, Goal

class ListAllController(IListAllController):
    def __init__(
            self,
            goals_repository: IGoalsRepository,
            tasks_repository: ITasksRepository,
        ) -> None:
        self.__goals_repository = goals_repository
        self.__tasks_repository = tasks_repository

    def list_all(self, user_id: str, goal_id: str, filters: dict = None) -> dict:
        owner = self.__get_owner(goal_id)
        self.__verify_same_goal_owner(user_id, owner)
        tasks = self.__get_tasks(goal_id, filters)
        return self.__format_response(tasks)

    def __get_owner(self, goal_id: str) -> Goal:
        goal = self.__goals_repository.find_by_id(goal_id)

        if not goal:
            raise HttpNotFoundError("Goal not found")

        return goal

    def __verify_same_goal_owner(self, user_id: str, owner: Goal) -> None:
        if user_id != str(owner.user_id):
            raise HttpUnauthorizedError("You're not permission")

    def __get_tasks(self, goal_id: str, filters: dict = None) -> list[Task]:
        tasks = self.__tasks_repository.find_all(goal_id, filters)
        return tasks

    def __format_response(self, tasks: list[Task]) -> dict:
        tasks_list = [task.to_dict() for task in tasks]
        return {
            "data": {
                "type": "Tasks",
                "count": len(tasks_list),
                "tasks": tasks_list
            }
        }
