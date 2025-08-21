import os

class RedisInfos:
    def __init__(self):
        self.password = os.getenv("REDIS_PASSWORD")
        self.host = os.getenv("REDIS_HOST")
        self.port = os.getenv("REDIS_PORT")

redis_infos = RedisInfos()
