from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker
from src.configs.db_configs import db_infos, DBInfos

class DBConnectionHandler:
    def __init__(self, db: DBInfos) -> None:
        self.__connection_string = (
            f"postgresql+psycopg2://{db.user}:{db.password}@{db.host}:{db.port}/{db.database}"
        )
        self.__engine = None
        self.session = None

    def connect(self) -> None:
        self.__engine = create_engine(self.__connection_string)

    def get_engine(self) -> Engine:
        return self.__engine

    def __enter__(self) -> "DBConnectionHandler":
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.session.close()

db_connection_handler = DBConnectionHandler(db_infos)
