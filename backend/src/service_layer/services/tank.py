from datetime import datetime
from typing import List
import uuid
from src.models.utils import WaterUnitType, WaterType
from src.service_layer.unit_of_work.tank import AbstractTankUnitOfWork

from src.models.tank import Tank


def add_tank(user_id: uuid.UUID, id: uuid.UUID, name: str, capacity: int, unit_type: int, water_type: int, uow: AbstractTankUnitOfWork) -> dict:

    water_type = WaterType(int(water_type)).name
    unit_type = WaterUnitType(int(unit_type)).name

    tank = Tank(id=id, user_id=user_id, name=name, capacity=capacity, unit_type=unit_type,
                water_type=water_type, created=datetime.now(), last_updated=datetime.now(), readings=[])

    print(tank)

    with uow:
        uow.tanks.add(tank)
        uow.commit()

    return dict(tank)


def read_tank(tank_id: uuid.UUID, user_id: uuid.UUID, uow: AbstractTankUnitOfWork) -> dict:

    filters = {
        "id": tank_id,
        "user_id": user_id,
        "is_deleted": False
    }

    with uow:
        tank = uow.tanks.read(filters)

    return dict(tank) if tank is not None else None


def list_tanks(user_id: uuid.UUID, uow: AbstractTankUnitOfWork) -> List[dict]:

    filters = {
        "user_id": user_id,
        "is_deleted": False
    }

    with uow:
        tanks = uow.tanks.list(filters)

    return {"tanks": [dict(x) for x in tanks]}


def update_tank(tank_id: uuid.UUID, user_id: uuid.UUID, update: dict, uow: AbstractTankUnitOfWork) -> dict:

    filters = {
        "id": tank_id,
        "user_id": user_id,
        "is_deleted": False
    }

    tank = uow.tanks.read(filters)

    if tank is None:
        return None

    if not any([hasattr(tank, x) for x in update]):
        return {"Parameters not found": [x for x in update if not hasattr(tank, x)]}, 404

    if "water_type" in update.keys():
        update["water_type"] = WaterType(int(update["water_type"])).name
    if "unit_type" in update.keys():
        update["unit_type"] = WaterUnitType(int(update["unit_type"])).name

    with uow:
        uow.tanks.update(filters, update)
        uow.commit()

        tank = uow.tanks.read(filters)

    return dict(tank)


def soft_delete_tank(tank_id: uuid.UUID, user_id: uuid.UUID, uow: AbstractTankUnitOfWork) -> dict:

    filters = {
        "id": tank_id,
        "user_id": user_id,
        "is_deleted": False
    }

    with uow:
        tank = uow.tanks.read(filters)

        if tank is None:
            return {"Status": "Tank Not Found"}, 404

        uow.tanks.soft_delete(filters)
        uow.commit()

    return {"Status": "Success"}, 200


def restore_tank(tank_id: uuid.UUID, user_id: uuid.UUID, uow: AbstractTankUnitOfWork) -> dict:

    filters = {
        "id": tank_id,
        "user_id": user_id,
        "is_deleted": True
    }

    with uow:

        tank = uow.tanks.read(filters)

        if tank is None:
            return {"Status": "Tank is not deleted"}, 404

        uow.tanks.restore(filters)
        uow.commit()

        filters["is_deleted"] = False

        tank = uow.tanks.read(filters)

    return dict(tank)


def hard_delete_tank(tank_id: uuid.UUID, user_id: uuid.UUID, uow: AbstractTankUnitOfWork) -> dict:

    filters = {
        "id": tank_id,
        "user_id": user_id
    }

    with uow:
        uow.tanks.delete(filters)
        uow.commit()
