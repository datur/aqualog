from dataclasses import dataclass
import uuid
from src.models.base import Base
from src.models.reading import PreferredParameter
from src.models.utils import PlantSizeType


@dataclass(kw_only=True)
class Inhabitant(Base):
    tank_id: uuid.UUID
    name: str
    species: str
    max_size: float
    preferred_parameters: list[PreferredParameter]


@dataclass(kw_only=True)
class Plant(Base):
    tank_id: uuid.UUID
    name: str
    species: str
    max_height: float
    size_type: PlantSizeType
    preferred_parameters: list[PreferredParameter]
