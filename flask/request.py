from flask import Flask,jsonify,request,make_response
import requests
from flask_restful import Api
from flask_cors import CORS
import json

app=Flask(__name__)
api = Api(app)
CORS(app)

@app.route('/',methods=['GET', 'POST']) #end point is chat

def post():
	json1 = request.get_json() #it will take the request in json format and storing in json

	print("JSON Data: {}".format(json1))
	json.dumps(json1)
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	r = requests.post("http://rasa_server:5005/webhooks/rest/webhook", json=json1,headers=headers) #geting the response and stored in r by using the data in json
	return r.json()[0] 


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
