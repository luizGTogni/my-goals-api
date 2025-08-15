from src.models.settings.connection import db_connection_handler
from src.models.repositories.users_repository import UsersRepository
from src.controllers.user.create_controller import CreateUserController
from src.views.user.create_view import CreateUserView
from src.views.interfaces.view import IView

def create_user_composer() -> IView:
    repository = UsersRepository(db_conn=db_connection_handler)
    controller = CreateUserController(users_repository=repository)
    view = CreateUserView(create_controller=controller)
    return view
