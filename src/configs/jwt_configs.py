import os

class JwtInfos:
    def __init__(self):
        self.secret_key = os.getenv("JWT_SECRET_KEY")
        self.algorithm = os.getenv("JWT_ALGORITHM")

jwt_infos = JwtInfos()
