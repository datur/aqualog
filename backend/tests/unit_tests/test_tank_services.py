from typing import List
import uuid
import pytest

from src.service_layer.unit_of_work.tank import AbstractTankUnitOfWork
from src.models.tank import Tank, TankUpdate
from src.service_layer.services import tank as tank_service
from tests.utils import FakeRepository

class FakeTankUnitOfWork(AbstractTankUnitOfWork):
    def __init__(self, items: List[Tank]):
        self.committed = False
        self.tanks = FakeRepository(items)

    def commit(self):
        self.committed = True

    def rollback(self):
        self.committed = False
