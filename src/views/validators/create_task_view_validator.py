from pydantic import BaseModel, ValidationError, constr
from src.types.http import HttpRequest
from src.types.errors import HttpUnprocessableEntityError

def create_task_view_validator(http_request: HttpRequest) -> None:
    class BodyData(BaseModel):
        title: constr(min_length=1, max_length=150) # type: ignore
        description: constr(max_length=300) # type: ignore

    try:
        BodyData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntityError(e.errors()) from e
