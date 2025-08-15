from functools import wraps
from src.middlewares import auth_handler
from .error_handler import error_handler

def protected_route(func):

    @error_handler
    @wraps(func)
    def wrapper(*args, **kwargs):
        token_info = auth_handler()
        return func(token_info=token_info, *args, **kwargs)

    return wrapper
