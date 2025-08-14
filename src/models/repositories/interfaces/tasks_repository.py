from abc import ABC, abstractmethod
from src.models.entities.goal import Goal
from src.models.entities.task import StatusEnum, Task

class ITasksRepository(ABC):

    @abstractmethod
    def create(self, title: str, description: str, goal: Goal) -> None:
        pass

    @abstractmethod
    def find_by_id(self, task_id: str) -> Task:
        pass

    @abstractmethod
    def find_all(self) -> list[Task]:
        pass

    @abstractmethod
    def update(self, task_id: str, title: str, description: str) -> None:
        pass

    @abstractmethod
    def update_status(self, task_id: str, new_status: StatusEnum) -> None:
        pass

    @abstractmethod
    def delete(self, task_id) -> None:
        pass
