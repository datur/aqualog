
from sqlalchemy.orm.session import Session
from src.adapters.repository.reading import SqlAlchemyReadingRepository

from src.adapters.repository.reading import AbstractReadingRespoitory
from .base import BaseAbstractUnitOfWork


class AbstractReadingUnitOfWork(BaseAbstractUnitOfWork):
    readings: AbstractReadingRespoitory


class SqlAlchemyReadingUnitOfWork(AbstractReadingUnitOfWork):
    def __init__(
        self,
        session: Session
    ):
        self.session = session
        self.readings = SqlAlchemyReadingRepository(session)

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()