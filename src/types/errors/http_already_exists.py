from .http_error import HttpError

class HttpAlreadyExistsError(HttpError):
    def __init__(self, message: str) -> None:
        super().__init__(
            status_code=409,
            name="AlreadyExists",
            message=message
        )
