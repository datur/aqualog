from dataclasses import dataclass
from typing import List
import uuid

from src.models.base import Base
from src.models.reading import Reading
from src.models.utils import WaterUnitType, WaterType


@dataclass(kw_only=True)
class Tank(Base):
    user_id: uuid.UUID
    name: str
    capacity: int
    unit_type: WaterUnitType
    water_type: WaterType
    readings: List[Reading]

    def __iter__(self):
        yield 'id', self.id,
        yield 'name', self.name,
        yield 'capacity', self.capacity,
        yield 'unit_type', str(self.unit_type.name),
        yield 'water_type', str(self.water_type.name),
        yield 'readings', [dict(x) for x in self.readings if x.is_deleted != True]


@dataclass
class TankUpdate:
    name: str
    capacity: int
    unit_type: WaterUnitType
    water_type: WaterType
