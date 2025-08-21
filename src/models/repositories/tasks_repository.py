from sqlalchemy.orm import joinedload
from sqlalchemy.exc import NoResultFound
from src.models.settings.sqlite_connection import SqliteConnectionHandler
from src.models.entities.goal import Goal
from src.models.entities.task import Task, StatusTaskEnum
from .interfaces.tasks_repository import ITasksRepository

class TasksRepository(ITasksRepository):
    def __init__(self, db_conn: SqliteConnectionHandler) -> None:
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

    def find_all(self, goal_id: dict, filters: dict = None) -> list[Goal]:
        with self.__db_conn as db:
            try:
                query = db.session.query(Task)
                filters_accepted = ["title", "title"]
                for field, value in filters.items():
                    if field in filters_accepted:
                        column = getattr(Task, field)
                        query = query.filter(column.ilike(f"%{value}%"))

                if "status" in filters:
                    value = filters["status"]
                    if value in StatusTaskEnum:
                        query = query.filter_by(status=value)

                if not goal_id:
                    tasks = query.options(joinedload(Task.goal)).all()
                    return tasks

                tasks = (query
                            .filter_by(goal_id=goal_id)
                            .options(joinedload(Task.goal))
                            .all()
                         )
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

    def update_status(self, task_id: str, new_status: StatusTaskEnum) -> None:
        with self.__db_conn as db:
            try:
                db.session.query(Task).filter_by(id=task_id).update({
                    "status": new_status,
                })
                db.session.commit()
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
