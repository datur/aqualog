import uuid
from flask import Blueprint, request, g
from supertokens_python.recipe.session.framework.flask import verify_session
from supertokens_python.recipe.session import SessionContainer
from supertokens_python.recipe.emailpassword.syncio import get_user_by_id

from src.utils.utils import parse_uuid
from src.adapters.session_factory import session_factory
from src.service_layer.services import user as service
from src.service_layer.unit_of_work.user import SqlAlchemyUserUnitOfWork

from . import _session

user_blueprint = Blueprint('user', __name__, url_prefix='/api')

@user_blueprint.route('/user', methods=["POST"])
@verify_session()
def add_user():
    session: SessionContainer = g.supertokens

    supertoken_id = session.get_user_id()

    json_data = request.get_json()

    uid = parse_uuid(supertoken_id)

    user = service.read_user(uid, SqlAlchemyUserUnitOfWork(_session))

    if user is not None:
        return "User already exists", 400

    f_name = json_data.get('first_name')
    l_name = json_data.get('last_name')
    email = json_data.get('email')

    user = service.add_user(uid, f_name, l_name, email, SqlAlchemyUserUnitOfWork(_session))

    print(user)

    return user

@user_blueprint.route('/user', methods=["GET"])
@verify_session()
def read_user():
    session: SessionContainer = g.supertokens

    supertoken_id = session.get_user_id()

    uid = parse_uuid(supertoken_id)

    user = service.read_user(uid, SqlAlchemyUserUnitOfWork(_session))

    if user is None:
        user = get_user_by_id(supertoken_id)
        if user is None:
            return "Error during Signup", 500
        user = {
            "id": supertoken_id,
            "email": user.email,
        }

    # print(get_user_by_id(supertoken_id).email)

    return user

@user_blueprint.route('/user', methods=["PATCH"])
@verify_session()
def update_user():
    session: SessionContainer = g.supertokens

    supertoken_id = session.get_user_id()

    uid = parse_uuid(supertoken_id)

    update = request.get_json()

    user = service.update_user(uid, update, SqlAlchemyUserUnitOfWork(_session))

    print(user)

    return user

@user_blueprint.route('/user', methods=["DELETE"])
@verify_session()
def delete_user():
    session: SessionContainer = g.supertokens

    supertoken_id = session.get_user_id()

    uid = parse_uuid(supertoken_id)

    service.delete_user(uid, SqlAlchemyUserUnitOfWork(_session))

    return "Success", 200

@user_blueprint.route('/user_exists', methods=["GET"])
@verify_session()
def check_user_exists():
    session: SessionContainer = g.supertokens

    supertoken_id = session.get_user_id()

    uid = parse_uuid(supertoken_id)

    user = service.read_user(uid, SqlAlchemyUserUnitOfWork(_session))

    print(user)

    exists = True if user is not None else False

    print(exists)
    # exists = False

    return dict({"exists": exists})

@user_blueprint.route('/user_email', methods=["GET"])
@verify_session()
def get_user_email():
    session: SessionContainer = g.supertokens

    supertoken_id = session.get_user_id()

    user = get_user_by_id(supertoken_id)

    return dict({
        "email": user.email
    })