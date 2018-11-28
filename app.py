#!/usr/bin/python3
import flask
import sqlite3
from flask import request, jsonify, render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")


@app.route('/last', methods=['GET'])
def last_measurement():
    con = sqlite3.connect('pms.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    query = cur.execute("SELECT * FROM pms ORDER BY id DESC LIMIT 1").fetchone()

    data = {
        'ts' : query['timestamp'],
        'temperature': query['temperature'],
        'soil_moisture' : query['soil_moisture'],
        'light_intensity': query['light_intensity'],
        'air_humidity': query['air_humidity'],
    }

    return jsonify(data)

app.run()