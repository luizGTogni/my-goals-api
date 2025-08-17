from src.controllers.interfaces.task.create_controller import ICreateTaskController
from src.models.repositories.interfaces.goals_repository import IGoalsRepository
from src.models.repositories.interfaces.tasks_repository import ITasksRepository
from src.types.errors import HttpNotFoundError, HttpUnauthorizedError
from src.models.entities import Goal

class CreateTaskController(ICreateTaskController):
    def __init__(
            self,
            goals_repository: IGoalsRepository,
            tasks_repository: ITasksRepository,
        ) -> None:
        self.__goals_repository = goals_repository
        self.__tasks_repository = tasks_repository

    def create(self, title: str, description: str, user_id: str, goal_id: str) -> dict:
        owner = self.__get_owner(goal_id)
        self.__verify_same_goal_owner(user_id, owner)
        self.__insert_in_db(title, description, owner)

        return self.__format_response()

    def __get_owner(self, goal_id: str) -> Goal:
        goal = self.__goals_repository.find_by_id(goal_id)

        if not goal:
            raise HttpNotFoundError("Goal not found")

        return goal

    def __verify_same_goal_owner(self, user_id: str, owner: Goal) -> None:
        if user_id != str(owner.user_id):
            raise HttpUnauthorizedError("You're not permission")

    def __insert_in_db(self, title: str, description: str, owner: Goal) -> None:
        self.__tasks_repository.create(title, description, owner)

    def __format_response(self) -> dict:
        return {
            "data": {
                "type": "Task",
                "count": 1,
                "message": "Task created successfully"
            }
        }
