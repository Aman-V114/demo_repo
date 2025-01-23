import json
dictionary=dict()

with open('data.json', 'r') as file:
    data_list = json.load(file)

data_dict=dict()

for l in data_list:
    
    data_dict[l['name']]=l['marks']

#https://tdsassignment-e0ryggrpm-aman-dhols-projects.vercel.app/?name=EqUei16&name=R9t28iF