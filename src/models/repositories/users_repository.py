from sqlalchemy.exc import NoResultFound
from src.models.settings.connection import DBConnectionHandler
from src.models.entities.user import User
from .interfaces.users_repository import IUsersRepository

class UsersRepository(IUsersRepository):
    def __init__(self, db_conn: DBConnectionHandler) -> None:
        self.__db_conn = db_conn

    def create(self, name: str, username: str, email: str, password: str) -> None:
        with self.__db_conn as db:
            try:
                user_created = User(
                    name=name,
                    username=username,
                    email=email,
                    password=password,
                )

                db.session.add(user_created)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def find_by_id(self, user_id: str) -> User:
        with self.__db_conn as db:
            try:
                user = db.session.query(User).filter_by(id=user_id).one()
                return user
            except NoResultFound:
                return None

    def update(self, user_id: str, data: dict) -> None:
        with self.__db_conn as db:
            try:
                db.session.query(User).filter_by(id=user_id).update(data)
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, user_id) -> None:
        with self.__db_conn as db:
            try:
                db.session.query(User).filter_by(id=user_id).delete()
            except Exception as exception:
                db.session.rollback()
                raise exception
