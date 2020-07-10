from flask import Flask, render_template, request, jsonify, redirect
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)

@app.route('/',methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        try:
            user_message = request.get_json()
            # user_message = json.dumps(user_message)

            print("User messge: {}".format(user_message))
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            response = requests.post("http://rasa_server:5005/webhooks/rest/webhook", json = user_message, headers = headers)
            print("Something filled1111")
            return jsonify({"status":"success","response":json.loads(response.content.decode())})
        except Exception as e:
            print(e)
            return jsonify({"status":"success","response":"Sorry I am not trained to do that yet..."})       


    return render_template('index.html')

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
