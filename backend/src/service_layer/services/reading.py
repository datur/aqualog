
from datetime import datetime
from typing import List
import uuid
from src.models.reading import ReadingUpdate

from src.models.reading import Reading
from src.service_layer.unit_of_work.reading import AbstractReadingUnitOfWork


def add_reading(tank_id: uuid.UUID, id: uuid.UUID, uow: AbstractReadingUnitOfWork, temp: float, ph: float = None, ammonia: float = None,
                nitrite: float = None, nitrate: float = None, gh: int = None, kh: int = None, specific_gravity: float = None,
                alkalinity: int = None, phosphate: float = None, calcium: int = None, magnesium: int = None, iodine: float = None,
                strontium: int = None, silicate: float = None) -> dict:

    reading = Reading(tank_id=tank_id, id=id, ph=ph, temp=temp, ammonia=ammonia,
                      nitrite=nitrite, nitrate=nitrate, gh=gh, kh=kh,
                      specific_gravity=specific_gravity, alkalinity=alkalinity,
                      phosphate=phosphate, calcium=calcium, magnesium=magnesium,
                      iodine=iodine, strontium=strontium, silicate=silicate,
                      created=datetime.now(), last_updated=datetime.now())

    with uow:
        uow.readings.add(reading)
        uow.commit()

    return dict(reading)

def read_reading(tank_id: uuid.UUID, reading_id: uuid.UUID, uow: AbstractReadingUnitOfWork) -> Reading:

    filters = {
        "tank_id": tank_id,
        "id": reading_id
    }

    with uow:
        reading = uow.readings.read(filters)

    return dict(reading) if reading is not None else None


def list_readings(tank_id: uuid.UUID, uow: AbstractReadingUnitOfWork) -> Reading:

    filters = {
        "tank_id": tank_id,
    }

    with uow:
        readings = uow.readings.list(filters)

    return dict({"readings": [dict(x) for x in readings]})

def update_reading(tank_id: uuid.UUID, reading_id: uuid.UUID, update: ReadingUpdate, uow: AbstractReadingUnitOfWork) -> dict:

    filters = {
        "id": reading_id,
        "tank_id": tank_id,
        "is_deleted": False
    }

    reading = uow.readings.read(filters)

    if reading is None:
        return None

    if not any([hasattr(reading, x) for x in update]):
        return {"Parameters not found": [x for x in update if not hasattr(reading, x)]}, 404

    with uow:
        uow.readings.update(filters, update)
        uow.commit()

        reading = uow.readings.read(filters)

    return dict(reading)

def soft_delete_readings(reading_ids: List[uuid.UUID], uow: AbstractReadingUnitOfWork) -> dict:

    with uow:
        uow.readings.soft_delete(reading_ids)
        uow.commit()

    return {"Status": "Success"}, 200


def soft_delete_reading(reading_id: uuid.UUID, uow: AbstractReadingUnitOfWork) -> dict:

    filters = {
        "id": reading_id,
        "is_deleted": False
    }

    with uow:
        reading = uow.readings.read(filters)

        if reading is None:
            return {"Status": "Reading Not Found"}, 404

        uow.readings.soft_delete(filters)
        uow.commit()

    return {"Status": "Success"}, 200

def restore_reading(tank_id: uuid.UUID, reading_id: uuid.UUID, uow: AbstractReadingUnitOfWork) -> dict:

    filters = {
        "id": reading_id,
        "tank_id": tank_id,
        "is_deleted": True
    }

    with uow:

        tank = uow.readings.read(filters)

        if tank is None:
            return {"Status": "Reading is not deleted"}, 404

        uow.readings.restore(filters)
        uow.commit()

        filters["is_deleted"] = False

        reading = uow.readings.read(filters)

    return dict(reading)

def reatore_readings_for_tank(tank_id: uuid.UUID, uow: AbstractReadingUnitOfWork):

    filters = {
        "tank_id": tank_id,
        "is_deleted": True
    }

    with uow:
        readings = uow.readings.list(filters)
        for reading in readings:
            filters["id"] = reading.id
            uow.readings.update(filters, {"is_deleted": False})
        uow.commit()


def hard_delete_reading(tank_id: uuid.UUID, reading_id: uuid.UUID, uow: AbstractReadingUnitOfWork) -> dict:

    filters = {
        "id": reading_id,
        "tank_id": tank_id
    }

    with uow:
        uow.readings.delete(filters)
        uow.commit()