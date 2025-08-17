from pydantic import BaseModel, ValidationError
from src.models.entities.goal import StatusEnum
from src.types.http import HttpRequest
from src.types.errors import HttpUnprocessableEntityError

def update_status_goal_view_validator(http_request: HttpRequest) -> None:
    class BodyData(BaseModel):
        new_status: StatusEnum

    try:
        BodyData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntityError(e.errors()) from e
