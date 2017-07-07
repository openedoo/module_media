import os
from flask import jsonify
from werkzeug.utils import secure_filename
from openedoo.core.libs import Blueprint, request
from .utils import random_char

UPLOAD_FOLDER = '/modules/module_media/uploads/'

module_media = Blueprint('module_media', __name__)


def add_extension(mime_type):
    return '.' + mime_type.split('/')[1]


def save_file(request):
    cwd = os.getcwd()
    mime_type = request.content_type
    rand_name = random_char(length=33)
    file_extension = add_extension(mime_type)
    file_name = secure_filename(rand_name+file_extension)
    file_path = cwd+UPLOAD_FOLDER+file_name

    with open(file_path, 'w+b') as f:
        f.write(request.get_data())

    file_info = {
        'type': mime_type,
        'path': file_path,
        'name': file_name,
        'extension': file_extension
    }
    return file_info


@module_media.route('/', methods=['POST'])
def index():
    saved_file = save_file(request)
    host_name = request.host
    file_link = '{host}/media/attachments/{f_name}'
    file_link = file_link.format(host=host_name, f_name=saved_file['name'])
    resp = {
        'type': saved_file['type'],
        'name': saved_file['name'],
        'link': file_link
    }
    return jsonify(resp)
