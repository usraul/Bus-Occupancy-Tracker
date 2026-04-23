from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

# 🔹 Route 1 — Serve HTML page
@app.route("/")
def home():
    return render_template("index.html")

# 🔹 Route 2 — Send live data (JSON)
@app.route("/data")
def get_data():
    try:
        with open("gps_data.json") as g:
            gps = json.load(g)
        with open("person_data.json") as p:
            person = json.load(p)

        return jsonify({
            "lat": gps["lat"],
            "lon": gps["lon"],
            "count": person["person_count"],
            "utc": gps["utc"],
            "local": gps["local"]
        })
    except:
        return jsonify({"error": "No data"})

# 🔹 Start server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
