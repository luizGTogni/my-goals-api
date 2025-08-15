from flask import Flask
from flask_cors import CORS

from src.main.routes.users_routes import users_routes_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(users_routes_bp)
