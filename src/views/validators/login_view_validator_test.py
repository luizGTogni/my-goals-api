from pytest import raises
from src.types.errors import HttpUnprocessableEntityError
from .login_view_validator import login_view_validator

class HttpRequestMock:
    def __init__(self, body: dict) -> None:
        self.body = body

def test_login_view_validator():
    http_body = HttpRequestMock({
        "username": "johndoe",
        "password": "123456"
    })

    login_view_validator(http_body)

def test_login_view_validator_error_without_field():
    http_body = HttpRequestMock({
        "password": "123456"
    })

    with raises(HttpUnprocessableEntityError):
        login_view_validator(http_body)
