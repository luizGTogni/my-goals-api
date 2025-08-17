from src.views.interfaces.view import IView
from src.types.http import HttpResponse, HttpRequest
from src.controllers.interfaces.task.create_controller import ICreateTaskController
from src.views.validators.create_task_view_validator import create_task_view_validator

class CreateTaskView(IView):
    def __init__(self, create_controller: ICreateTaskController) -> None:
        self.__create_controller = create_controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        create_task_view_validator(http_request)

        title = http_request.body["title"]
        description = http_request.body["description"]
        goal_id = http_request.params["goal_id"]
        user_id = http_request.token_info["user_id"]
        response_body = self.__create_controller.create(
            title,
            description,
            user_id,
            goal_id,
        )
        return HttpResponse(status_code=201, body=response_body)
