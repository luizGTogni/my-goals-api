from src.models.settings.sqlite_connection import sqlite_connection_handler
from src.models.settings.redis_connection import redis_connection_handler
from src.main.server import app

if __name__ == "__main__":
    sqlite_connection_handler.connect()
    redis_connection_handler.connect()
    app.run(host="0.0.0.0", port=3000, debug=True)
