
from dataclasses import dataclass
from typing import Any
import uuid

from src.models.base import Base

@dataclass(kw_only=True)
class Reading(Base):
    tank_id: uuid.UUID
    temp: float
    ph: float = None
    ammonia: float = None
    nitrite: float = None
    nitrate: float = None
    gh: int = None
    kh: int = None
    specific_gravity: float = None
    alkalinity: int = None
    phosphate: float = None
    calcium: int = None
    magnesium: int = None
    iodine: float = None
    strontium: int = None
    silicate: float = None

    def __iter__(self):
        yield 'id', self.id,
        if self.ph is not None: yield 'ph', self.ph,
        if self.temp is not None: yield 'temp', self.temp,
        if self.ammonia is not None: yield 'ammonia', self.ammonia,
        if self.nitrite is not None: yield 'nitrite', self.nitrite,
        if self.nitrate is not None: yield 'nitrate', self.nitrate,
        if self.gh is not None: yield 'gh', self.gh,
        if self.kh is not None: yield 'kh', self.kh,
        if self.specific_gravity is not None: yield 'specific_gravity', self.specific_gravity,
        if self.alkalinity is not None: yield 'alkalinity', self.alkalinity,
        if self.phosphate is not None: yield 'phosphate', self.phosphate,
        if self.calcium is not None: yield 'calcium', self.calcium,
        if self.magnesium is not None: yield 'magnesium', self.magnesium,
        if self.iodine is not None: yield 'iodine', self.iodine,
        if self.strontium is not None: yield 'strontium', self.strontium,
        if self.silicate is not None: yield 'silicate', self.silicate,
        yield 'created', self.created.isoformat(),
        yield 'last_updated', self.last_updated,


@dataclass
class ReadingUpdate:
    ph: float
    temp: float
    ammonia: float
    nitrite: float
    nitrate: float
    gh: int
    kh: int
    specific_gravity: float
    alkalinity: int
    phosphate: float
    calcium: int
    magnesium: int
    iodine: float
    strontium: int
    silicate: float

@dataclass
class PreferredParameter:
    parameter_name: str
    parameter_value: Any