import json
from http.server import BaseHTTPRequestHandler
from flask import Flask, jsonify, request
import json

dictionary=dict()

with open('data.json', 'r') as file:
    data_list = json.load(file)

data_dict=dict()

for l in data_list:
    
    data_dict[l['name']]=l['marks']

class handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"message": "Hello!"}).encode('utf-8'))
        return


app = Flask(__name__)


@app.route('/api', methods=['GET'])
def get_data():

    X=request.args.getlist('name')

    marks1=data_dict[X[0]]
    marks2=data_dict[X[1]]

    return jsonify({'marks': [marks1,marks2]})

@app.route('/', methods=['GET'])
def home():


    return jsonify({'location': "index page"})



if __name__ == '__main__':
    app.run(debug=True)
