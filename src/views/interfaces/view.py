from abc import ABC, abstractmethod
from src.types.http import HttpResponse, HttpRequest

class IView(ABC):

    @abstractmethod
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pass
