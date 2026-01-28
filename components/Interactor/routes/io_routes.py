# io_routes.py
from time import ctime

from flask import Blueprint
from flask import request

from flask_json import json_response

from zope.component import getUtility

from components.Interactor import request as _req

from components.Interfaces.interfaces import IComposer

# The use-case category for CRUD API operations
category = 'crud'
now = ctime()
io_routes_bp = Blueprint('io_routes', __name__)

'''
class _Response():
    @staticmethod
    def _return():
        return 
'''

@io_routes_bp.route('/api/create-table/', methods=['POST'])
def create_table():
    if request.method == 'POST':
        # `data` is retrieved at runtime therefore `data` doesnt 
        # exist statically.
        data = request.get_json()
        _req.request_ds = data
        implementation = getUtility(IComposer)
        implementation.execute_composer(category)

    return json_response(time=now)


@io_routes_bp.route('/api/drop-table/', methods=['POST'])
def drop_table():
    if request.method == 'POST':
        data = request.get_json()
        _req.request_ds = data
        implementation = getUtility(IComposer)
        implementation.execute_composer(category)
    return dict()


@io_routes_bp.route('/api/insert-row', methods=['POST'])
def insert_row():
    if request.method == 'POST':
        data = request.get_json()
        _req.request_ds = data
        implementation = getUtility(IComposer)
        implementation.execute_composer(category)
    return dict()


@io_routes_bp.route('/api/update-row/', methods=['POST'])
def update_row():
    if request.method == 'POST':
        data = request.get_json()
        print('data')
        print(data)
        _req.request_ds = data


        implementation = getUtility(IComposer)
        implementation.execute_composer()
    return dict()


@io_routes_bp.route('/api/delete-row', methods=['POST'])
def delete_row():
    if request.method == 'POST':
        data = request.get_json()
        _req.request_ds = data
        implementation = getUtility(IComposer)
        implementation.execute_composer(category)
    return dict()


@io_routes_bp.route('/api/fetch-table', methods=['GET'])
def fetch_table():
    if request.method == 'GET':
        data = request.get_json()
        _req.request_ds = data
        implementation = getUtility(IComposer)
        implementation.execute_composer(category)
    return dict()


@io_routes_bp.route('/api/fetch-row', methods=['GET'])
def fetch_row():
    if request.method == 'GET':
        data = request.get_json()
        _req.request_ds = data
        implementation = getUtility(IComposer)
        implementation.execute_composer(category)
    return dict()


@io_routes_bp.route('/api/fetch_rows', methods=['GET'])
def fetch_rows():
    if request.method == 'GET':
        data = request.get_json()
        _req.request_ds = data
        implementation = getUtility(IComposer)
        implementation.execute_composer(category)
    return dict()
