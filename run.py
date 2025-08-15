from src.models.settings.connection import db_connection_handler
from src.main.server import app

if __name__ == "__main__":
    db_connection_handler.connect()
    app.run(host="0.0.0.0", port=3000, debug=True)
