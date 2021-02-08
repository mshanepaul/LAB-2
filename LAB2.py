from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# database
Profile_db = {
        "success": True,
        "data": {
            "last_updated": "2/3/2021, 8:48:51 PM",
            "username": "user_",
            "role": "Engineer",
            "color": "red"
        }
    }

Tank_d = []
MaxId = 0

@app.route("/")
def home():
    return "ECSE3038 - Lab 2"

# Returns all data in the database
@app.route("/profile", methods=["GET", "POST", "PATCH"])
def get_profile():
    if request.method == "GET":
        return jsonify(PROFILE_DB)

    elif request.method == "POST":
        
        # Get the current date and time
        now = datetime.now()
        dt = now.strftime("%d/%m/%Y %H:%M:%S")

        Profile_db["data"]["last_updated"] = (dt)
        Profile_db["data"]["username"] = (request.json["username"])
        Profile_db["data"]["role"] = (request.json["role"])
        Profile_db["data"]["color"] = (request.json["color"])

        return jsonify(Profile_db)

    elif request.method == "PATCH":
        
        # Get the current date and time
        now = datetime.now()
        dt = now.strftime("%d/%m/%Y %H:%M:%S")
    
        data = Profile_db["data"]

        r = request.json
        r["last_updated"] = dt
        attributes = r.keys()
        for attribute in attributes:
            data[attribute] = r[attribute]

        return jsonify(Profile_db)    



# Returns all data in Tank_d
@app.route("/data", methods=["GET", "POST"])
def tank_data():
    if request.method == "GET":
        return jsonify(Tank_d)  

    elif request.method == "POST":
        global max_id

        MaxId += 1

        r = request.json
        r["id"] = max_id
        Tank_d.append(r)
        return jsonify(Tank_d)
   
 
@app.route('/data/<int:id>', methods=["PATCH", "DELETE"])
def tank_id_methods(id):
    if request.method == "PATCH":
        for i in Tank_d:
            if i["id"] == id:
                r = request.json
                attributes = r.keys()

                for attribute in attributes:
                    i[attribute] = r[attribute]

        return jsonify(Tank_d)
    
    elif request.method == "DELETE":
        for i in Tank_d:
            if i["id"] == id:
                Tank_d.remove(i)

        return jsonify(Tank_d)

    
if __name__ == "__main__":
    app.run(
       debug=True,
       port = 3000
    )
