from abc import ABC, abstractmethod

class ILoginController(ABC):

    @abstractmethod
    def login(self, username: str, password: str) -> dict:
        pass
