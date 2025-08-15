from pytest import raises
from src.types.errors import HttpUnprocessableEntityError
from .create_user_view_validator import create_user_view_validator

class HttpRequestMock:
    def __init__(self, body: dict) -> None:
        self.body = body

def test_create_user_view_validator():
    http_body = HttpRequestMock({
        "name": "John Doe",
        "username": "johndoe",
        "email": "johndoe@example.com",
        "password": "123456"
    })

    create_user_view_validator(http_body)

def test_create_user_view_validator_error_without_field():
    http_body = HttpRequestMock({
        "username": "johndoe",
        "email": "johndoe@example.com",
        "password": "123456"
    })

    with raises(HttpUnprocessableEntityError):
        create_user_view_validator(http_body)

def test_create_user_view_validator_error_email_invalid():
    http_body = HttpRequestMock({
        "name": "John Doe",
        "username": "johndoe",
        "email": "johndoe",
        "password": "123456"
    })

    with raises(HttpUnprocessableEntityError):
        create_user_view_validator(http_body)

def test_create_user_view_validator_error_min_password_invalid():
    http_body = HttpRequestMock({
        "name": "John Doe",
        "username": "johndoe",
        "email": "johndoe@example.com",
        "password": "1234"
    })

    with raises(HttpUnprocessableEntityError):
        create_user_view_validator(http_body)
