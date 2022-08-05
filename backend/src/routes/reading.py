import json
import uuid
from flask import Blueprint, request

from supertokens_python.recipe.session.framework.flask import verify_session
from supertokens_python.recipe.session import SessionContainer
from src.models.reading import ReadingUpdate
from src.service_layer.unit_of_work.reading import SqlAlchemyReadingUnitOfWork

from src.utils.utils import parse_uuid
from src.service_layer.services import reading as service

from . import session_factory

reading_blueprint = Blueprint('reading', __name__, url_prefix='/api')

@reading_blueprint.route('/reading', methods=["POST"])
@verify_session()
def add_reading():

    json_data = request.get_json()
    
    uid = uuid.uuid4()

    tank_id = json_data.pop("tank_id")
    tank_id = parse_uuid(tank_id)

    if tank_id == False: return {"Status": "Unable to parse TankId"}, 400

    reading = service.add_reading(tank_id=tank_id, id=uid, uow=SqlAlchemyReadingUnitOfWork(session_factory()), **json_data)

    print(reading)
    return reading

@reading_blueprint.route('/reading', methods=["GET"])
@verify_session()
def read_reading():

    tank_id = tank_id = request.args.get("tank_id")

    tank_id = parse_uuid(tank_id)

    if tank_id == False: return {"Status": "Unable to parse tank_id"}, 400

    reading_id = tank_id = request.args.get("reading_id")

    reading_id = parse_uuid(tank_id)

    if reading_id == False: return {"Status": "Unable to parse reading_id"}, 400

    reading = service.read_reading(tank_id=tank_id, reading_id=reading_id, uow=SqlAlchemyReadingUnitOfWork(session_factory()))

    return reading

@reading_blueprint.route('/readings', methods=["GET"])
@verify_session()
def list_readings():

    tank_id = tank_id = request.args.get("tank_id")

    tank_id = parse_uuid(tank_id)

    if tank_id == False: return {"Status": "Unable to parse tank_id"}, 400

    readings = service.list_readings(tank_id=tank_id, uow=SqlAlchemyReadingUnitOfWork(session_factory()))

    return readings


@reading_blueprint.route('/reading', methods=["PATCH"])
@verify_session()
def update_reading():

    tank_id = tank_id = request.args.get("tank_id")

    tank_id = parse_uuid(tank_id)

    if tank_id == False: return {"Status": "Unable to parse tank_id"}, 400

    reading_id = tank_id = request.args.get("reading_id")

    reading_id = parse_uuid(tank_id)

    if reading_id == False: return {"Status": "Unable to parse reading_id"}, 400

    json_data = request.get_json()

    update = ReadingUpdate(**json_data)

    reading = service.update_reading(tank_id=tank_id, reading_id=reading_id, update=update, uow=SqlAlchemyReadingUnitOfWork(session_factory()))

    return reading

@reading_blueprint.route('/readings/delete', methods=["POST"])
@verify_session()
def delete_readings():
    json_data = json.loads(request.data)
    reading_ids = json_data["reading_ids"]

    reading_ids = [parse_uuid(reading_id) for reading_id in reading_ids]

    if not any(reading_ids):
        return {"Status": "Unable to parse reading_id"}, 400

    result = service.soft_delete_readings(reading_ids, uow=SqlAlchemyReadingUnitOfWork(session_factory()))

    return result


# @reading_blueprint.route('/restore_tank', methods=["PUT"])
# @verify_session()
# def restore_tank():

#     tank_id = tank_id = request.args.get("tank_id")

#     tank_id = parse_uuid(tank_id)

#     if tank_id == False: return {"Status": "Unable to parse tank_id"}, 400

#     reading_id = tank_id = request.args.get("reading_id")

#     reading_id = parse_uuid(tank_id)

#     if reading_id == False: return {"Status": "Unable to parse reading_id"}, 400


#     status = service.restore_reading(tank_id, reading_id=reading_id, uow=SqlAlchemyReadingUnitOfWork(_session))

#     return status