from uuid import uuid4
from src.types.http import HttpRequest, HttpResponse
from .create_view import CreateGoalView

class CreateGoalControllerMock:
    def __init__(self) -> None:
        self.create_attributes = {}

    def create(self, title: str, description: str, user_id: str) -> dict:
        self.create_attributes["title"] = title
        self.create_attributes["description"] = description
        self.create_attributes["user_id"] = user_id
        return {
            "data": {
                "type": "Goal",
                "count": 1,
                "message": "Goal created successfully"
            }
        }

def test_create_view_test():
    mock_controller = CreateGoalControllerMock()
    view = CreateGoalView(create_controller=mock_controller)
    user_id = str(uuid4)
    http_request = HttpRequest(
        body={
            "title": "Title Goal",
            "description": "Description Goal",
        },
        token_info={ "user_id": user_id }
    )

    http_response = view.handle(http_request)

    assert mock_controller.create_attributes["title"] == http_request.body["title"]
    assert mock_controller.create_attributes["description"] == http_request.body["description"]
    assert mock_controller.create_attributes["user_id"] == http_request.token_info["user_id"]
    assert isinstance(http_response, HttpResponse)
    assert http_response.status_code == 201
    assert http_response.body == {
            "data": {
                "type": "Goal",
                "count": 1,
                "message": "Goal created successfully"
            }
        }
