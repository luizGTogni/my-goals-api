# pylint: disable=unused-import
from src.models.settings.base import Base
from src.models.settings.sqlite_connection import sqlite_connection_handler

from src.models.entities import User, Goal, Task

sqlite_connection_handler.connect()

engine = sqlite_connection_handler.get_engine()
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
print("Database created")
