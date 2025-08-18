from pydantic import BaseModel, ValidationError
from src.models.entities.task import StatusTaskEnum
from src.types.http import HttpRequest
from src.types.errors import HttpUnprocessableEntityError

def update_status_task_view_validator(http_request: HttpRequest) -> None:
    class BodyData(BaseModel):
        new_status: StatusTaskEnum

    try:
        BodyData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntityError(e.errors()) from e
