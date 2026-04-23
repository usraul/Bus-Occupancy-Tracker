from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/bus_data")
def bus_data():
    try:
        with open("gps_data.json") as g:
            gps = json.load(g)

        with open("person_data.json") as p:
            person = json.load(p)

        return jsonify({
            "lat": gps["lat"],
            "lon": gps["lon"],
            "passenger_count": person["person_count"],
            "timestamp": gps["local"],
            "total_seats": 50
        })
    except:
        return jsonify({"error": "no data"})


app.run(host="0.0.0.0", port=5000)
