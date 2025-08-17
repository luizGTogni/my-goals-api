from uuid import uuid4
from src.models.entities import Goal
from .list_all_controller import ListAllController

class GoalsRepositoryMock:
    def __init__(self) -> None:
        self.find_all_attributes = {}

    def find_all(self, user_id: str = None, filters: dict = None) -> list[Goal]:
        self.find_all_attributes["user_id"] = user_id
        self.find_all_attributes["filters"] = filters
        return [Goal(id="1"), Goal(id="2")]

def test_list_all_controler():
    mock_repository = GoalsRepositoryMock()
    controller = ListAllController(goals_repository=mock_repository)
    user_id = str(uuid4())
    response = controller.list_all(user_id=user_id)

    assert mock_repository.find_all_attributes["user_id"] == user_id
    assert mock_repository.find_all_attributes["filters"] is None
    assert response["data"]["count"] == 2
