from uuid import uuid4
from src.models.entities import Task, Goal
from .list_all_controller import ListAllController

USER_ID = str(uuid4())
GOAL_ID = str(uuid4())

class GoalsRepositoryMock:
    def __init__(self) -> None:
        self.find_by_id_attributes = {}

    def find_by_id(self, goal_id: str) -> Goal:
        self.find_by_id_attributes["goal_id"] = goal_id
        return Goal(id=GOAL_ID, user_id=USER_ID)

class TasksRepositoryMock:
    def __init__(self) -> None:
        self.find_all_attributes = {}

    def find_all(self, goal_id: str = None, filters: dict = None) -> list[Task]:
        self.find_all_attributes["goal_id"] = goal_id
        self.find_all_attributes["filters"] = filters
        goal = Goal(id=GOAL_ID, user_id=USER_ID)
        return [
            Task(id="1", goal_id=GOAL_ID, goal=goal),
            Task(id="2", goal_id=GOAL_ID, goal=goal)
        ]

def test_list_all_controler():
    mock_goals_repository = GoalsRepositoryMock()
    mock_tasks_repository = TasksRepositoryMock()
    controller = ListAllController(
        goals_repository=mock_goals_repository,
        tasks_repository=mock_tasks_repository,
    )

    response = controller.list_all(user_id=USER_ID, goal_id=GOAL_ID)

    assert mock_goals_repository.find_by_id_attributes["goal_id"] == GOAL_ID
    assert mock_tasks_repository.find_all_attributes["goal_id"] == GOAL_ID
    assert mock_tasks_repository.find_all_attributes["filters"] is None
    assert response["data"]["count"] == 2
