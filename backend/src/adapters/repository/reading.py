import abc
from typing import List
import uuid
from sqlalchemy.orm.session import Session
from src.models.reading import Reading, ReadingUpdate


class AbstractReadingRespoitory(abc.ABC):
    @abc.abstractclassmethod
    def add(self, reading: Reading):
        raise NotImplementedError

    @abc.abstractclassmethod
    def read(self, uid) -> Reading:
        raise NotImplementedError

    @abc.abstractclassmethod
    def list(self, uid) -> Reading:
        raise NotImplementedError

    @abc.abstractclassmethod
    def update(self, uid) -> Reading:
        raise NotImplementedError

    @abc.abstractclassmethod
    def soft_delete(self, uid) -> Reading:
        raise NotImplementedError

    @abc.abstractclassmethod
    def restore(self, uid) -> Reading:
        raise NotImplementedError

    @abc.abstractclassmethod
    def delete(self, tank: Reading) -> Reading:
        raise NotImplementedError

class SqlAlchemyReadingRepository(AbstractReadingRespoitory):
    def __init__(self, session: Session):
        self.session = session

    def add(self, reading: Reading):
        return self.session.add(reading)

    def read(self, filters: dict):
        return self.session.query(Reading).filter_by(**filters).first()
    
    def read_multiple(self, ids: List):
        return self.session.query(Reading).filter(Reading.id.in_(ids)).all()

    def list(self, filters: dict):
        return self.session.query(Reading).filter_by(**filters)

    def update(self, filters: dict, update: ReadingUpdate):
        stored_reading = self.read(filters)
        stored_reading.update(update)

    def soft_delete(self, ids: List):
        stored_readings = self.read_multiple(ids)
        [sr.update({"is_deleted": True}) for sr in stored_readings if sr is not None]

    def delete(self, filters: dict):
        stored_reading = self.read(filters)
        self.session.delete(stored_reading)

    def restore(self, filters: dict):
        stored_reading = self.read(filters)
        stored_reading.update({"is_deleted": False})