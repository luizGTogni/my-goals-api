from src.views.interfaces.view import IView
from src.types.http import HttpResponse, HttpRequest
from src.controllers.interfaces.goal.update_status import IUpdateStatusGoal
from src.views.validators.update_status_goal_view_validator import update_status_goal_view_validator

class UpdateStatusGoalView(IView):
    def __init__(self, update_status_controller: IUpdateStatusGoal) -> None:
        self.__update_status_controller = update_status_controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        update_status_goal_view_validator(http_request)

        goal_id = http_request.params["goal_id"]
        new_status = http_request.body["new_status"]
        response_body = self.__update_status_controller.update_status(
            goal_id,
            new_status
        )
        return HttpResponse(status_code=200, body=response_body)
