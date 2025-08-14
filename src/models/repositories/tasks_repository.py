from sqlalchemy.exc import NoResultFound
from src.models.settings.connection import DBConnectionHandler
from src.models.entities.goal import Goal
from src.models.entities.task import Task, StatusEnum
from .interfaces.tasks_repository import ITasksRepository

class TasksRepository(ITasksRepository):
    def __init__(self, db_conn: DBConnectionHandler) -> None:
        self.__db_conn = db_conn

    def create(self, title: str, description: str, goal: Goal) -> None:
        with self.__db_conn as db:
            try:
                task_created = Task(
                    title=title,
                    description=description,
                    goal=goal,
                )

                db.session.add(task_created)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def find_by_id(self, task_id: str) -> Task:
        with self.__db_conn as db:
            try:
                task = db.session.query(Task).filter_by(id=task_id).one()
                return task
            except NoResultFound:
                return None

    def find_all(self) -> list[Goal]:
        with self.__db_conn as db:
            try:
                tasks = db.session.query(Task).all()
                return tasks
            except NoResultFound:
                return []

    def update(self, task_id: str, title: str, description: str) -> None:
        with self.__db_conn as db:
            try:
                db.session.query(Task).filter_by(id=task_id).update({
                    "title": title,
                    "description": description,
                })
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def update_status(self, task_id: str, new_status: StatusEnum) -> None:
        with self.__db_conn as db:
            try:
                db.session.query(Task).filter_by(id=task_id).update({
                    "status": new_status,
                })
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, task_id) -> None:
        with self.__db_conn as db:
            try:
                db.session.query(Task).filter_by(id=task_id).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
