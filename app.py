from flask import Flask, Response
from flask_cors import CORS
import json
import logging

from application_services.imdb_artists_resource import IMDBArtistResource
from application_services.UsersResource.user_service import UserResource
from application_services.UsersResource.address_service import AddressResource
from database_services.RDBService import RDBService as RDBService

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return '<u>Hello World!</u>'


@app.route('/imdb/artists/<prefix>')
def get_artists_by_prefix(prefix):
    res = IMDBArtistResource.get_by_name_prefix(prefix)
    rsp = Response(json.dumps(res), status=200, content_type="application/json")
    return rsp


@app.route('/users')
def get_users():
    res = UserResource.get_all_user_data("usersInfo")
    rsp = Response(json.dumps(res), status=200, content_type="application/json")
    return rsp

@app.route('/users/<userID>')
def get_users_by_id(userID):
    res = UserResource.get_user_data_by_id("usersInfo", userID)
    rsp = Response(json.dumps(res), status=200, content_type="application/json")
    return rsp

@app.route('/users/<userID>/address')
def get_address_by_userid(userID):
    res = UserResource.get_user_address_by_id("usersInfo", userID)
    rsp = Response(json.dumps(res), status=200, content_type="application/json")
    return rsp

@app.route('/address')
def get_address():
    res = AddressResource.get_all_address_data("usersInfo")
    rsp = Response(json.dumps(res), status=200, content_type="application/json")
    return rsp

@app.route('/address/<addressID>')
def get_address_by_id(addressID):
    res = AddressResource.get_address_data_by_id("usersInfo", addressID)
    rsp = Response(json.dumps(res), status=200, content_type="application/json")
    return rsp

@app.route('/address/<addressID>/users')
def get_users_by_addressid(addressID):
    res = AddressResource.get_address_user_by_id("usersInfo", addressID)
    rsp = Response(json.dumps(res), status=200, content_type="application/json")
    return rsp

@app.route('/<db_schema>/<table_name>/<column_name>/<prefix>')
def get_by_prefix(db_schema, table_name, column_name, prefix):
    res = RDBService.get_by_prefix(db_schema, table_name, column_name, prefix)
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
