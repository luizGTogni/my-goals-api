from pytest import raises
from src.types.errors import HttpUnprocessableEntityError
from .create_goal_view_validator import create_goal_view_validator

class HttpRequestMock:
    def __init__(self, body: dict) -> None:
        self.body = body

def test_create_goal_view_validator():
    http_body = HttpRequestMock({
        "title": "Title Goal",
        "description": "Description Goal",
    })

    create_goal_view_validator(http_body)

def test_create_goal_view_validator_error_without_field():
    http_body = HttpRequestMock({
        "title": "Title Goal",
    })

    with raises(HttpUnprocessableEntityError):
        create_goal_view_validator(http_body)
