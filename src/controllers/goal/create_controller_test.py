from uuid import uuid4
from pytest import raises
from src.models.entities import User
from src.types.errors import HttpNotFoundError
from .create_controller import CreateGoalController

USER_ID = str(uuid4)

class UsersRepositoryMock:
    def __init__(self) -> None:
        self.find_by_id_attributes = {}

    def find_by_id(self, user_id: str) -> User:
        if user_id == "uuid_user_not_exists":
            return None

        self.find_by_id_attributes["user_id"] = user_id
        return User(id=USER_ID)

class GoalsRepositoryMock:
    def __init__(self) -> None:
        self.create_attributes = {}

    def create(self, title: str, description: str, owner: User) -> None:
        self.create_attributes["title"] = title
        self.create_attributes["description"] = description
        self.create_attributes["owner"] = owner

def test_create_goal():
    mock_users_repository = UsersRepositoryMock()
    mock_goals_repository = GoalsRepositoryMock()
    controller = CreateGoalController(
        users_repository=mock_users_repository,
        goals_repository=mock_goals_repository
    )

    response = controller.create(
        title="Goal Title",
        description="Goal Description",
        user_id=USER_ID
    )

    assert mock_users_repository.find_by_id_attributes["user_id"] == USER_ID
    assert mock_goals_repository.create_attributes["title"] == "Goal Title"
    assert mock_goals_repository.create_attributes["description"] == "Goal Description"
    assert isinstance(mock_goals_repository.create_attributes["owner"], User)
    assert mock_goals_repository.create_attributes["owner"].id == USER_ID

    assert response == {
        "data": {
            "type": "Goal",
            "count": 1,
            "message": "Goal created successfully"
        }
    }

def test_create_goal_error_owner_not_found():
    mock_users_repository = UsersRepositoryMock()
    mock_goals_repository = GoalsRepositoryMock()
    controller = CreateGoalController(
        users_repository=mock_users_repository,
        goals_repository=mock_goals_repository
    )

    with raises(HttpNotFoundError):
        controller.create(
            title="Goal Title",
            description="Goal Description",
            user_id="uuid_user_not_exists"
        )
