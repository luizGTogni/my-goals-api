from functools import wraps
from flask import jsonify
from src.middlewares import error_handle

def error_handler(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e: # pylint: disable=broad-exception-caught
            http_response = error_handle(e)
            return jsonify(http_response.body), http_response.status_code

    return wrapper
