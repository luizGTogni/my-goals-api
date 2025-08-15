from pydantic import BaseModel, ValidationError, constr, EmailStr
from src.types.http import HttpRequest
from src.types.errors import HttpUnprocessableEntityError

def create_user_view_validator(http_request: HttpRequest) -> None:
    class BodyData(BaseModel):
        name: constr(max_length=150) # type: ignore
        username: constr(min_length=3, max_length=100) # type: ignore
        email: EmailStr
        password: constr(min_length=5) # type: ignore

    try:
        BodyData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntityError(e.errors()) from e
