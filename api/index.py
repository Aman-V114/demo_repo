import json
from http.server import BaseHTTPRequestHandler
from flask import Flask, jsonify, request
import json
from flask_cors import CORS
dictionary=dict()

with open('data.json', 'r') as file:
    data_list = json.load(file)

data_dict=dict()

for l in data_list:
    
    data_dict[l['name']]=l['marks']


app = Flask(__name__)
CORS(app)

@app.route('/api', methods=['GET'])
def get_data():

    
    X=request.args.getlist('name')
    marks=list()
    
    for x in X:
        
        if(x not in X.keys()):
            marks.append(data_dict[x])

    return jsonify({'marks': marks})

@app.route('/', methods=['GET'])
def home():


    return jsonify({'location': "index page"})



if __name__ == '__main__':
    app.run(debug=True)
