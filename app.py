from flask import Flask, jsonify, request
import json
import logging
import sys
from flask.logging import default_handler
import os
from dotenv import load_dotenv
from gevent.pywsgi import WSGIServer

def removeLog():
    logging.getLogger('werkzeug').setLevel(logging.ERROR)
    sys.modules['flask.cli'].show_server_banner = lambda *x: None

# create a function that prints message in given hex color in the terminal
def printColor(message, color):
    return (f"\033[{color}m{message}\033[00m")


load_dotenv()

app = Flask(__name__)





# log_format = "%(asctime)s - %(levelname)s - %(message)s"
# removeLog()
# log_format = "%(message)s"
# logging.basicConfig(level=logging.INFO, format=log_format)
print(f"Running JSON-SERVER on port {os.getenv('PORT')}")

with open('db.json', 'r') as f:
    data = json.load(f)
    # print the possible routes, for GET, POST, PUT, DELETE
    for key in data:
        # add a separator between each resource
        print(f"\n\033[1m\033[4m{key.upper()}\033[00m")
        # GET with blue
        print(f"{printColor('GET', '34')} /{key}")
        # POST with green
        print(f"{printColor('GET', '34')} /{key}/<id>")
        print(f"{printColor('POST', '32')} /{key}")
        # PUT with yellow
        print(f"{printColor('PUT', '33')} /{key}")
        # print delete with red
        print(f"{printColor('DELETE', '31')} /{key}")

@app.route('/<resource>', methods=['GET'])
def get_resource(resource):
    if resource in data:
        return jsonify(data[resource])
    else:
        return jsonify({"error": "Resource not found"}), 404

@app.route('/<resource>/<id>', methods=['GET'])
def get_resource_by_id(resource, id):
    if resource in data:
        for item in data[resource]:
            if item['id'] == int(id):
                return jsonify(item)
        # Resource - use the param value not found
        return jsonify({"error": f"{resource} not found"}), 404
    else:
        return jsonify({"error": "Resource not found"}), 404

@app.route('/<resource>', methods=['POST'])
def create_resource(resource):
    if resource in data:
        return jsonify({"error": "Resource already exists"}), 400
    else:
        data[resource] = request.json
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        return jsonify(data[resource]), 201

@app.route('/<resource>', methods=['PUT'])
def update_resource(resource):
    if resource in data:
        data[resource] = request.json
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        return jsonify(data[resource])
    else:
        return jsonify({"error": "Resource not found"}), 404

@app.route('/<resource>', methods=['DELETE'])
def delete_resource(resource):
    if resource in data:
        del data[resource]
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        return jsonify({"message": "Resource deleted"})
    else:
        return jsonify({"error": "Resource not found"}), 404

# To include children resources, add child resource name after parent resource name and id
# GET /posts/1?child=comments


if __name__ == "__main__":
    # use .env file to get port
    # app.run(port=os.getenv('PORT'), debug=False)
    app.debug = True
    http_server = WSGIServer(('', int(os.getenv('PORT'))), app)
    http_server.serve_forever()