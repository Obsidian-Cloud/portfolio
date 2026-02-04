# io_routes.py
from time import ctime

from flask import session
from flask import Blueprint
from flask import request

from flask_json import json_response
from flask_json import as_json

from zope.component import getUtility

from components.Interactor import request as _req
from components.Interfaces.interfaces import IComposer

now = ctime()
io_routes_bp = Blueprint('io_routes', __name__)


@io_routes_bp.route('/api/insert-row/', methods=['POST'])
@as_json
def insert_row():
    if request.method == 'POST':
        data = request.get_json()
        print('DATA')
        print(data)
        data['payload']['user_cookie'] = session['user_cookie']
        # implementation below this comment is completely plug-n-play into
        # different API frameworks. no other component knows about Flask.
        _req.request_ds = data
        implementation = getUtility(IComposer)
        _response = implementation.execute_composer()
        if 'error' in _response:
            return (_response, 422)
        return (_response, 201)
    return json_response(405)


@io_routes_bp.route('/api/update-row/', methods=['POST'])
@as_json
def update_row():
    if request.method == 'POST':
        data = request.get_json()
        data['payload']['user_cookie'] = session['user_cookie']
        _req.request_ds = data
        implementation = getUtility(IComposer)
        _response = implementation.execute_composer()
        print('RESPONSE')
        print(_response)
        if 'error' in _response:
            return (_response, 422)
        return (_response, 201)
    return json_response(405)


@io_routes_bp.route('/api/delete-row/', methods=['POST'])
@as_json
def delete_row():
    if request.method == 'POST':
        data = request.get_json()
        data['payload']['user_cookie'] = session['user_cookie']
        _req.request_ds = data
        implementation = getUtility(IComposer)
        _response = implementation.execute_composer()
        if 'error' in _response:
            return (_response, 422)
        return (_response, 201)
    return json_response(405)