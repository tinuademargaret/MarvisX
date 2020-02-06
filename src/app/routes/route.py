from src.app.controllers.controller import *
from flask import render_template
from src.app.services.consumer import consumer


@app.route("/index")
def index():
    return render_template("index.html")


@socketio.on('connect', namespace='/marvis')
def test_connect():
    print('Client connected')
    consumer()




