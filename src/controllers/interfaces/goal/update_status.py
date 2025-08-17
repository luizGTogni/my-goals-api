from abc import ABC, abstractmethod
from src.models.entities.goal import StatusEnum

class IUpdateStatusGoal(ABC):

    @abstractmethod
    def update_status(self, goal_id: str, new_status: StatusEnum) -> dict:
        pass
