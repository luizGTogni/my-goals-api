from .http_error import HttpError

class HttpBadRequestError(HttpError):
    def __init__(self, message: str) -> None:
        super().__init__(
            status_code=400,
            name="BadRequest",
            message=message
        )
