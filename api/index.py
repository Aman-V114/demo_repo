import json
from http.server import BaseHTTPRequestHandler
from flask import Flask, jsonify, request
import json
import data

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"message": "Hello!"}).encode('utf-8'))
        return

app = Flask(__name__)

dictionary=dict()


with open('data.json', 'r') as file:
    data_dict = json.load(file)


@app.route('/api', methods=['GET'])
def get_data():

    X=request.args.getlist('name')

    marks1=data.data_dict[X[0]]
    marks2=data.data_dict[X[1]]



    return jsonify({'marks': [marks1,marks2]})


if __name__ == '__main__':
    app.run(debug=True)
