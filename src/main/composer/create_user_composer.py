from src.models.settings.sqlite_connection import sqlite_connection_handler
from src.models.settings.redis_connection import redis_connection_handler
from src.models.repositories.users_repository import UsersRepository
from src.models.repositories.redis_repository import RedisRepository
from src.controllers.user.create_controller import CreateUserController
from src.views.user.create_view import CreateUserView
from src.views.interfaces.view import IView

def create_user_composer() -> IView:
    repository = UsersRepository(db_conn=sqlite_connection_handler)
    conn = redis_connection_handler.get_connection()
    redis_repository = RedisRepository(redis_conn=conn)
    controller = CreateUserController(
        users_repository=repository,
        redis_repository=redis_repository
    )
    view = CreateUserView(create_controller=controller)
    return view
