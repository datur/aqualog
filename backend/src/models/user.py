from dataclasses import dataclass
from datetime import datetime
from typing import List
from src.models.tank import Tank
from src.models.base import Base

@dataclass(kw_only=True)
class User(Base):
    first_name: str
    last_name: str
    email: str
    tanks: List[Tank]

    def __iter__(self):
        yield 'id',  self.id,
        yield 'first_name', self.first_name
        yield 'last_name', self.last_name
        yield 'email', self.email
        yield 'tanks', [dict(x) for x in self.tanks]
        yield 'created', self.created
        yield 'last_updated', self.last_updated

@dataclass
class UserUpdate:
    first_name: str = None
    last_name: str = None
    email: str = None
    last_updated: datetime = datetime.now()

    def __iter__(self):
        if self.first_name is not None: yield 'first_name', self.first_name,
        if self.last_name is not None: yield 'last_name', self.last_name,
        if self.email is not None: yield 'last_name', self.email,
        if not all(v is None for v in [self.first_name, self.last_name, self.email]): yield 'last_updated', self.last_updated