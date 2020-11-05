import json

json.dumps([1,2,3])

json.loads('[1,2,3]')

with open('c:/Users/Natalia/Desktop/CourseraPython/2/json_example.txt','w') as a_file:
    json.dump([1,2,3,4], a_file)

with open('c:/Users/Natalia/Desktop/CourseraPython/2/json_example.txt','r') as a_file:
    a_list = json.load(a_file)

