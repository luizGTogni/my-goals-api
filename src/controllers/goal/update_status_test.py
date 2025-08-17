from uuid import uuid4
from src.models.entities.goal import StatusEnum, Goal
from .update_status import UpdateStatusGoal

GOAL_ID=str(uuid4())

class GoalsRepositoryMock:
    def __init__(self) -> None:
        self.find_by_id_attributes = {}
        self.update_status_attributes = {}

    def find_by_id(self, goal_id: str) -> Goal:
        self.find_by_id_attributes["goal_id"] = goal_id
        return Goal(id="1")

    def update_status(self, goal_id: str, new_status: StatusEnum) -> None:
        self.update_status_attributes["goal_id"] = goal_id
        self.update_status_attributes["new_status"] = new_status

def test_update_status_goal():
    mock_repository = GoalsRepositoryMock()
    controller = UpdateStatusGoal(goals_repository=mock_repository)
    response = controller.update_status(goal_id=GOAL_ID, new_status=StatusEnum.COMPLETED)

    assert mock_repository.find_by_id_attributes["goal_id"] == GOAL_ID
    assert mock_repository.update_status_attributes["goal_id"] == GOAL_ID
    assert mock_repository.update_status_attributes["new_status"] == StatusEnum.COMPLETED
    assert response == {
        "data": {
            "type": "Goal",
            "count": 1,
            "message": "Update status successfully"
        }
    }
