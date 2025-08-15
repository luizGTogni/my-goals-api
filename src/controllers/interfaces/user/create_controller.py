from abc import ABC, abstractmethod

class ICreateUserController(ABC):

    @abstractmethod
    def create(self, user_info: dict) -> dict:
        pass
