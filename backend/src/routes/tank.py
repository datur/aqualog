import json
import uuid
from flask import Blueprint, request, g
from src.service_layer.unit_of_work.tank import SqlAlchemyTankUnitOfWork
from src.models.utils import WaterUnitType

from src.utils.utils import parse_uuid
from src.service_layer.services import tank as service

from supertokens_python.recipe.session.framework.flask import verify_session
from supertokens_python.recipe.session import SessionContainer

from . import _session

tank_blueprint = Blueprint('tank', __name__, url_prefix='/api')


@tank_blueprint.route('/tank', methods=["POST"])
@verify_session()
def add_tank():
    session: SessionContainer = g.supertokens

    supertoken_id = session.get_user_id()

    user_id = parse_uuid(supertoken_id)

    json_data = request.get_json()

    uid = uuid.uuid4()

    name = json_data.get('name')
    capacity = json_data.get('capacity')
    unit_type = json_data.get('unit_type')
    water_type = json_data.get('water_type')

    tank = service.add_tank(user_id=user_id,
                            id=uid, name=name,
                            capacity=capacity,
                            unit_type=unit_type,
                            water_type=water_type,
                            uow=SqlAlchemyTankUnitOfWork(_session))

    return tank


@tank_blueprint.route('/tank', methods=["GET"])
@verify_session()
def read_tank():
    session: SessionContainer = g.supertokens
    supertoken_id = session.get_user_id()

    user_id = parse_uuid(supertoken_id)

    tank_id = request.args.get("tank_id")

    tank_id = parse_uuid(tank_id)

    if tank_id == False:
        return {"Status": "Unable to parse TankId"}, 400

    tank = service.read_tank(
        tank_id, user_id, SqlAlchemyTankUnitOfWork(_session))

    print(tank)

    if tank is None:
        return {"Status": "Tank Not Found"}, 404

    return tank


@tank_blueprint.route('/tanks', methods=["GET"])
@verify_session()
def list_tanks():
    session: SessionContainer = g.supertokens

    supertoken_id = session.get_user_id()

    user_id = parse_uuid(supertoken_id)

    tanks = service.list_tanks(user_id, SqlAlchemyTankUnitOfWork(_session))

    return tanks


@tank_blueprint.route('/tank', methods=["PATCH"])
@verify_session()
def update_tank():
    session: SessionContainer = g.supertokens

    supertoken_id = session.get_user_id()

    user_id = parse_uuid(supertoken_id)

    update = request.get_json()

    tank_id = request.args.get("tank_id")

    tank_id = parse_uuid(tank_id)

    if tank_id == False:
        return "Unable to parse Tank Id", 400

    tank = service.update_tank(
        tank_id, user_id, update, SqlAlchemyTankUnitOfWork(_session))

    if tank is None:
        return "Tank Not Found", 404

    return tank


@tank_blueprint.route('/tank', methods=["DELETE"])
@verify_session()
def delete_tank():
    session: SessionContainer = g.supertokens

    supertoken_id = session.get_user_id()

    user_id = parse_uuid(supertoken_id)

    tank_id = request.args.get("tank_id")

    tank_id = parse_uuid(tank_id)

    if tank_id == False:
        return "Unable to parse Reading Id", 400

    soft_delete = request.args.get("soft", None)

    if soft_delete:
        status = service.soft_delete_tank(
            tank_id, user_id, SqlAlchemyTankUnitOfWork(_session))
        return status

    hard_delete = request.args.get("hard", None)

    if hard_delete:
        service.hard_delete_tank(
            tank_id, user_id, SqlAlchemyTankUnitOfWork(_session))
        return {"Status": "Success"}, 200

    return "Bad Requesst", 400


@tank_blueprint.route('/restore_tank', methods=["PUT"])
@verify_session()
def restore_tank():
    session: SessionContainer = g.supertokens

    supertoken_id = session.get_user_id()

    user_id = parse_uuid(supertoken_id)

    tank_id = request.args.get("tank_id")

    tank_id = parse_uuid(tank_id)

    status = service.restore_tank(
        tank_id, user_id, SqlAlchemyTankUnitOfWork(_session))

    return status
