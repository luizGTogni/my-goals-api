from pydantic import BaseModel, ValidationError
from src.types.http import HttpRequest
from src.types.errors import HttpUnprocessableEntityError

def login_view_validator(http_request: HttpRequest) -> None:
    class BodyData(BaseModel):
        username: str
        password: str

    try:
        BodyData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntityError(e.errors()) from e
