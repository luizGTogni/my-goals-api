from uuid import uuid4
from pytest import raises
from src.models.entities import Goal
from src.types.errors import HttpNotFoundError, HttpUnauthorizedError
from .create_controller import CreateTaskController

USER_ID = str(uuid4)
GOAL_ID = str(uuid4)

class GoalsRepositoryMock:
    def __init__(self) -> None:
        self.find_by_id_attributes = {}

    def find_by_id(self, goal_id: str) -> Goal:
        if goal_id == "uuid_goal_not_exists":
            return None

        self.find_by_id_attributes["goal_id"] = goal_id
        return Goal(id=GOAL_ID, user_id=USER_ID)

class TasksRepositoryMock:
    def __init__(self) -> None:
        self.create_attributes = {}

    def create(self, title: str, description: str, owner: Goal) -> None:
        self.create_attributes["title"] = title
        self.create_attributes["description"] = description
        self.create_attributes["owner"] = owner

def test_create_goal():
    mock_goals_repository = GoalsRepositoryMock()
    mock_tasks_repository = TasksRepositoryMock()
    controller = CreateTaskController(
        goals_repository=mock_goals_repository,
        tasks_repository=mock_tasks_repository,
    )

    response = controller.create(
        title="Task Title",
        description="Task Description",
        user_id=USER_ID,
        goal_id=GOAL_ID
    )

    assert mock_goals_repository.find_by_id_attributes["goal_id"] == GOAL_ID
    assert mock_tasks_repository.create_attributes["title"] == "Task Title"
    assert mock_tasks_repository.create_attributes["description"] == "Task Description"
    assert isinstance(mock_tasks_repository.create_attributes["owner"], Goal)
    assert mock_tasks_repository.create_attributes["owner"].id == GOAL_ID

    assert response == {
        "data": {
            "type": "Task",
            "count": 1,
            "message": "Task created successfully"
        }
    }

def test_create_task_error_owner_not_found():
    mock_goals_repository = GoalsRepositoryMock()
    mock_tasks_repository = TasksRepositoryMock()
    controller = CreateTaskController(
        goals_repository=mock_goals_repository,
        tasks_repository=mock_tasks_repository,
    )

    with raises(HttpNotFoundError):
        controller.create(
            title="Task Title",
            description="Task Description",
            user_id=USER_ID,
            goal_id="uuid_goal_not_exists"
        )

def test_create_task_error_not_same_owner():
    mock_goals_repository = GoalsRepositoryMock()
    mock_tasks_repository = TasksRepositoryMock()
    controller = CreateTaskController(
        goals_repository=mock_goals_repository,
        tasks_repository=mock_tasks_repository,
    )

    with raises(HttpUnauthorizedError):
        controller.create(
            title="Task Title",
            description="Task Description",
            user_id="uuid_not_same_owner_goal",
            goal_id=GOAL_ID
        )
