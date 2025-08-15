from pytest import raises
from src.models.entities import User
from src.drivers.password_handler import PasswordHandler
from src.types.errors import HttpUnauthorizedError
from .login_controller import LoginController

password_handle = PasswordHandler()

class UsersRepositoryMock:
    def __init__(self) -> None:
        self.find_by_username_attributes = {}

    def find_by_username(self, username: str) -> User:
        if username == "john_not_found":
            return None

        self.find_by_username_attributes["username"] = username
        return User(
            username="johndoe",
            password=password_handle.encrypt_password("123456")
        )

def test_login():
    mock_repository = UsersRepositoryMock()
    controller = LoginController(users_repository=mock_repository)

    username = "johndoe"
    password = "123456"
    response = controller.login(username, password)

    assert mock_repository.find_by_username_attributes["username"] == username
    assert "data" in response
    assert "authentication" in response["data"]

def test_login_error_user_not_found():
    mock_repository = UsersRepositoryMock()
    controller = LoginController(users_repository=mock_repository)

    username = "john_not_found"
    password = "123456"

    with raises(HttpUnauthorizedError):
        controller.login(username, password)

def test_login_error_password_invalid():
    mock_repository = UsersRepositoryMock()
    controller = LoginController(users_repository=mock_repository)

    username = "johndoe"
    password = "password_wrong"

    with raises(HttpUnauthorizedError):
        controller.login(username, password)
