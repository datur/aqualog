from .supertoken.supertoken import supertoken_blueprint
from .user import user_blueprint
from .tank import tank_blueprint
from .reading import reading_blueprint
from flask import Blueprint, abort

routes = Blueprint('routes', __name__)

# This is required since if this is not there, then OPTIONS requests for
# the APIs exposed by the supertokens' Middleware will return a 404


def build_routes() -> Blueprint:

    @routes.route('/', defaults={'u_path': ''})  # type: ignore
    @routes.route('/<path:u_path>')  # type: ignore
    def catch_all(u_path: str):  # pylint: disable=unused-argument
        abort(404)

    routes.register_blueprint(supertoken_blueprint)
    routes.register_blueprint(user_blueprint)
    routes.register_blueprint(tank_blueprint)
    routes.register_blueprint(reading_blueprint)
    return routes