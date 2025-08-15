from src.types.http import HttpRequest, HttpResponse
from .login_view import LoginView

class LoginControllerMock:
    def __init__(self) -> None:

        self.login_attributes = {}

    def login(self, username: str, password: str) -> dict:
        self.login_attributes["username"] = username
        self.login_attributes["password"] = password
        return {
            "data": {
                "authentication": "token"
            }
        }

def test_login_view():
    mock_controller = LoginControllerMock()
    view = LoginView(login_controller=mock_controller)

    http_request = HttpRequest(
        body={
            "username": "john doe",
            "password": "123456"
        }
    )

    http_response = view.handle(http_request)

    assert mock_controller.login_attributes["username"] == http_request.body["username"]
    assert mock_controller.login_attributes["password"] == http_request.body["password"]
    assert isinstance(http_response, HttpResponse)
    assert http_response.status_code == 200
    assert "data" in http_response.body
    assert "authentication" in http_response.body["data"]
