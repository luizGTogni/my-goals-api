from datetime import datetime, timedelta, timezone
import jwt
from src.configs.jwt_configs import jwt_infos

class JwtHandler:
    def generate_token(self, body: dict = None) -> str:
        token = jwt.encode(
            payload={
                "exp": datetime.now(timezone.utc) + timedelta(hours=24),
                **body
            },
            key=jwt_infos.secret_key,
            algorithm=jwt_infos.algorithm
        )

        return token

    def check_token(self, token: str) -> dict:
        token_info = jwt.decode(
            token,
            key=jwt_infos.secret_key,
            algorithms=jwt_infos.algorithm
        )

        return token_info
