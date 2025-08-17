from abc import ABC, abstractmethod

class ICreateTaskController(ABC):

    @abstractmethod
    def create(self, title: str, description: str, user_id: str, goal_id: str) -> dict:
        pass
