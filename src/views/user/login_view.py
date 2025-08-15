from src.views.interfaces.view import IView
from src.controllers.interfaces.user.login_controller import ILoginController
from src.types.http import HttpResponse, HttpRequest
from src.views.validators.login_view_validator import login_view_validator

class LoginView(IView):
    def __init__(self, login_controller: ILoginController) -> None:
        self.__login_controller = login_controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        login_view_validator(http_request)

        username = http_request.body["username"]
        password = http_request.body["password"]
        response_body = self.__login_controller.login(username, password)
        return HttpResponse(status_code=200, body=response_body)
