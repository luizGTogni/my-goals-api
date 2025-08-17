from abc import ABC, abstractmethod

class IListAllController(ABC):

    @abstractmethod
    def list_all(self, user_id: str, filters: dict = None) -> dict:
        pass
