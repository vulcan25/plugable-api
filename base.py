from flask import Blueprint, make_response, json, current_app
from bson import ObjectId
from flask.views import MethodView
from ..pymongo import DuplicateKeyError
from .exceptions import BadRequest, Unauthorized, Forbidden
from ..security import get_current_user

the_api = Blueprint('the_api', __name__)


class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self, obj)

def handle_exception(e):
    # handle common exceptions
    if isinstance(e, DuplicateKeyError):
        raise BadRequest(str(e))


def json_converter(f):
    '''Converts `dict`, list or mongo cursor to JSON.
    Creates `~flask.Response` object and sets headers.
    '''
    def decorator(*args, **kwargs):
        try:
            result = f(*args, **kwargs)
        except Exception as e:
            handle_exception(e)
            raise

        if isinstance(result, dict):
            result = json.dumps(result, cls=JsonEncoder)
        else:
            # unwind cursor
            result = json.dumps(list(result), cls=JsonEncoder)
        response = make_response(result)
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response
    return decorator


def login_required(f):
    def decorator(*args, **kwargs):
        if not get_current_user().is_authenticated():
            raise Unauthorized('You must log in to access this URL.')
        return f(*args, **kwargs)
    return decorator


def admin_required(f):
    def decorator(*args, **kwargs):
        if not get_current_user().is_admin():
            raise Forbidden('You must be an admin to access this URL.')
        return f(*args, **kwargs)
    return decorator


class APIEndpoint(MethodView):
    # make converter run after every request handler method returns
    decorators = [json_converter, login_required]

    def __init__(self, *args, **kwargs):
        super(APIEndpoint, self).__init__(*args, **kwargs)
        self.logger = current_app.logger


class AdminAPIEndpoint(APIEndpoint):
    decorators = APIEndpoint.decorators + [admin_required]
