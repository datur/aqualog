import uuid
from src.service_layer.unit_of_work.user import AbstractUserUnitOfWork
from src.models.user import User, UserUpdate


def add_user(id: uuid.UUID, first_name: str, last_name: str, email: str, uow: AbstractUserUnitOfWork) -> dict:

    user = User(id=id, first_name=first_name, last_name=last_name, email=email, tanks=[])
    with uow:
        uow.users.add(user)
        uow.commit()

    return dict(user)

def read_user(id: uuid.UUID, uow: AbstractUserUnitOfWork) -> dict:
    filters = {
        "id": id
    }
    
    with uow:
        user = uow.users.read(filters)

    return dict(user) if user is not None else None

def update_user(id: uuid.UUID, update: UserUpdate, uow: AbstractUserUnitOfWork) -> dict:

    with uow:
        uow.users.update(id, dict(update))
        uow.commit()

        user = uow.users.read(id)

    return dict(user)

def soft_delete_user(id: uuid.UUID, uow: AbstractUserUnitOfWork) -> None:

    with uow:
        uow.users.soft_delete(id)
        uow.commit()

def delete_user(id: uuid.UUID, uow: AbstractUserUnitOfWork) -> None:

    with uow:
        uow.users.delete(id)
        uow.commit()
