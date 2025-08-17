from src.views.interfaces.view import IView
from src.controllers.interfaces.task.list_all_controller import IListAllController
from src.types.http import HttpRequest, HttpResponse

class ListAllView(IView):
    def __init__(self, list_all_controller: IListAllController) -> None:
        self.__list_all_controller = list_all_controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        user_id = http_request.token_info["user_id"]
        goal_id = http_request.params["goal_id"]
        filters = http_request.query
        response_body = self.__list_all_controller.list_all(user_id, goal_id, filters)
        return HttpResponse(status_code=200, body=response_body)
