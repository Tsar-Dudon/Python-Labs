import json
from jsonschema import validate, ValidationError

with open('task 1\scheme.json', 'r') as file:
    scheme = json.load(file)

with open('task 1\ex_1.json', 'r') as file:
    data = json.load(file)

with open('task 1\ex_1(incorrect).json', 'r') as file:
    data1 = json.load(file)
 
try:
    validate(instance=data, schema=scheme)
    print("JSON валиден")
except ValidationError as e:
    print("Ошибка валидации:", e.message)

try:
    validate(instance=data1, schema=scheme)
    print("JSON валиден")
except ValidationError as e:
    print("Ошибка валидации:", e.message)