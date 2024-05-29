from flask import Flask, request, abort
import os
import tempfile
import tarfile
import shutil
from flask_cors import CORS, cross_origin

api = Flask(__name__)
cors = CORS(api)
api.config['CORS_HEADERS'] = 'Content-Type'

@api.route('/unslippy', methods=['POST'])
def cache():
    if 'file' not in request.files:
        return abort(400)
    extraction = extract_from_archive(request.files['file'])
    if extraction:
        return {"list": extraction}, 200
    return '', 204

def extract_from_archive(file):
    tmp = tempfile.gettempdir()
    path = os.path.join(tmp, file.filename)
    file.save(path)

    if tarfile.is_tarfile(path):
        tar = tarfile.open(path, 'r:gz')
        tar.extractall(tmp)
        extractdir = './archive/123'
        os.makedirs(extractdir, exist_ok=True)
        extracted_filenames = []
        for tarinfo in tar:
            name = tarinfo.name
            if tarinfo.isreg():
                filename = os.path.join(extractdir, name)
                shutil.move(os.path.join(tmp, name), filename)
                extracted_filenames.append(filename)
                continue
            os.makedirs(os.path.join(extractdir, name), exist_ok=True)
        tar.close()
        return extracted_filenames
    return False
