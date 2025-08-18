from uuid import uuid4
from src.types.http import HttpRequest, HttpResponse
from src.models.entities.task import StatusTaskEnum
from .update_status_view import UpdateStatusTaskView

class UpdateStatusTaskControllerMock:
    def __init__(self) -> None:
        self.update_status_attributes = {}

    def update_status(self, goal_id: str, task_id: str, new_status: StatusTaskEnum) -> dict:
        self.update_status_attributes["goal_id"] = goal_id
        self.update_status_attributes["task_id"] = task_id
        self.update_status_attributes["new_status"] = new_status
        return {
            "data": {
                "type": "Task",
                "count": 1,
                "message": "Update status successfully"
            }
        }

def test_create_view_test():
    mock_controller = UpdateStatusTaskControllerMock()
    view = UpdateStatusTaskView(update_status_controller=mock_controller)
    goal_id = str(uuid4)
    task_id = str(uuid4)
    http_request = HttpRequest(
        body={
            "new_status": "done",
        },
        params={
            "goal_id": goal_id,
            "task_id": task_id,
        }
    )

    http_response = view.handle(http_request)

    assert mock_controller.update_status_attributes["task_id"] == http_request.params["task_id"]
    assert mock_controller.update_status_attributes["new_status"] == http_request.body["new_status"]
    assert isinstance(http_response, HttpResponse)
    assert http_response.status_code == 200
    assert http_response.body == {
            "data": {
                "type": "Task",
                "count": 1,
                "message": "Update status successfully"
            }
        }
