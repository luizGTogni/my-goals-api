from uuid import uuid4
from .jwt_handler import JwtHandler

def test_jwt_handler():
    handle = JwtHandler()
    user_id = uuid4()
    payload_body = { "user_id": user_id.hex }
    token = handle.generate_token(body=payload_body)
    token_info = handle.check_token(token)

    assert token_info["user_id"] == user_id.hex
    assert isinstance(token_info["exp"], int)
