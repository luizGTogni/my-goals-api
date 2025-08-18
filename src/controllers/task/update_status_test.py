from uuid import uuid4
from src.models.entities.goal import Goal
from src.models.entities.task import Task, StatusTaskEnum
from .update_status import UpdateStatusTask

GOAL_ID=str(uuid4())
TASK_ID=str(uuid4())

class GoalsRepositoryMock:
    def __init__(self) -> None:
        self.find_by_id_attributes = {}

    def find_by_id(self, goal_id: str) -> Goal:
        self.find_by_id_attributes["goal_id"] = goal_id
        return Goal(id=GOAL_ID)

class TasksRepositoryMock:
    def __init__(self) -> None:
        self.find_by_id_attributes = {}
        self.update_status_attributes = {}

    def find_by_id(self, task_id: str) -> Task:
        self.find_by_id_attributes["task_id"] = task_id
        return Task(id="1", goal_id=GOAL_ID)

    def update_status(self, task_id: str, new_status: StatusTaskEnum) -> None:
        self.update_status_attributes["task_id"] = task_id
        self.update_status_attributes["new_status"] = new_status

def test_update_status_goal():
    mock_goals_repository = GoalsRepositoryMock()
    mock_tasks_repository = TasksRepositoryMock()
    controller = UpdateStatusTask(
        goals_repository=mock_goals_repository,
        tasks_repository=mock_tasks_repository
        )
    response = controller.update_status(
        goal_id=GOAL_ID,
        task_id=TASK_ID,
        new_status=StatusTaskEnum.DONE
    )

    assert mock_goals_repository.find_by_id_attributes["goal_id"] == GOAL_ID
    assert mock_tasks_repository.update_status_attributes["task_id"] == TASK_ID
    assert mock_tasks_repository.update_status_attributes["new_status"] == StatusTaskEnum.DONE
    assert response == {
        "data": {
            "type": "Task",
            "count": 1,
            "message": "Update status successfully"
        }
    }
