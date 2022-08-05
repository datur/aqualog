from email.policy import default
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID, JSON
from sqlalchemy import (Column, Float, ForeignKey, Integer, MetaData,
                        Table, String, DateTime,
                        Boolean, Enum)
from sqlalchemy.orm import relationship, registry
from src.models.reading import Reading
from src.models.tank import Tank
from src.models.user import User
from src.models.utils import WaterUnitType, WaterType

metadata = MetaData()
mapper_registry = registry()

user = Table(
    "user",
    metadata,
    Column('id', UUID(as_uuid=True), primary_key=True),
    Column('first_name', String),
    Column('last_name', String),
    Column('email', String, nullable=False),
    Column('created', DateTime, default=datetime.now()),
    Column('last_updated', DateTime, default=datetime.now()),
    Column('is_deleted', Boolean, default=False),
)

tank = Table(
    'tank',
    metadata,
    Column('id', UUID(as_uuid=True), primary_key=True),
    Column('name', String),
    Column('capacity', Float),
    Column('unit_type', Enum(WaterUnitType)),
    Column('water_type', Enum(WaterType)),
    Column('user_id', UUID(as_uuid=True), ForeignKey('user.id')),
    Column('created', DateTime),
    Column('last_updated', DateTime),
    Column('is_deleted', Boolean),
)

reading = Table(
    'reading',
    metadata,
    Column('id', UUID(as_uuid=True), primary_key=True),
    Column('tank_id', UUID(as_uuid=True), ForeignKey('tank.id')),
    Column('ph', Float, nullable=True),
    Column('temp', Float),
    Column('ammonia', Float, nullable=True, default=None),
    Column('nitrite', Float, nullable=True, default=None),
    Column('nitrate', Float, nullable=True, default=None),
    Column('gh', Integer, nullable=True, default=None),
    Column('kh', Integer, nullable=True, default=None),
    Column('specific_gravity', Float, nullable=True, default=None),
    Column('alkalinity', Integer, nullable=True, default=None),
    Column('phosphate', Float, nullable=True, default=None),
    Column('calcium', Integer, nullable=True, default=None),
    Column('magnesium', Integer, nullable=True, default=None),
    Column('iodine', Float, nullable=True, default=None),
    Column('strontium', Integer, nullable=True, default=None),
    Column('silicate', Float, nullable=True, default=None),
    Column('created', DateTime),
    Column('last_updated', DateTime),
    Column('is_deleted', Boolean),
)

inhabitant = Table(
    'inhabitant',
    metadata,
    Column('id', UUID(as_uuid=True), primary_key=True),
    Column('tank_id', UUID(as_uuid=True), ForeignKey('tank.id')),
    Column('name', String),
    Column('species', String),
    Column('max_size', Float),
    Column('preferred_parameters', JSON),
)


def start_mappers():
    mapper_registry.map_imperatively(User, user, properties={
        'tanks': relationship(Tank, backref='user', order_by=tank.c.name)
    })
    mapper_registry.map_imperatively(Tank, tank, properties={
        'readings': relationship(Reading, backref='tank', order_by=reading.c.created)
    })
    mapper_registry.map_imperatively(Reading, reading)
