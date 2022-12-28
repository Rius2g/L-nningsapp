#! flask/bin/python3
from flask import Flask, jsonify, abort, make_response, request
from flask_cors import CORS
import time
from random import random
import sqlite3
from datetime import datetime
import json

class User:

    def __init__(self): #settings in the top
        self.payrate = 1
        self.taxrate = 1

        self.items = []#array for shifts
        self.rules = []
        self.startRange = datetime.now().strftime("%Y-%m-%d")
        self.endRange = datetime.now().strftime("%Y-%m-%d")
        self.Uid = 1


    def create_db(self): #create two tables for shifts and settings
        self.connection = sqlite3.connect("shifts.db", check_same_thread=False) #connect to the database
        self.cursor = self.connection.cursor() #create a cursor
        sql_command = """ CREATE TABLE IF NOT EXISTS shifts ( 
                Sid INTEGER PRIMARY KEY,
                Uid INTEGER NOT NULL,
                Date INTEGER(255) NOT NULL,
                Start varchar(255) NOT NULL,
                End varchar(255) NOT NULL);"""

        sql_command2 = """ CREATE TABLE IF NOT EXISTS users ( 
                Uid INTEGER PRIMARY KEY,
                Payrate INTEGER NOT NULL,
                Taxrate INTEGER NOT NULL,
                Name varchar(255),
                FOREIGN KEY (Uid) REFERENCES shifts(uid));"""


        sql_command3 = """ CREATE TABLE IF NOT EXISTS rules (
                Rid INTEGER PRIMARY KEY,
                Uid INTEGER NOT NULL,
                type varchar(255) NOT NULL,
                value varchar(255) NOT NULL,
                increaseType varchar(255) NOT NULL,
                increaseValue varchar(255) NOT NULL;"""


            #shift id, user id, date, start time, end time
        self.cursor.execute(sql_command) #create the shifts table
        self.cursor.execute(sql_command2) #create the user/settings table with foreign key uid
        self.cursor.execute(sql_command3) #create the user/settings table with foreign key uid
        self.connection.commit()
        self.cursor.close()


    def close_db(self):
        self.cursor.close()
        self.connection.close()

    def get_certain_shifts(self): #get shifts from database
        self.cursor = self.connection.cursor()
        sql_comand = """SELECT * FROM shifts
        WHERE (?) <= Date AND (?) >= Date; """
        self.cursor.execute(sql_comand, (self.range_convert(self.startRange), self.range_convert(self.endRange)))
        shifts = self.cursor.fetchall()
        self.connection.commit()
        self.cursor.close()
        if shifts == []:
            return []
        else:
            return shifts


    def add_rule(self, id, type, value, increaseType, increaseValue):
        self.cursor = self.connection.cursor()
        sql_command = """INSERT INTO rules
        (Rid, Uid, type, value, increaseType, increaseValue)
        VALUES (?, ?, ?, ?, ?);"""
        data = (id, self.Uid, type, value, increaseType, increaseValue)
        self.cursor.execute(sql_command, data)
        self.connection.commit()
        self.cursor.close()


    def get_rules(self):
        self.cursor = self.connection.cursor()
        sql_comand = """SELECT * FROM rules
        WHERE Uid = (?);"""
        self.cursor.execute(sql_comand, self.Uid) #get all the rules for the current user
        rules = self.cursor.fetchall()
        self.connection.commit()
        self.cursor.close()
        if rules == []:
            self.rules = []
        else:
            self.rules = rules



    def get_all_shifts(self):
        self.cursor = self.connection.cursor()
        sql_comand = """SELECT * FROM shifts"""
        self.cursor.execute(sql_comand)
        shifts = self.cursor.fetchall()
        self.connection.commit()
        self.cursor.close()
        if shifts == []:
            return []
        else:
            return shifts
            

    def create_shifts(self, bool):
        shift_list = []
        shifts = []
        if bool == 1:
            shifts = self.get_all_shifts()
        else:
            shift = self.get_certain_shifts()
        for shift in shifts:
            shift_list.append({"id": shift[0], "date": self.convert_date(shift[2]), "start": shift[3], "end": shift[4]})
        self.items = shift_list
        
 
    def get_settings(self): #get the settings from database
        self.cursor = self.connection.cursor()
        sql_command = """SELECT * FROM users;"""
        settings = self.cursor.fetchall()
        self.connection.commit()
        self.cursor.close()


        
    def add_shift(self, sid, date, start, end): #add a shift to the database
        self.cursor = self.connection.cursor()
        sql_command = """INSERT INTO shifts 
        (Sid, Uid, Date, Start, End) 
        VALUES (?, ?, ?, ?, ?);"""
        newdate = int(date[6:10]) *10000 + int(date[3:5])*100 + int(date[0:2])
        data = (sid, self.Uid, newdate, start, end)
        self.cursor.execute(sql_command, data)
        self.connection.commit()
        self.cursor.close()


    def delete_shift(self, sid): #delete a shift from the database given that the shift belongs to the current user
        self.cursor = self.connection.cursor()
        sql_commmand = """DELETE * FROM shifts WHERE sid = (?);"""
        self.cursor.execute(sql_commmand, sid)
        self.connection.commit()
        self.cursor.close()
        

    def delete_all_shifts(self):
        self.items = [] #set as empty array
        self.cursor = self.connection.cursor()
        sql_commmand = """DELETE FROM shifts;"""
        self.cursor.execute(sql_commmand)
        self.connection.commit()
        self.cursor.close()


    def put_settings(self, payrate, taxrate): #update the settings
        self.payrate = payrate
        self.taxrate = taxrate


    def put_range(self, startRange, endRange): #update the range
        self.startRange = startRange
        self.endRange = endRange

    def range_convert(self, date):
        return int(date[0:4]) *10000 + int(date[5:7])*100 + int(date[8:10])


    def convert_date(self, date):
        date = str(date)
        return str(date[6:8]) + "/" + str(date[4:6]) + "/" + str(date[0:4])
  

