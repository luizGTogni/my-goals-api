from pytest import raises
from src.types.errors import HttpAlreadyExistsError
from src.models.entities import User
from src.drivers.password_handler import PasswordHandler
from .create_controller import CreateUserController

password_handle = PasswordHandler()

class UsersRepositoryMock:
    def __init__(self) -> None:
        self.create_attributes = {}
        self.find_by_username_attributes = {}
        self.find_by_email_attributes = {}

    def create(self, name: str, username: str, email: str, password: str) -> None:
        self.create_attributes["user_info"] = (name, username, email, password)

    def find_by_username(self, username: str) -> User:
        if username == "johndoe_exists":
            return User()

        self.find_by_username_attributes["username"] = username
        return None

    def find_by_email(self, email: str) -> User:
        if email == "johndoe_exists@example.com":
            return User()

        self.find_by_email_attributes["email"] = email
        return None

def test_create_user():
    mock_repository = UsersRepositoryMock()
    controller = CreateUserController(users_repository=mock_repository)

    user_info = {
        "name": "John Doe",
        "username": "johndoe",
        "email": "johndoe@example.com",
        "password": "123456"
    }

    response = controller.create(user_info)
    password_hashed = mock_repository.create_attributes["user_info"][3]

    assert mock_repository.create_attributes["user_info"][0] == "John Doe"
    assert mock_repository.create_attributes["user_info"][1] == "johndoe"
    assert mock_repository.create_attributes["user_info"][2] == "johndoe@example.com"
    assert password_handle.check_password(user_info["password"], password_hashed) is True

    assert mock_repository.find_by_username_attributes["username"] == "johndoe"
    assert mock_repository.find_by_email_attributes["email"] == "johndoe@example.com"

    assert response == {
        "data": {
            "type": "User",
            "count": 1,
            "message": "User created successfully"
        }
    }


def test_create_user_error_if_username_already_exists():
    mock_repository = UsersRepositoryMock()
    controller = CreateUserController(users_repository=mock_repository)

    user_info = {
        "name": "John Doe",
        "username": "johndoe_exists",
        "email": "johndoe@example.com",
        "password": "123456"
    }

    with raises(HttpAlreadyExistsError):

        controller.create(user_info)
def test_create_user_error_if_email_already_exists():
    mock_repository = UsersRepositoryMock()
    controller = CreateUserController(users_repository=mock_repository)

    user_info = {
        "name": "John Doe",
        "username": "johndoe",
        "email": "johndoe_exists@example.com",
        "password": "123456"
    }

    with raises(HttpAlreadyExistsError):
        controller.create(user_info)
