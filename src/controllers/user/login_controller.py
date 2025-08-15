from src.controllers.interfaces.user.create_controller import ICreateUserController
from src.drivers.password_handler import PasswordHandler
from src.models.entities import User
from src.models.repositories.users_repository import UsersRepository
from src.types.errors import HttpUnauthorizedError
from src.drivers.jwt_handler import JwtHandler

class LoginController(ICreateUserController):
    def __init__(self, users_repository: UsersRepository) -> None:
        self.__users_repository = users_repository
        self.__password_handle = PasswordHandler()
        self.__jwt_handle = JwtHandler()

    def login(self, username: str, password: str) -> dict:
        user = self.__verify_if_user_exists(username)
        self.__verify_password_combine(password_plain=password, password_hashed=user.password)
        token = self.__generate_token(str(user.id))

        return self.__format_response(token)

    def __verify_if_user_exists(self, username: str) -> User:
        user = self.__users_repository.find_by_username(username)

        if not user:
            raise HttpUnauthorizedError("Username or Password invalid")

        return user

    def __verify_password_combine(self, password_plain: str, password_hashed: str) -> None:
        is_combine = self.__password_handle.check_password(password_plain, password_hashed)

        if not is_combine:
            raise HttpUnauthorizedError("Username or Password invalid")

    def __generate_token(self, user_id: str) -> None:
        token = self.__jwt_handle.generate_token(body={ "user_id": user_id })
        return token

    def __format_response(self, token: str) -> dict:
        return {
            "data": {
                "authentication": token
            }
        }
