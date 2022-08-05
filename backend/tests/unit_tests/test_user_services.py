from typing import List
import uuid
import pytest

from src.service_layer.unit_of_work.user import AbstractUserUnitOfWork
from src.models.user import User, UserUpdate
from src.service_layer.services import user as user_service
from tests.utils import FakeRepository

class FakeUserUnitOfWork(AbstractUserUnitOfWork):
    def __init__(self, items: List[User]):
        self.committed = False
        self.users = FakeRepository(items)

    def commit(self):
        self.committed = True

    def rollback(self):
        self.committed = False

def test_add_user_no_existing_user():
    users = []

    uow = FakeUserUnitOfWork(users)

    _ = user_service.add_user("uid", "first_name", "last_name", "test@example.com", uow)

    assert len(uow.users.items) == 1

def test_add_user_user_already_exists():
    user = User(
        id=uuid.uuid4(),
        first_name="Name",
        last_name="Surname",
        email="Email",
        tanks=[]
    )

    users = [user]

    uow = FakeUserUnitOfWork(users)

    _ = user_service.add_user(uow=uow, id=uuid.uuid4(), first_name="Name", last_name="Surname", email="Email")

    assert len(uow.users.items) == 1


def test_read_user():

    user_id = "identity"

    user = User(
        id=user_id,
        first_name="Name",
        last_name="Surname",
        email="Email",
        tanks=[]
    )

    users = [user]

    uow = FakeUserUnitOfWork(users)

    result = user_service.read_user(user_id, uow)

    assert dict(user) == result

def test_read_user_not_exist():
    users = []

    user_id = "id"

    uow = FakeUserUnitOfWork(users)

    result = user_service.read_user(user_id, uow)

    assert {} == result

def test_update_user():

    user_id = "identity"

    user = User(
        id=user_id,
        first_name="Name",
        last_name="Surname",
        email="Email",
        tanks=[]
    )

    users = [user]

    uow = FakeUserUnitOfWork(users)

    update = UserUpdate(first_name="New Name")

    result = user_service.update_user(user_id, update, uow)

    assert result['first_name'] == update.first_name

def test_update_user_no_update():

    user_id = "identity"

    user = User(
        id=user_id,
        first_name="Name",
        last_name="Surname",
        email="Email",
        tanks=[]
    )

    users = [user]

    uow = FakeUserUnitOfWork(users)

    update = UserUpdate()

    result = user_service.update_user(user_id, update, uow)

    assert result['last_updated'] == user.last_updated


def test_delete_user():
    user_id = "identity"

    user = User(
        id=user_id,
        first_name="Name",
        last_name="Surname",
        email="Email",
        tanks=[]
    )

    users = [user]

    uow = FakeUserUnitOfWork(users)

    user_service.delete_user(user_id, uow)

    assert len(uow.users.items) == 0
