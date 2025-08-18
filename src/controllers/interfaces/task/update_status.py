from abc import ABC, abstractmethod
from src.models.entities.task import StatusTaskEnum

class IUpdateStatusTask(ABC):

    @abstractmethod
    def update_status(
        self,
        goal_id: str,
        task_id: str,
        new_status: StatusTaskEnum
    ) -> dict:
        pass
