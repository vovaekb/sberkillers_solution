import os
import flask
import json
from flask import Flask, request, jsonify, Response
from s3_bucket import upload_file
from process_video import filter_video

# Create database structure

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return Response('Hello', status=200)

@app.route('/recognize', methods=['POST'])
def recognize():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        file_path = data['source']
        # TODO: Process file
        # prefix = data['prefix']
        # result_file = filter_video(file_path)
        # upload_file(result_file)
        result = {
            'result': []
        }
        return jsonify(result)



