from uuid import uuid4
from pytest import raises
from sqlalchemy.exc import NoResultFound
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from .users_repository import UsersRepository

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
        raise NoResultFound("User not found")

    def __enter__(self) -> "DBConnectionMock":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        pass

def test_create_user():
    conn = DBConnectionMock()
    repository = UsersRepository(db_conn=conn)
    repository.create(
        name="John Doe",
        username="johndoe",
        email="johndoe@example.com",
        password="123456"
    )

    conn.session.add.assert_called_once()
    conn.session.commit.assert_called_once()
    person_created_args = conn.session.add.call_args[0][0]

    assert person_created_args.name == "John Doe"
    assert person_created_args.username == "johndoe"
    assert person_created_args.email == "johndoe@example.com"
    assert person_created_args.password == "123456"

def test_create_user_exception():
    conn = DBConnectionExceptionMock()
    repository = UsersRepository(db_conn=conn)

    with raises(Exception):
        repository.create(
            name="John Doe",
            username="johndoe",
            email="johndoe@example.com",
            password="123456"
        )

    conn.session.add.assert_called_once()
    conn.session.commit.assert_not_called()
    conn.session.rollback.assert_called_once()

def test_find_user_by_id():
    conn = DBConnectionMock()
    repository = UsersRepository(db_conn=conn)
    user_id=uuid4()
    repository.find_by_id(user_id)

    conn.session.query.assert_called_once()
    conn.session.filter_by.assert_called_once_with(id=user_id)
    conn.session.one.assert_called_once()

def test_find_user_by_id_exception():
    conn = DBConnectionExceptionMock()
    repository = UsersRepository(db_conn=conn)
    user_id=uuid4()

    response = repository.find_by_id(user_id)
    assert response is None

def test_find_user_by_username():
    conn = DBConnectionMock()
    repository = UsersRepository(db_conn=conn)
    username="johndoe"
    repository.find_by_username(username)

    conn.session.query.assert_called_once()
    conn.session.filter_by.assert_called_once_with(username=username)
    conn.session.one.assert_called_once()

def test_find_user_by_username_exception():
    conn = DBConnectionExceptionMock()
    repository = UsersRepository(db_conn=conn)
    username="johndoe"

    response = repository.find_by_username(username)
    assert response is None

def test_update_user():
    conn = DBConnectionMock()
    repository = UsersRepository(db_conn=conn)
    user_id=uuid4()
    user_data = {
        "name":"John Doe",
        "username":"johndoe",
        "email":"johndoe@example.com",
        "password":"123456"
    }
    repository.update(user_id, data=user_data)

    conn.session.query.assert_called_once()
    conn.session.filter_by.assert_called_once_with(id=user_id)
    conn.session.update.assert_called_once_with(user_data)

def test_update_user_exception():
    conn = DBConnectionExceptionMock()
    repository = UsersRepository(db_conn=conn)

    with raises(Exception):
        user_id=uuid4()
        user_data = {
            "name":"John Doe",
            "username":"johndoe",
            "email":"johndoe@example.com",
            "password":"123456"
        }
        repository.update(user_id, user_data)

def test_delete_user():
    conn = DBConnectionMock()
    repository = UsersRepository(db_conn=conn)
    user_id=uuid4()
    repository.delete(user_id)

    conn.session.query.assert_called_once()
    conn.session.filter_by.assert_called_once_with(id=user_id)
    conn.session.delete.assert_called_once_with()

def test_delete_user_exception():
    conn = DBConnectionExceptionMock()
    repository = UsersRepository(db_conn=conn)

    with raises(Exception):
        user_id=uuid4()
        repository.delete(user_id)
