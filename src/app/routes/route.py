from src.app.controllers.controller import *
from flask import render_template, request, jsonify
controller_ins = Controller()


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/callback", methods=['POST'])
def notification():
    msg = request.get_json()
    if not msg:
        return "Invalid data", 400
    print("processing message: ", msg)
    controller_ins.run(msg)
    return "success", 200


@socketio.on('connect', namespace='/marvis')
def test_connect():
    print('Client connected')









