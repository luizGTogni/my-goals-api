from src.types.http import HttpRequest, HttpResponse
from .create_view import CreateUserView

class CreateUserControllerMock:
    def __init__(self) -> None:
        self.create_attributes = {}

    def create(self, user_info: dict) -> dict:
        self.create_attributes["user_info"] = user_info
        return {
            "data": {
                "type": "User",
                "count": 1,
                "message": "User created successfully"
            }
        }

def test_create_view_test():
    mock_controller = CreateUserControllerMock()
    view = CreateUserView(create_controller=mock_controller)

    http_request = HttpRequest(
        body={
            "name": "John Doe",
            "username": "johndoe",
            "email": "johndoe@example.com",
            "password": "123456"
        }
    )

    http_response = view.handle(http_request)

    assert mock_controller.create_attributes["user_info"] == http_request.body
    assert isinstance(http_response, HttpResponse)
    assert http_response.status_code == 201
    assert http_response.body == {
            "data": {
                "type": "User",
                "count": 1,
                "message": "User created successfully"
            }
        }
