from src.types.http import HttpResponse
from src.types.errors import HttpError

def error_handle(error: Exception) -> HttpResponse:
    if isinstance(error, HttpError):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "title": error.name,
                "detail": error.message
            },
        )

    return HttpResponse(
        status_code=500,
            body={
                "title": "Server error",
                "detail": str(error)
            },
    )
