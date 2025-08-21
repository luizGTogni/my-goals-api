from src.models.settings.sqlite_connection import sqlite_connection_handler
from src.models.repositories.users_repository import UsersRepository
from src.controllers.user.login_controller import LoginController
from src.views.user.login_view import LoginView
from src.views.interfaces.view import IView

def login_composer() -> IView:
    repository = UsersRepository(db_conn=sqlite_connection_handler)
    controller = LoginController(users_repository=repository)
    view = LoginView(login_controller=controller)
    return view
