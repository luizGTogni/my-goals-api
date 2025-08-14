from abc import ABC, abstractmethod
from src.models.entities.user import User
from src.models.entities.goal import StatusEnum, Goal

class IGoalsRepository(ABC):

    @abstractmethod
    def create(self, title: str, description: str, owner: User) -> None:
        pass

    @abstractmethod
    def find_by_id(self, goal_id: str) -> Goal:
        pass

    @abstractmethod
    def find_all(self) -> list[Goal]:
        pass

    @abstractmethod
    def update(self, goal_id: str, title: str, description: str) -> None:
        pass

    @abstractmethod
    def update_status(self, goal_id: str, new_status: StatusEnum) -> None:
        pass

    @abstractmethod
    def delete(self, goal_id) -> None:
        pass
