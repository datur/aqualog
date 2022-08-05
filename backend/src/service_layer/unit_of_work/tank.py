
from sqlalchemy.orm.session import Session

from src.adapters.repository.tank import AbstractTankRespoitory, SqlAlchemyTankRepository
from .base import BaseAbstractUnitOfWork


class AbstractTankUnitOfWork(BaseAbstractUnitOfWork):
    tanks: AbstractTankRespoitory


class SqlAlchemyTankUnitOfWork(AbstractTankUnitOfWork):
    def __init__(
        self,
        session: Session
    ):
        self.session = session
        self.tanks = SqlAlchemyTankRepository(session)

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()