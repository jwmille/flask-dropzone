# -*- coding: utf-8 -*-
import os

from flask import Flask, render_template, request, redirect
from flask_dropzone import Dropzone

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)

app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'uploads'),
    # Flask-Dropzone config:
    DROPZONE_ALLOWED_FILE_TYPE='image',
    DROPZONE_MAX_FILE_SIZE=3,
    DROPZONE_MAX_FILES=20,
    DROPZONE_UPLOAD_ON_CLICK=True
)

dropzone = Dropzone(app)


@app.route('/', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        for key, f in request.files.iteritems():  # use request.files.items() in Python3
            if key.startswith('file'):
                f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
