from flask import Flask, render_template, jsonify, request
import requests
import os
import pwd
import tzlocal


app = Flask(__name__)

@app.route("/app")
def hello():
    with open("/etc/hostname", "r") as f:
        container_id = f.read().strip()
    container_username = pwd.getpwuid(os.getuid()).pw_name
    availability_zone = 'UTC'
    meta = {
        'container_id': container_id,
        'container_username': container_username,
        'availability_zone': availability_zone
    }

    return render_template("index.html", meta=meta)

# In-memory data storage
data = {"items": []}

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask API!"})

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify({"items": data["items"]})

@app.route('/items', methods=['POST'])
def add_item():
    item = request.json.get("item")
    if not item:
        return jsonify({"error": "Item is required"}), 400
    data["items"].append(item)
    return jsonify({"message": "Item added", "item": item}), 201

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id < 0 or item_id >= len(data["items"]):
        return jsonify({"error": "Invalid item ID"}), 404
    removed_item = data["items"].pop(item_id)
    return jsonify({"message": "Item removed", "item": removed_item})

if __name__ == '__main__':
    app.run(debug=True)