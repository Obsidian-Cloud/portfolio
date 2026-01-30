# io_routes.py
from time import ctime

from flask import Blueprint
from flask import request

from flask_json import json_response
from flask_json import as_json

from zope.component import getUtility

from components.Interactor import request as _req
from components.Interfaces.interfaces import IComposer

# The use-case category for CRUD API operations
category = 'crud'
now = ctime()
io_routes_bp = Blueprint('io_routes', __name__)



@io_routes_bp.route('/api/insert-row/', methods=['POST'])
@as_json
def insert_row():
    if request.method == 'POST':
        data = request.get_json()
        _req.request_ds = data
        implementation = getUtility(IComposer)
        implementation.execute_composer()
        return json_response(test=12)
    return json_response(test=12)


@io_routes_bp.route('/api/update-row/', methods=['POST'])
@as_json
def update_row():
    if request.method == 'POST':
        data = request.get_json()
        _req.request_ds = data
        implementation = getUtility(IComposer)
        response = implementation.execute_composer()
        if 'error' in response:
            return (response, 422)
        return (response, 201)
    return json_response(405)


@io_routes_bp.route('/api/delete-row/', methods=['POST'])
@as_json
def delete_row():
    if request.method == 'POST':
        data = request.get_json()
        _req.request_ds = data
        implementation = getUtility(IComposer)
        implementation.execute_composer()
        return json_response(test=12)
    return json_response(test=12)
