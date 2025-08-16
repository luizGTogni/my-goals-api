from src.views.interfaces.view import IView
from src.types.http import HttpResponse, HttpRequest
from src.controllers.interfaces.goal.create_controller import ICreateGoalController
from src.views.validators.create_goal_view_validator import create_goal_view_validator

class CreateGoalView(IView):
    def __init__(self, create_controller: ICreateGoalController) -> None:
        self.__create_controller = create_controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        create_goal_view_validator(http_request)

        title = http_request.body["title"]
        description = http_request.body["description"]
        user_id = http_request.token_info["user_id"]
        response_body = self.__create_controller.create(
            title,
            description,
            user_id,
        )
        return HttpResponse(status_code=201, body=response_body)
