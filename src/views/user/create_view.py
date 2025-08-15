from src.views.interfaces.view import IView
from src.types.http import HttpResponse, HttpRequest
from src.controllers.interfaces.user.create_controller import ICreateUserController
from src.views.validators.create_user_view_validator import create_user_view_validator

class CreateUserView(IView):
    def __init__(self, create_controller: ICreateUserController) -> None:
        self.__create_controller = create_controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        create_user_view_validator(http_request)

        body = http_request.body
        response_body = self.__create_controller.create(user_info=body)
        return HttpResponse(status_code=201, body=response_body)
