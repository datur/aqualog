from sqlalchemy.orm.session import Session

from src.adapters.repository.user import AbstractUserRespoitory, SqlAlchemyUserRepository
from .base import BaseAbstractUnitOfWork

class AbstractUserUnitOfWork(BaseAbstractUnitOfWork):
    users: AbstractUserRespoitory


class SqlAlchemyUserUnitOfWork(AbstractUserUnitOfWork):
    def __init__(
        self,
        session: Session
    ):
        self.session = session
        self.users = SqlAlchemyUserRepository(session)

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
