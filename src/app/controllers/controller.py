from src.app import app, socketio, emit
# from flask import jsonify
import requests
import ast
# from src.app.services.consumer import consumer



class Controller:

    def get_bible(self, passage):
        print('I got here 5')
        response = requests.get(
            "https://bible-api.com/{passage}".format(passage=passage))
        print(response)
        return response.json()
        # f = open('/home/tinuade/PycharmProject/project_marvis/app/templates/bible.html', "w+")
        # f.write(response.text)
        # f.close()

    def search(self, query):
        pass

    def run(self, message):
        print("Received message: {}".format(message))
        # Messages.append(message.data)
        # message.ack()
        # message = message.data
        # message = ast.literal_eval(message.decode('utf-8'))
        # message = ast.literal_eval(message)
        if message.get('action') == "openBible":
            data = self.get_bible(message.get('query'))
            print("data retrieved: ", data)
            socketio.emit("result", {"data": data}, namespace="/marvis")
        elif message.get('action') == "search":
            data = self.search(message.get('query'))
            print("data retrieved 2: ", data)
            socketio.emit("result", {"data": data}, namespace="/marvis")

