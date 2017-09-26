from flask import Blueprint, Response
import os
import json
from src.infrastructure.UserDataAccess import UserDataAccess

help_controller = Blueprint('help_controller', __name__, template_folder='templates')

@help_controller.route('/v1/help', methods=['GET'])
def help():
    content = ''
    dir = os.path.join(os.path.dirname(__file__), "../docs/swagger.yaml")
    with open(dir, 'r') as content_file:
        content = content_file.read()

    return content, 200


def _to_json(obj):
	return json.dumps(obj, default=lambda o: o._serialize() if getattr(o, "_serialize", None) else o.__dict__, sort_keys=True, indent=4)

def module_obj(module, status):
    return {'module': module, 'status': status}

@help_controller.route('/v1/health', methods=['GET'])
def health():
    try:
        module_status_list = []
        userdb_status = UserDataAccess().connect_to_db()

        aws_connection_creds = False
        if 'aws_region' in os.environ and 'aws_access_key_id' in os.environ and 'aws_secret_access_key' in os.environ:
            aws_connection_creds = True

        module_status_list.append(module_obj('userdb', userdb_status))
        module_status_list.append(module_obj('aws connection', aws_connection_creds))

        return Response(_to_json(module_status_list), 200, mimetype='application/json')
    except Exception as e:
        return Response(None, 500, mimetype='application/json')