User1 = User() # Create the application instance
User1.create_db() #init the databases if not already created

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


@app.route("/api/items/", methods=["GET"]) #get all shifts
def get_items(): 
    User1.create_shifts(1)
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


@app.route("/api/rules/", methods=["POST"])
def post_rule():
    if not request.json:
        abort(400, "Must be JSON.")
    if "value" not in request.json:
        abort(400, "Must contain 'value'-field.")
    if not isinstance(request.json["value"], str):
        description = f"'value'-field must be str."
        abort(400, description)
    new_id = 0 if not User1.rules else max(rule["id"] for rule in User1.rules) + 1
    User1.add_rule(new_id, request.json["type"], request.json["increaseType"], request.json["value"])
    rule = {"id": new_id, "type": request.json["type"], "increaseType": request.json["increaseType"], "value": request.json["value"]}
    User1.rules.append(rule)
    return jsonify({"rules": User1.rules}), 201



def date_compare(date): #date to int conversion before comparing
    newdate = int(date[11:15])*10000 + int(date[4:7])*100 + int(date[8:11])
    startdate = int(User1.startRange[0:4]) *10000 + int(User1.startRange[5:7])*100 + int(User1.startRange[8:10])
    enddate = int(User1.endRange[0:4]) *10000 + int(User1.endRange[5:7])*100 + int(User1.endRange[8:10])
    if newdate >= startdate and newdate <= enddate:
        return True
    else:
        return False



def time_extra(time_Ex, timeend):
       hours_ex = timeend - time_Ex
       return hours_ex

def time_compare(time1, timestart):
    if time1 >= timestart:
        return True


def day_compare(day1, day2):
    if day1 == day2:
        return True
    else:
        return False



def rules_extra(shift):
    for rules in User1.rules:
        if rules["type"] == "0":
            if day_compare(rules["value"], shift["day"]) == True: #check if the day is in the range
                if rules["increaseType"] == "%":
                    User1.payrate = (int(User1.payrate) * (1 + int(rules["increaseValue"]))) #add the % to the payrate
                else:
                    User1.payrate = int(User1.payrate) + int(rules["increaseValue"]) #add the amount in nok
        elif rules["type"] == "1":
            if time_compare(rules["value"], shift["start"]) == True:
                if rules["increaseType"] == "%":
                    extra = (int(User1.payrate) * (1 + int(rules["increaseValue"])) - int(User1.payrate)) * time_extra(rules["value"], shift["end"])
                else:
                    extra = int(rules["increaseValue"]) * time_extra(rules["value"], shift["end"])
        else: #rules["type"] == "2": day and time
            if day_compare(rules["value"], shift["day"]) == True and time_compare(rules["value"], shift["start"]) == True:
                if rules["increaseType"] == "%":
                    extra = (int(User1.payrate) * (1 + int(rules["increaseValue"])) - int(User1.payrate)) * time_extra(rules["value"], shift["end"])
                else:
                    extra = int(rules["increaseValue"]) * time_extra(rules["value"], shift["end"]) #increase val * hours with exra pay

    return extra



@app.route("/api/expectedpay/", methods=["GET"])
def get_expectedpay(): 
    total = 0
    User1.create_shifts(0) #get shifts in range
    for item in User1.items:
        if date_compare(item["date"]) == True:
            hours = (int(item["end"][0:2]) - int(item["start"][0:2]))
            total += hours * int(User1.payrate)
            if int(item["end"][3:5]) > 0: #for minutes
                minute_rate = int(User1.payrate) / 60
                minutes = (int(item["end"][3:5]) - int(item["start"][3:5]))
                if minutes < 0:
                    minutes = minutes + 60
                total += minutes * minute_rate
    total = total - (total * (int(User1.taxrate) / 100))
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
    User1.add_shift(new_id, request.json["date"], request.json["start"], request.json["end"])
    item = {"id": new_id, "date": request.json["date"], "start": request.json["start"], "end": request.json["end"]}
    User1.items.append(item)
    return jsonify({"items": User1.items}), 201



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


@app.route("/api/items/", methods=["DELETE"]) #deletes all
def delete_item():
    User1.delete_all_shifts()
    return jsonify({"deleted": True})


if __name__ == "__main__":
    app.run(debug=True)
