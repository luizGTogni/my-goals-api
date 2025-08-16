from src.controllers.interfaces.goal.create_controller import ICreateGoalController
from src.models.repositories.interfaces.users_repository import IUsersRepository
from src.models.repositories.interfaces.goals_repository import IGoalsRepository
from src.types.errors import HttpNotFoundError
from src.models.entities import User

class CreateGoalController(ICreateGoalController):
    def __init__(
            self,
            users_repository: IUsersRepository,
            goals_repository: IGoalsRepository,
        ) -> None:
        self.__users_repository = users_repository
        self.__goals_repository = goals_repository

    def create(self, title: str, description: str, user_id: str) -> dict:
        owner = self.__get_owner(user_id)
        self.__insert_in_db(title, description, owner)

        return self.__format_response()

    def __get_owner(self, user_id: str) -> User:
        user = self.__users_repository.find_by_id(user_id)

        if not user:
            raise HttpNotFoundError("User not found")

        return user

    def __insert_in_db(self, title: str, description: str, owner: User) -> None:
        self.__goals_repository.create(title, description, owner)

    def __format_response(self) -> dict:
        return {
            "data": {
                "type": "Goal",
                "count": 1,
                "message": "Goal created successfully"
            }
        }
