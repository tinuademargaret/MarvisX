from src.app import app, socketio, emit
import requests
import ast


class Controller:
    def get_bible(self, passage):
        print('I got here 5')
        response = requests.get(
            "https://bible-api.com/{passage}".format(passage=passage))
        print(response)
        return response.json()

    def search(self, query):
        pass

    def run(self, message):
        print("Received message: {}".format(message))
        if message.get('action') == "openBible":
            data = self.get_bible(message.get('query'))
            print("data retrieved: ", data)
            socketio.emit("result", {"data": data}, namespace="/marvis")
        elif message.get('action') == "search":
            data = self.search(message.get('query'))
            print("data retrieved 2: ", data)
            socketio.emit("result", {"data": data}, namespace="/marvis")

