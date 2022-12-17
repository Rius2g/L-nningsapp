#! flask/bin/python3
from flask import Flask, jsonify, abort, make_response, request
from flask_cors import CORS
import time
from random import random
import sqlite3

class User:

    def __init__(self): #settings in the top
        self.payrate = 1
        self.taxrate = 1

        self.items = []#array for shifts
        self.startRange = ""
        self.endRange = ""


    def create_db(self): #create two tables for shifts and settings
        self.connection = sqlite3.connect("shifts.db") #connect to the database
        self.cursor = self.connection.cursor() #create a cursor
        sql_command = """ CREATE TABLE IF NOT EXISTS shifts ( 
                Sid INTEGER PRIMARY KEY AUTOINCREMENT,
                Uid INTEGER NOT NULL AUTOINCREMENT,
                Date INTEGER(255) NOT NULL,
                Start varchar(255) NOT NULL,
                End varchar(255) NOT NULL);"""

        sql_command2 = """ CREATE TABLE IF NOT EXISTS users ( 
                Uid INTEGER PRIMARY KEY AUTOINCREMENT,
                Payrate INTEGER NOT NULL,
                Taxrate INTEGER NOT NULL,
                Name varchar(255)
                FOREIGN KEY(Uid) REFERENCES shifts(uid));"""

            #shift id, user id, date, start time, end time
        self.cursor.execute(sql_command) #create the shifts table
        self.cursor.execute(sql_command2) #create the user/settings table with foreign key uid
        self.connection.commit()
        self.cursor.close()


    def close_db(self):
        self.cursor.close()
        self.connection.close()

    def get_shifts(self): #get shifts from database
        pass
 
    def get_settings(self): #get the settings from database
        pass

    def expected_pay(self):
        total = 0
        for item in self.items:
            if date_compare(item["date"]):
                hours = (int(item["end"][0:2]) - int(item["start"][0:2]))
                total += hours * int(self.payrate)
                if int(item["end"][3:5]) > 0: #for minutes
                    minute_rate = int(self.payrate) / 60
                    minutes = (int(item["end"][3:5]) - int(item["start"][3:5]))
                    if minutes < 0:
                        minutes = minutes + 60
                    total += minutes * minute_rate
        total = total - (total * (int(self.taxrate) / 100))
        return total
        
    def put_shift(self, date, start, end): #add a shift to the database
        pass

    def delete_shift(self, sid): #delete a shift from the database
        pass

    def delete_all_shifts(self):
        pass

    def get_total(self): #calculate the total
        pass



    def put_settings(self, payrate, taxrate): #update the settings
        self.payrate = payrate
        self.taxrate = taxrate


    def put_range(self, startRange, endRange): #update the range
        self.startRange = startRange
        self.endRange = endRange
  

User1 = User() # Create the application instance
User1.create_db() #init the databases if not already created

app = Flask(__name__)
CORS(app)



datedict = {
    "Jan": "01",
    "Feb": "02",
    "Mar": "03",
    "Apr": "04",
    "May": "05",
    "Jun": "06",
    "Jul": "07",
    "Aug": "08",
    "Sep": "09",
    "Oct": "10",
    "Nov": "11",
    "Dec": "12"
}

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

    
@app.route("/api/expectedpay/", methods=["PUT"])
def get_payrange():
    User1.put_range(request.json["startRange"][0:10], request.json["endRange"][0:10])
    return jsonify(startRange=str(User1.startRange), endRange=str(User1.endRange))



def date_compare(date): #date to int conversion before comparing
    newdate = int(date[11:15]) *10000 + int(datedict[date[4:7]])*100 + int(date[8:11])
    startdate = int(User1.startRange[0:4]) *10000 + int(User1.startRange[5:7])*100 + int(User1.startRange[8:10])
    enddate = int(User1.endRange[0:4]) *10000 + int(User1.endRange[5:7])*100 + int(User1.endRange[8:10])
    if newdate >= startdate and newdate <= enddate:
        return True
    else:
        return False


@app.route("/api/expectedpay/", methods=["GET"])
def get_expectedpay(): 
    total = User1.expected_pay()
    return jsonify(expectedpay=str(total))


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
