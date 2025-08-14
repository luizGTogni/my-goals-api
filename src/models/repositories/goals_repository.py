from sqlalchemy.exc import NoResultFound
from src.models.settings.connection import DBConnectionHandler
from src.models.entities.user import User
from src.models.entities.goal import Goal, StatusEnum
from .interfaces.goals_repository import IGoalsRepository

class GoalsRepository(IGoalsRepository):
    def __init__(self, db_conn: DBConnectionHandler) -> None:
        self.__db_conn = db_conn

    def create(self, title: str, description: str, owner: User) -> None:
        with self.__db_conn as db:
            try:
                goal_created = Goal(
                    title=title,
                    description=description,
                    owner=owner,
                )

                db.session.add(goal_created)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def find_by_id(self, goal_id: str) -> Goal:
        with self.__db_conn as db:
            try:
                goal = db.session.query(Goal).filter_by(id=goal_id).one()
                return goal
            except NoResultFound:
                return None

    def find_all(self) -> list[Goal]:
        with self.__db_conn as db:
            try:
                goals = db.session.query(Goal).all()
                return goals
            except NoResultFound:
                return []

    def update(self, goal_id: str, title: str, description: str) -> None:
        with self.__db_conn as db:
            try:
                db.session.query(Goal).filter_by(id=goal_id).update({
                    "title": title,
                    "description": description,
                })
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def update_status(self, goal_id: str, new_status: StatusEnum) -> None:
        with self.__db_conn as db:
            try:
                db.session.query(Goal).filter_by(id=goal_id).update({
                    "status": new_status,
                })
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, goal_id) -> None:
        with self.__db_conn as db:
            try:
                db.session.query(Goal).filter_by(id=goal_id).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
