from redis import Redis
from src.configs.redis_configs import redis_infos

class RedisConnectionHandler:
    def __init__(self) -> None:
        self.__conn = None

    def connect(self) -> Redis:
        self.__conn = Redis(
            host=redis_infos.host,
            port=redis_infos.port,
            password=redis_infos.password,
            db=0,
        )
        return self.__conn

    def get_connection(self) -> Redis:
        return self.__conn

redis_connection_handler = RedisConnectionHandler()
