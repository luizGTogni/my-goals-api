from uuid import uuid4
from pytest import raises
from sqlalchemy.exc import NoResultFound
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.entities.user import User
from src.models.entities.goal import Goal
from src.models.entities.task import StatusTaskEnum
from .tasks_repository import TasksRepository

class DBConnectionMock:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock()

    def __enter__(self) -> "DBConnectionMock":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        pass

class DBError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

class DBConnectionExceptionMock:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock()
        self.session.add.side_effect = self.__raise_exception
        self.session.query.side_effect = self.__raise_not_result_found

    def __raise_exception(self) -> None:
        raise DBError("Exception")

    def __raise_not_result_found(self, *args, **kwargs) -> None:
        raise NoResultFound("Task not found")

    def __enter__(self) -> "DBConnectionMock":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        pass

def test_create_task():
    conn = DBConnectionMock()

    user = User(
        id=uuid4(),
        name="John Doe",
        username="johndoe",
        email="johndoe@example.com",
        password="123456",
    )

    goal = Goal(
        title="Title Test",
        description="Description Test",
        owner=user
    )

    repository = TasksRepository(db_conn=conn)
    repository.create(
        title="Title Test",
        description="Description Test",
        goal=goal
    )

    conn.session.add.assert_called_once()
    conn.session.commit.assert_called_once()
    task_created_args = conn.session.add.call_args[0][0]

    assert task_created_args.title == "Title Test"
    assert task_created_args.description == "Description Test"
    assert task_created_args.goal == goal

def test_create_task_exception():
    conn = DBConnectionExceptionMock()

    user = User(
        id=uuid4(),
        name="John Doe",
        username="johndoe",
        email="johndoe@example.com",
        password="123456",
    )

    goal = Goal(
        title="Title Test",
        description="Description Test",
        owner=user
    )

    repository = TasksRepository(db_conn=conn)

    with raises(Exception):
        repository.create(
            title="Title Test",
            description="Description Test",
            goal=goal
        )

    conn.session.add.assert_called_once()
    conn.session.commit.assert_not_called()
    conn.session.rollback.assert_called_once()

def test_find_task_by_id():
    conn = DBConnectionMock()
    repository = TasksRepository(db_conn=conn)
    task_id=uuid4()
    repository.find_by_id(task_id)

    conn.session.query.assert_called_once()
    conn.session.filter_by.assert_called_once_with(id=task_id)
    conn.session.one.assert_called_once()

def test_find_task_by_id_exception():
    conn = DBConnectionExceptionMock()
    repository = TasksRepository(db_conn=conn)
    task_id=uuid4()

    response = repository.find_by_id(task_id)
    assert response is None

def test_update_task():
    conn = DBConnectionMock()
    repository = TasksRepository(db_conn=conn)
    task_id=uuid4()
    repository.update(task_id, title="Title", description="description")

    conn.session.query.assert_called_once()
    conn.session.filter_by.assert_called_once_with(id=task_id)
    conn.session.update.assert_called_once_with({
        "title":"Title",
        "description":"description"
    })

def test_update_task_exception():
    conn = DBConnectionExceptionMock()
    repository = TasksRepository(db_conn=conn)

    with raises(Exception):
        task_id=uuid4()
        repository.update(task_id, title="Title", description="description")

def test_update_status_task():
    conn = DBConnectionMock()
    repository = TasksRepository(db_conn=conn)
    task_id=uuid4()
    repository.update_status(task_id, new_status=StatusTaskEnum.DONE)

    conn.session.query.assert_called_once()
    conn.session.filter_by.assert_called_once_with(id=task_id)
    conn.session.update.assert_called_once_with({
        "status":StatusTaskEnum.DONE,
    })

def test_update_status_task_exception():
    conn = DBConnectionExceptionMock()
    repository = TasksRepository(db_conn=conn)

    with raises(Exception):
        task_id=uuid4()
        repository.update_status(task_id, new_status=StatusTaskEnum.DONE)

def test_delete_task():
    conn = DBConnectionMock()
    repository = TasksRepository(db_conn=conn)
    task_id=uuid4()
    repository.delete(task_id)

    conn.session.query.assert_called_once()
    conn.session.filter_by.assert_called_once_with(id=task_id)
    conn.session.delete.assert_called_once_with()

def test_delete_task_exception():
    conn = DBConnectionExceptionMock()
    repository = TasksRepository(db_conn=conn)

    with raises(Exception):
        task_id=uuid4()
        repository.delete(task_id)
