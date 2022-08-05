from datetime import datetime
from typing import Any
import uuid
from src.models.base import Base
from dataclasses import dataclass

from src.models.utils import DoseUnits


@dataclass(kw_only=True)
class SupplementalDose(Base):
    tank_id: uuid.UUID
    name: str
    amount: Any
    amount_unit: DoseUnits


@dataclass(kw_only=True)
class SupplementalDoseSchedule(Base):
    tank_id: uuid.UUID
    name: str
    amount: Any
    amount_unit: DoseUnits
    repeat_until: datetime
    repeat_interval: int
