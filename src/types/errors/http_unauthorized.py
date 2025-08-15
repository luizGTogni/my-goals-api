from .http_error import HttpError

class HttpUnauthorizedError(HttpError):
    def __init__(self, message: str) -> None:
        super().__init__(
            status_code=401,
            name="Unauthorized",
            message=message
        )
