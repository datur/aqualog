from flask import jsonify, Blueprint, g
from supertokens_python.recipe.session.framework.flask import verify_session

supertoken_blueprint = Blueprint('supertoken', __name__)

@supertoken_blueprint.route('/sessioninfo', methods=['GET'])  # type: ignore
@verify_session()
def get_session_info():
    session_ = g.supertokens
    return jsonify({
        'sessionHandle': session_.get_handle(),
        'userId': session_.get_user_id(),
        'accessTokenPayload': session_.get_access_token_payload()
    })

@supertoken_blueprint.route('/supertoken', methods=['GET'])  # type: ignore
def supertoken():
    return 'Supertoken! :)'
