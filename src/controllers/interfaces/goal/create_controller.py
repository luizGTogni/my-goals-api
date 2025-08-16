from abc import ABC, abstractmethod

class ICreateGoalController(ABC):

    @abstractmethod
    def create(self, title: str, description: str, user_id: str) -> dict:
        pass
