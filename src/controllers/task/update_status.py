from src.models.repositories.interfaces.goals_repository import IGoalsRepository
from src.models.repositories.interfaces.tasks_repository import ITasksRepository
from src.controllers.interfaces.task.update_status import IUpdateStatusTask
from src.models.entities.task import StatusTaskEnum
from src.types.errors import HttpNotFoundError, HttpBadRequestError, HttpUnauthorizedError

class UpdateStatusTask(IUpdateStatusTask):
    def __init__(
            self,
            goals_repository: IGoalsRepository,
            tasks_repository: ITasksRepository,
        ) -> None:
        self.__goals_repository = goals_repository
        self.__tasks_repository = tasks_repository

    def update_status(
        self,
        goal_id: str,
        task_id: str,
        new_status: StatusTaskEnum
    ) -> dict:
        self.__verify_if_goal_exists(goal_id)
        self.__verify_if_task_exists(task_id)
        self.__verify_if_task_exists_in_goal(goal_id, task_id)
        self.__update_in_db(task_id, new_status)
        return self.__format_response()

    def __verify_if_goal_exists(self, goal_id: str) -> None:
        goal = self.__goals_repository.find_by_id(goal_id)

        if not goal:
            raise HttpNotFoundError("Goal not found")

    def __verify_if_task_exists(self, task_id: str) -> None:
        task = self.__tasks_repository.find_by_id(task_id)

        if not task:
            raise HttpNotFoundError("Task not found")

    def __verify_if_task_exists_in_goal(self, goal_id: str, task_id: str) -> None:
        task = self.__tasks_repository.find_by_id(task_id)

        if str(task.goal_id) != goal_id:
            raise HttpUnauthorizedError("You're not permission")

    def __update_in_db(self, task_id: str, new_status: StatusTaskEnum) -> None:
        if new_status not in StatusTaskEnum:
            raise HttpBadRequestError("New status invalid")

        self.__tasks_repository.update_status(task_id, new_status)

    def __format_response(self) -> dict:
        return {
            "data": {
                "type": "Task",
                "count": 1,
                "message": "Update status successfully"
            }
        }
