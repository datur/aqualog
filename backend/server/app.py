from server.config import get_website_domain
from server.config import get_api_port
from src.routes.routes import build_routes
from server.supertokens import init_supertokens
from src.adapters.orm import start_mappers
from supertokens_python import (InputAppInfo, SupertokensConfig
                                , init)

from flask import Flask, abort, g, jsonify, url_for
from flask_cors import CORS

from supertokens_python import get_all_cors_headers
from supertokens_python.framework.flask import Middleware
from supertokens_python.recipe import session, thirdparty
from supertokens_python.recipe.session.framework.flask import verify_session
from supertokens_python.recipe.thirdpartyemailpassword import (
     Github, Google)

def create_app():
    init_supertokens()

    start_mappers()

    app = Flask(__name__)

    Middleware(app)

    CORS(
        app=app,
        origins=[
            "http://localhost:3000"
        ],
        supports_credentials=True,
        allow_headers=["Content-Type"] + get_all_cors_headers(),
    )

    app.register_blueprint(build_routes())

    # @app.route('/', defaults={'u_path': ''})  # type: ignore
    # @app.route('/<path:u_path>')  # type: ignore
    # def catch_all(u_path: str):  # pylint: disable=unused-argument
    #     abort(404)

    return app