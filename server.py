#! flask/bin/python3
from flask import Flask, jsonify, abort, make_response, request
from flask_cors import CORS
from User import User


User1 = User() # Create the application instance
User1.create_db()


app = Flask(__name__)
CORS(app)

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



@app.route("/api/rules/", methods=["GET"])
def return_rules():
    User1.get_rules()
    return jsonify({"rules": User1.rules}), 200



@app.route("/api/rules/", methods=["POST"])
def post_rule():
    if not request.json:
        abort(400, "Must be JSON.")
    if "value" not in request.json:
        abort(400, "Must contain 'value'-field.")
    User1.delete_certain_rule()
    new_id = User1.get_largest_rule_id() + 1
    User1.add_rule(request.json["type"], request.json["typeVal"], request.json["increaseType"], request.json["value"])
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


def time_extra(time_Ex, timeend): #calculate the extra hours
    time_ext = timeend[:2] - time_Ex[:2]
    if time_ext < 0:
        time_ext = 24 + time_ext
    return time_ext


def minutes_extra(timeend, time_ex):
    minutes_extra = timeend[2:] - time_ex[2:]
    if minutes_extra < 0:
        minutes_extra = 60 + minutes_extra
    return minutes_extra
    

def time_compare(time1, timestart):
    if time1 >= timestart:
        return True


def day_compare(day1, day2):
    if day1 == day2:
        return True
    else:
        return False



def rules_extra(shift): #iterate through the rules and check if the shift is in the range for extra pay
    extra_hours = 0
    extra_minutes = 0
    for rules in User1.rules:
        if rules["type"] == "0":
            if day_compare(rules["value"], shift["day"]) == True: #check if the day is in the range
                if rules["increaseType"] == "%":
                    extra_hours = (int(User1.payrate) * (1 + int(rules["increaseValue"]))) * time_extra(shift["end"], rules["value"])#add the % to the payrate
                    extra_minutes = (int(User1.payrate) * (1 + int(rules["increaseValue"]))) * minutes_extra(shift["end"], rules["value"]) / 60
                else:
                    extra_hours =  int(rules["increaseValue"]) * time_extra(shift["end"], rules["value"])#add the % to the payrate
                    extra_minutes = int(rules["increaseValue"]) * minutes_extra(shift["end"], rules["value"]) / 60 #add the amount in nok
        elif rules["type"] == "1":
            if time_compare(rules["value"], shift["start"]) == True:
                if rules["increaseType"] == "%":
                    extra_hours = (int(User1.payrate) * (1 + int(rules["increaseValue"]))) * time_extra(shift["end"], rules["value"])#add the % to the payrate
                    extra_minutes = (int(User1.payrate) * (1 + int(rules["increaseValue"]))) * minutes_extra(shift["end"], rules["value"]) / 60
                else:
                    extra_hours =  int(rules["increaseValue"]) * time_extra(shift["end"], rules["value"])#add the % to the payrate
                    extra_minutes = int(rules["increaseValue"]) * minutes_extra(shift["end"], rules["value"]) / 60 #add the amount in nok
        else: #rules["type"] == "2": day and time
            if day_compare(rules["value"], shift["day"]) == True and time_compare(rules["value"], shift["start"]) == True:
                if rules["increaseType"] == "%":
                    extra_hours = (int(User1.payrate) * (1 + int(rules["increaseValue"]))) * time_extra(shift["end"], rules["value"])#add the % to the payrate
                    extra_minutes = (int(User1.payrate) * (1 + int(rules["increaseValue"]))) * minutes_extra(shift["end"], rules["value"]) / 60
                else:
                    extra_hours =  int(rules["increaseValue"]) * time_extra(shift["end"], rules["value"])#add the % to the payrate
                    extra_minutes = int(rules["increaseValue"]) * minutes_extra(shift["end"], rules["value"]) / 60 #add the amount in nok

    return extra_hours + extra_minutes



@app.route("/api/expectedpay/", methods=["GET"])
def get_expectedpay(): 
    extra = 0
    total = 0
    User1.create_shifts(0) #get shifts in range
    for item in User1.items:
        if date_compare(item["date"]) == True:
            extra = rules_extra(item)
            hours = (int(item["end"][0:2]) - int(item["start"][0:2]))
            total += hours * int(User1.payrate)
            if int(item["end"][3:5]) > 0: #for minutes
                minute_rate = int(User1.payrate) / 60
                minutes = (int(item["end"][3:5]) - int(item["start"][3:5]))
                if minutes < 0:
                    minutes = minutes + 60
                total += minutes * minute_rate
    total = total - (total * (int(User1.taxrate) / 100)) + extra
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
    User1.add_shift(new_id, request.json["date"], request.json["workday"], request.json["start"], request.json["end"])
    item = {"id": new_id, "date": request.json["date"], "day": request.json["workday"], "start": request.json["start"], "end": request.json["end"]}
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


@app.route("/api/items/<int:item_id>", methods=["DELETE"])
def delete_specific_shift():
    id = request.json["id"]
    User1.delete_shift(id)
    return jsonify({"deleted": True})


if __name__ == "__main__":
    app.run(debug=True)
