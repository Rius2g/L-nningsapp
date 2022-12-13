#! flask/bin/python3
from flask import Flask, jsonify, abort, make_response, request
from flask_cors import CORS
import time
from random import random
import datetime as date

x = date.datetime.now()

class User:

    def __init__(self): #settings in the top
        self.payrate = 10
        self.taxrate = 7

        self.items = []#array for shifts

    def put_settings(self, payrate, taxrate): #update the settings
        self.payrate = payrate
        self.taxrate = taxrate
  

User1 = User()

app = Flask(__name__)
CORS(app)


# Once your client works, you can apply this decorator
# to one of the endpoints to add a random delay to simulate
# the operation taking a long time due to database transactions etc.
def randomdelay(func):
    print("Applying random delay to", func.__name__)

    def inner(*args, **kwargs):
        time.sleep(random() * 5)
        return func(*args, **kwargs)

    return inner


@app.errorhandler(405)
def not_allowed_error(error):
    text = jsonify({"Code": "405", "Message": "Method Not Allowed"})
    return make_response(text, 405)


@app.errorhandler(404)
def not_found_error(error):
    text = jsonify(
        {"Code": "404", "Message": "Not Found", "Description": error.description}
    )
    return make_response(text, 404)


@app.errorhandler(400)
def bad_request_error(error):
    text = jsonify(
        {"Code": "400", "Message": "Bad Request", "Description": error.description}
    )
    return make_response(text, 400)


@app.route("/api/items/", methods=["GET"])
def get_items(): 
    return jsonify({"items": User1.items})


@app.route("/api/payrate/", methods=["GET"])
def get_payrate(): 
    return jsonify(payrate=str(User1.payrate))


@app.route("/api/taxrate/", methods=["GET"])
def get_taxrate(): 
    return jsonify(taxrate=str(User1.taxrate))



@app.route("/api/payrate/", methods=["PUT"])
def update_payrate(): 
    User1.put_settings(request.json["payrate"], request.json["taxrate"])
    return jsonify(payrate=str(User1.payrate) , taxrate=str(User1.taxrate))


@app.route("/api/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    for item in User1.items:
        if item["id"] == item_id:
            return jsonify({"item": item})
    message = f"No item with ID {item_id}."
    abort(404, message)


@app.route("/api/items/", methods=["POST"])
def create_item():
    if not request.json:
        abort(400, "Must be JSON.")
    if "date" not in request.json:
        abort(400, "Must contain 'date'-field.")
    if not isinstance(request.json["date"], str):
        description = f"'name'-field must be str."
        abort(400, description)
    new_id = 0 if not User1.items else max(item["id"] for item in User1.items) + 1
    item = {"id": new_id, "date": request.json["date"], "start": request.json["start"], "end": request.json["end"]}
    User1.items.append(item)
    return jsonify({"item": item}), 201


@app.route("/api/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    if not request.json:
        abort(400, "Must be JSON.")
    wanted_item = None
    for item in User1.items:
        if item["id"] == item_id:
            wanted_item = item
            break

    if not wanted_item:
        message = f"No item with ID {item_id}."
        abort(404, message)
    update = request.json
    if "name" in update:
        if not isinstance(update["name"], str):
            message = f"'name' field must be a str."
            abort(404, message)
        wanted_item["name"] = update["name"]

    if "done" in update:
        if not isinstance(update["done"], bool):
            message = f"'done' field must be a boolean."
            abort(404, message)
        wanted_item["done"] = update["done"]

    return jsonify({"item": wanted_item})


@app.route("/api/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    old_item = False
    for item in User1.items:
        if item["id"] == item_id:
            old_item = item
            break
    if not old_item:
        message = f"No item with ID {item_id}."
        abort(404, message)
    User1.items.remove(old_item)
    return jsonify({"deleted": True})


if __name__ == "__main__":
    app.run(debug=True)
