import abc
import uuid
from sqlalchemy.orm.session import Session
from src.models.tank import Tank, TankUpdate


class AbstractTankRespoitory(abc.ABC):
    @abc.abstractclassmethod
    def add(self, tank: Tank):
        raise NotImplementedError

    @abc.abstractclassmethod
    def read(self, uid) -> Tank:
        raise NotImplementedError

    @abc.abstractclassmethod
    def list(self, uid) -> Tank:
        raise NotImplementedError

    @abc.abstractclassmethod
    def update(self, uid) -> Tank:
        raise NotImplementedError

    @abc.abstractclassmethod
    def soft_delete(self, uid) -> Tank:
        raise NotImplementedError

    @abc.abstractclassmethod
    def restore(self, uid) -> Tank:
        raise NotImplementedError

    @abc.abstractclassmethod
    def delete(self, tank: Tank) -> Tank:
        raise NotImplementedError

class SqlAlchemyTankRepository(AbstractTankRespoitory):
    def __init__(self, session: Session):
        self.session = session

    def add(self, tank: Tank):
        return self.session.add(tank)

    def read(self, filters: dict):
        return self.session.query(Tank).filter_by(**filters).first()

    def list(self, filters: dict):
        return self.session.query(Tank).filter_by(**filters)

    def update(self, filters: dict, update: TankUpdate):
        stored_tank = self.read(filters)
        stored_tank.update(update)

    def soft_delete(self, filters: dict):
        stored_tank = self.read(filters)
        stored_tank.update({"is_deleted": True})

    def delete(self, filters: dict):
        stored_tank = self.read(filters)
        self.session.delete(stored_tank)

    def restore(self, filters: dict):
        stored_tank = self.read(filters)
        stored_tank.update({"is_deleted": False})