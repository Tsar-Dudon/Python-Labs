import json
with open('task 2\ex_2(corrected).json', 'r') as f:
    data = json.load(f)
d = dict()
for i in range(len(data)):
    d[data[i]["name"]] = data[i]["phoneNumber"]
print(d)