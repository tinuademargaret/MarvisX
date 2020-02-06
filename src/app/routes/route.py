from src.app import *
from src.app.controllers.controller import *
from flask import render_template
controller = Controller()

@app.route("/index")
def index():
    render_template("index.html")


@socketio.on('connect', namespace='/marvis')
def test_connect():
    print('Client connected')
    controller.run()


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', debug=True, port=port)

