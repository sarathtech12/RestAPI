import logging
import os
import pathlib
import uuid
from flask import Flask, request, send_file, jsonify
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = r"C:\sandbox"

@app.route('/')
@app.route('/home')
def homepage():
    return "Home Page"

@app.route('/uploadfile', methods=['POST'])
def upload_file():
        file = request.args.get('file_id')
        print(file)
        path = app.config['UPLOAD_FOLDER']
        dir_list = os.listdir(path)
        print(dir_list)
        if file in dir_list :
            print('File Exist')
            return jsonify(file, 'File Exist'), 200
        else:
            print('File does not exist')
            return jsonify(file, 'File does not exist'), 400

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGER_UI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Device"
    }
)
app.register_blueprint(SWAGGER_UI_BLUEPRINT, url_prefix=SWAGGER_URL)

app.run(debug=True)
