from uuid import uuid4
from src.types.http import HttpRequest, HttpResponse
from .list_all_view import ListAllView

GOAL_ID = str(uuid4())

class ListAllControllerMock:
    def __init__(self) -> None:
        self.list_all_attributes = {}

    def list_all(self, goal_id: str, filters: dict = None) -> dict:
        self.list_all_attributes["goal_id"] = goal_id
        self.list_all_attributes["filters"] = filters

def test_list_all_task():
    mock_controller = ListAllControllerMock()
    view = ListAllView(list_all_controller=mock_controller)
    http_request = HttpRequest(token_info={ "goal_id": GOAL_ID })
    http_response = view.handle(http_request)

    assert mock_controller.list_all_attributes["goal_id"] == GOAL_ID
    assert mock_controller.list_all_attributes["filters"] is None
    assert isinstance(http_response, HttpResponse)
