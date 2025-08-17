from uuid import uuid4
from pytest import raises
from src.types.errors import HttpUnprocessableEntityError
from .create_task_view_validator import create_task_view_validator

class HttpRequestMock:
    def __init__(self, body: dict) -> None:
        self.body = body

def test_create_task_view_validator():
    http_body = HttpRequestMock({
        "title": "Title Task",
        "description": "Description Task",
        "goal_id": str(uuid4())
    })

    create_task_view_validator(http_body)

def test_create_task_view_validator_error_without_field():
    http_body = HttpRequestMock({
        "title": "Title Task",
    })

    with raises(HttpUnprocessableEntityError):
        create_task_view_validator(http_body)
