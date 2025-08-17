# pylint: disable=unused-import
from src.models.settings.base import Base
from src.models.settings.connection import db_connection_handler

from src.models.entities import User, Goal, Task

db_connection_handler.connect()

engine = db_connection_handler.get_engine()
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
print("Database created")
