from flask import Flask, render_template, url_for, abort, redirect ,request, jsonify
import random
app = Flask(__name__)
@app.route('/ev_charging_station', methods=['GET'])
def ev_charging_station():
    lat = round(random.uniform(-90, 90), 6)
    lon = round(random.uniform(-180, 180), 6)
    capacity = random.randint(1, 6)
    data = {
        "latitude": lat,
        "longitude": lon,
        "capacity": capacity
    }
    return jsonify(data)
