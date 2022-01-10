import os
from server import flask_app as app
from server.settings import UPLOAD_FOLDER, OUTPUT_FOLDER
from flask import request, Response, render_template
import json

# from scripts import checkbox_detect, table_analysis, util, template_extract
# from utils import CustomEncoder

output_fpath = '/static/outputs/'

@app.route('/')
def home():
    """
    URL: /
    Homepage for the app
    """
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    """
    URL: /process
    Returns JSON response for the request sent to process.
    """
    # action = request.form['actionType']
    # page = int(request.form['page'])
    # document = request.files['document']
    # filename = UPLOAD_FOLDER + document.filename
    # name = os.path.basename(filename).split('.')[0]
    # document.save(filename)


    # return json.dumps(response, cls=CustomEncoder)
    return