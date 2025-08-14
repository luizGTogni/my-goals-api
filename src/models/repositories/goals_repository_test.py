from uuid import uuid4
from pytest import raises
from sqlalchemy.exc import NoResultFound
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.entities.user import User
from src.models.entities.goal import StatusEnum
from .goals_repository import GoalsRepository

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
        raise NoResultFound("Goal not found")

    def __enter__(self) -> "DBConnectionMock":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        pass

def test_create_goal():
    conn = DBConnectionMock()

    user = User(
        id=uuid4(),
        name="John Doe",
        username="johndoe",
        email="johndoe@example.com",
        password="123456",
    )

    repository = GoalsRepository(db_conn=conn)
    repository.create(
        title="Title Test",
        description="Description Test",
        owner=user
    )

    conn.session.add.assert_called_once()
    conn.session.commit.assert_called_once()
    goal_created_args = conn.session.add.call_args[0][0]

    assert goal_created_args.title == "Title Test"
    assert goal_created_args.description == "Description Test"
    assert goal_created_args.owner == user

def test_create_goal_exception():
    conn = DBConnectionExceptionMock()

    user = User(
        id=uuid4(),
        name="John Doe",
        username="johndoe",
        email="johndoe@example.com",
        password="123456",
    )

    repository = GoalsRepository(db_conn=conn)

    with raises(Exception):
        repository.create(
            title="Title Test",
            description="Description Test",
            owner=user
        )

    conn.session.add.assert_called_once()
    conn.session.commit.assert_not_called()
    conn.session.rollback.assert_called_once()

def test_find_goal_by_id():
    conn = DBConnectionMock()
    repository = GoalsRepository(db_conn=conn)
    goal_id=uuid4()
    repository.find_by_id(goal_id)

    conn.session.query.assert_called_once()
    conn.session.filter_by.assert_called_once_with(id=goal_id)
    conn.session.one.assert_called_once()

def test_find_goal_by_id_exception():
    conn = DBConnectionExceptionMock()
    repository = GoalsRepository(db_conn=conn)
    goal_id=uuid4()

    response = repository.find_by_id(goal_id)
    assert response is None

def test_update_goal():
    conn = DBConnectionMock()
    repository = GoalsRepository(db_conn=conn)
    goal_id=uuid4()
    repository.update(goal_id, title="Title", description="description")

    conn.session.query.assert_called_once()
    conn.session.filter_by.assert_called_once_with(id=goal_id)
    conn.session.update.assert_called_once_with({
        "title":"Title",
        "description":"description"
    })

def test_update_goal_exception():
    conn = DBConnectionExceptionMock()
    repository = GoalsRepository(db_conn=conn)

    with raises(Exception):
        goal_id=uuid4()
        repository.update(goal_id, title="Title", description="description")

def test_update_status_goal():
    conn = DBConnectionMock()
    repository = GoalsRepository(db_conn=conn)
    goal_id=uuid4()
    repository.update_status(goal_id, new_status=StatusEnum.COMPLETED)

    conn.session.query.assert_called_once()
    conn.session.filter_by.assert_called_once_with(id=goal_id)
    conn.session.update.assert_called_once_with({
        "status":StatusEnum.COMPLETED,
    })

def test_update_status_goal_exception():
    conn = DBConnectionExceptionMock()
    repository = GoalsRepository(db_conn=conn)

    with raises(Exception):
        goal_id=uuid4()
        repository.update_status(goal_id, new_status=StatusEnum.COMPLETED)

def test_delete_task():
    conn = DBConnectionMock()
    repository = GoalsRepository(db_conn=conn)
    goal_id=uuid4()
    repository.delete(goal_id)

    conn.session.query.assert_called_once()
    conn.session.filter_by.assert_called_once_with(id=goal_id)
    conn.session.delete.assert_called_once_with()

def test_delete_task_exception():
    conn = DBConnectionExceptionMock()
    repository = GoalsRepository(db_conn=conn)

    with raises(Exception):
        goal_id=uuid4()
        repository.delete(goal_id)
