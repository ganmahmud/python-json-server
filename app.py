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

def findIndexById(resourceList, id):
    for index, item in enumerate(resourceList):
        if item.get("id") == id:
            return index
    return None

def printColor(message, color):
    return (f"\033[{color}m{message}\033[00m")

load_dotenv()

app = Flask(__name__)


print(f"Running JSON-SERVER on port {os.getenv('PORT')}")

try:
    with open('db.json', 'r') as f:
        data = json.load(f)

    for key in data:
        print(f"\n\033[1m\033[4m{key.upper()}\033[00m")
        # GET with blue
        print(f"{printColor('GET', '34')} http://localhost:{os.getenv('PORT')}/{key}")
        # POST with green
        print(f"{printColor('GET', '34')} /{key}/<id>")
        print(f"{printColor('POST', '32')} /{key}")
        # PUT with yellow
        print(f"{printColor('PUT', '33')} /{key}")
        # print delete with red
        print(f"{printColor('DELETE', '31')} /{key}")

except FileNotFoundError:
    print("json data not found")
    exit()


@app.route('/<resource>', methods=['GET'])
def get_resource(resource):
    if resource in data:
        return jsonify(data[resource])
    else:
        return jsonify({"error": "Resource not found"}), 404

@app.route('/<resource>/<id>', methods=['GET'])
def get_resource_by_id_with_children(resource, id):
    if resource in data:
        for item in data[resource]:
            if item['id'] == int(id):
                # print(request.args.get('child'))
                if 'child' in request.args:
                    child = request.args.get('child')
                    if child in data:
                        children = []
                        for child_item in data[child]:
                            if child_item['postId'] == int(id):
                                children.append(child_item)
                        return jsonify(children)
                    else:
                        return jsonify({"error": f"{child} not found"}), 404
                else:
                    return jsonify(item)
        return jsonify({"error": f"{resource} not found"}), 404
    else:
        return jsonify({"error": f"{resource} not found"}), 404


@app.route('/<resource>', methods=['POST'])
def create_resource(resource):
    data[resource].append(request.json)
    with open('db.json', 'w') as f:
        json.dump(data, f, indent=4)
    return jsonify(data[resource]), 201

@app.route('/<resource>/<id>', methods=['PUT'])
def update_resource(resource, id):
    # first check if the id exists
    needle = findIndexById(data[resource], int(id))
    if needle is not None:
        data[resource][needle] = request.json
        with open('db.json', 'w') as f:
            json.dump(data, f, indent=4)
        return jsonify(data[resource][needle])
    else:
        return jsonify({"error": f"{resource} not found"}), 404


@app.route('/<resource>/<id>', methods=['PATCH'])
def patch_resource(resource, id):
    # First, check if the ID exists
    needle = findIndexById(data[resource], int(id))
    
    if needle is not None:
        updated_data = request.json
        itemTobePatched = data[resource][needle]
        for key in updated_data:
            itemTobePatched[key] = updated_data[key]
        
        data[resource][needle] = itemTobePatched
        
        with open('db.json', 'w') as f:
            json.dump(data, f, indent=4)
        
        return jsonify(data[resource][needle])
    else:
        return jsonify({"error": f"{resource} not found"}), 404


@app.route('/<resource>/<id>', methods=['DELETE'])
def delete_resource(resource, id):
    needle = findIndexById(data[resource], int(id))
    if needle is not None:
        del data[resource][needle]
        with open('db.json', 'w') as f:
            json.dump(data, f, indent=4)
        return jsonify({"message": f"{resource} deleted"}), 200
    else:
        return jsonify({"error": f"{resource} not found"}), 404




if __name__ == "__main__":
    # use .env file to get port
    # app.run(port=os.getenv('PORT'), debug=False)
    http_server = WSGIServer(('', int(os.getenv('PORT'))), app)
    http_server.serve_forever()