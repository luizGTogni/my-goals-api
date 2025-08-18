from pytest import raises
from src.types.errors import HttpUnprocessableEntityError
from .update_status_task_view_validator import update_status_task_view_validator

class HttpRequestMock:
    def __init__(self, body: dict) -> None:
        self.body = body

def test_update_status_task_view_validator():
    http_body = HttpRequestMock({
        "new_status": "done",
    })

    update_status_task_view_validator(http_body)

def test_update_status_task_view_validator_error_enum():
    http_body = HttpRequestMock({
        "new_status": "status_wrong",
    })

    with raises(HttpUnprocessableEntityError):
        update_status_task_view_validator(http_body)

def test_update_status_task_view_validator_error_without_field():
    http_body = HttpRequestMock({})

    with raises(HttpUnprocessableEntityError):
        update_status_task_view_validator(http_body)
