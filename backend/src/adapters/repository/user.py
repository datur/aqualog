import abc
import uuid
from sqlalchemy.orm.session import Session
from src.models.user import User, UserUpdate


class AbstractUserRespoitory(abc.ABC):
    @abc.abstractclassmethod
    def add(self, user: User):
        raise NotImplementedError

    @abc.abstractclassmethod
    def read(self, uid) -> User:
        raise NotImplementedError

    @abc.abstractclassmethod
    def delete(self, user: User) -> User:
        raise NotImplementedError

class SqlAlchemyUserRepository(AbstractUserRespoitory):
    def __init__(self, session: Session):
        self.session = session

    def add(self, user: User):
        return self.session.add(user)

    def read(self, filters: dict):
        return self.session.query(User).filter_by(**filters).first()

    def update(self, uid: uuid.UUID, update: UserUpdate):
        stored_user = self.read(uid)
        stored_user.update(update)
        return stored_user

    def soft_delete(self, uid: uuid.UUID):
        _ = self.update(uid, {"is_deleted":True})

    def restore(self, uid: uuid.UUID):
        _ = self.update(uid, {"is_deleted":False})

    def delete(self, uid: uuid.UUID):
        stored_user = self.read(uid)
        self.session.delete(stored_user)
