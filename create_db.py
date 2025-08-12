# pylint: disable=unused-import
from src.models.settings.base import Base
from src.models.settings.connection import db_connection_handler

from src.models.entities.user import User

db_connection_handler.connect()

engine = db_connection_handler.get_engine()
Base.metadata.create_all(engine)
print("Database created")
