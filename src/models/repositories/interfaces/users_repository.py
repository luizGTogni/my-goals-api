from abc import ABC, abstractmethod
from src.models.entities.user import User

class IUsersRepository(ABC):

    @abstractmethod
    def create(self, name: str, username: str, email: str, password: str) -> None:
        pass

    @abstractmethod
    def find_by_id(self, user_id: str) -> User:
        pass

    @abstractmethod
    def update(self, user_id: str, data: dict) -> None:
        pass

    @abstractmethod
    def delete(self, user_id) -> None:
        pass
