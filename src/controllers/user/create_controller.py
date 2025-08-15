from src.controllers.interfaces.user.create_controller import ICreateUserController
from src.models.repositories.interfaces.users_repository import IUsersRepository
from src.types.errors import HttpAlreadyExistsError
from src.drivers.password_handler import PasswordHandler

class CreateUserController(ICreateUserController):
    def __init__(self, users_repository: IUsersRepository) -> None:
        self.__users_repository = users_repository
        self.__password_handle = PasswordHandler()

    def create(self, user_info: dict) -> dict:
        name = user_info["name"]
        username = user_info["username"]
        email = user_info["email"]
        password = user_info["password"]

        self.__validate_if_username_already_exists(username)
        self.__validate_if_email_already_exists(email)
        password_hashed = self.__encrypt_password(password)
        self.__insert_in_db(name, username, email, password_hashed)

        return self.__format_response()

    def __validate_if_username_already_exists(self, username: str) -> None:
        user = self.__users_repository.find_by_username(username)

        if user:
            raise HttpAlreadyExistsError("User already exists")

    def __validate_if_email_already_exists(self, email: str) -> None:
        user = self.__users_repository.find_by_email(email)

        if user:
            raise HttpAlreadyExistsError("User already exists")

    def __encrypt_password(self, password_plain: str) -> str:
        password_hashed = self.__password_handle.encrypt_password(password_plain)
        return password_hashed

    def __insert_in_db(self, name: str, username: str, email: str, password_hashed: str) -> None:
        self.__users_repository.create(name, username, email, password_hashed)


    def __format_response(self) -> dict:
        return {
            "data": {
                "type": "User",
                "count": 1,
                "message": "User created successfully"
            }
        }
