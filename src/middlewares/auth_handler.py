from flask import request
from src.drivers.jwt_handler import JwtHandler
from src.types.errors import HttpUnauthorizedError, HttpBadRequestError

def auth_handler():
    jwt_handle = JwtHandler()
    raw_token = request.headers.get("Authorization")
    user_id = request.headers.get("uid")

    if not raw_token or not user_id:
        raise HttpBadRequestError("Invalid auth informations")

    token = raw_token.split()[1]
    token_info = jwt_handle.check_token(token)
    token_uid = token_info["user_id"]

    if token_uid and user_id and (token_uid == user_id):
        return token_info

    raise HttpUnauthorizedError("User Unauthorized")
