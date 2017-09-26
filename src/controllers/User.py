from src.infrastructure.UserDataAccess import UserDataAccess
from src.controllers.helpers.UserRequestHelper import validate_user_request
from src.infrastructure.MessagePublisher import Publisher
import os
from src.entities.User import Password, User_Post_Request, User_Get_Response
import json
import random, string
from flask import request, Response, Blueprint
import hashlib
import bcrypt
import uuid

user_controller = Blueprint('user_controller', __name__, template_folder='templates')

def _to_json(obj):
	return json.dumps(obj, default=lambda o: o._serialize() if getattr(o, "_serialize", None) else o.__dict__, sort_keys=True, indent=4)


def _get_key():
    key = str(uuid.uuid4())
    return key

def _hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = hashlib.sha512(str(password).encode('utf-8') + str(salt).encode('utf-8')).hexdigest()

    return Password(hashed_password, salt)

def get_error_obj_json(error_list):
    error = {'errors': error_list}
    return json.dumps(error, default=lambda o: o._serialize() if getattr(o, "_serialize", None) else o.__dict__, sort_keys=True, indent=4)

def _get_user_from_request(data):

    full_name = data.get('full_name')
    phone_number = data.get('phone_number')
    email = data.get('email')
    password = data.get('password')
    metadata = data.get('metadata')

    return (User_Post_Request(email, phone_number, full_name, password, metadata))

@user_controller.route("/v1/users", methods=['GET'])
def get_user():
    try:
        if len(request.args) > 0 and 'query' not in request.args:
            return Response(get_error_obj_json(["'query' is the only query string parameter allowed"]), 422, mimetype='application/json')

        filter_string = request.args.get('query', None)
        user_response = UserDataAccess().get_user(filter_string)

        return Response(_to_json(user_response), 200, mimetype="application/json")
    except Exception as e:
        return Response(get_error_obj_json(['Error in creating user']), 500, mimetype="application/json")

@user_controller.route('/v1/users', methods=['POST'])
def post_user():
    request_body = request.get_json()
    error_list = validate_user_request(request_body)

    if (len(error_list) == 0):

        user_request = _get_user_from_request(request_body)

        user_request.key = _get_key()
        user_request.password = _hash_password(user_request.password)
        user_request.account_key = None

        new_id = UserDataAccess().update_user(user_request)
        user_response = User_Get_Response(user_request.email, user_request.phone_number, user_request.full_name,
                                          user_request.key, user_request.account_key, user_request.metadata)

        if ('account_key_requested_topic' in os.environ):
            try:
                Publisher(os.environ['aws_region'], os.environ['aws_access_key_id'],
                          os.environ['aws_secret_access_key']).publish_message(user_request.email, user_request.key)
            except Exception as e:
                print('error pulishing topic to request account key')

        if (new_id > 0):
            user_request.id = new_id
            return Response(_to_json(user_response), 201, mimetype="application/json")
        else:
            return Response(get_error_obj_json(['Failed to create user']), 500, mimetype="application/json")
    else:
        return Response(get_error_obj_json(error_list), 406, mimetype="application/json")
