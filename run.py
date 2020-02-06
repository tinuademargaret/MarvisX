import os
from src.app import app
from src.app.routes.route import *
from src.app.controllers.controller import *
from src.app.services.consumer import *


if __name__ == '__main__':
    socketio.run(app, debug=True)