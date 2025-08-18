from src.views.interfaces.view import IView
from src.types.http import HttpResponse, HttpRequest
from src.controllers.interfaces.task.update_status import IUpdateStatusTask
from src.views.validators.update_status_task_view_validator import update_status_task_view_validator

class UpdateStatusTaskView(IView):
    def __init__(self, update_status_controller: IUpdateStatusTask) -> None:
        self.__update_status_controller = update_status_controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        update_status_task_view_validator(http_request)

        goal_id = http_request.params["goal_id"]
        task_id = http_request.params["task_id"]
        new_status = http_request.body["new_status"]
        response_body = self.__update_status_controller.update_status(
            goal_id,
            task_id,
            new_status
        )
        return HttpResponse(status_code=200, body=response_body)
