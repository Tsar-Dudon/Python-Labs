import json

with open('task 3\ex_3.json', 'r') as f:
    data = json.load(f)

k = data["invoices"]

object = {
    "id": 3,
    "total": 150.00,
    "items": [
    {
        "name": "Temmy flakes",
        "quantity": 16,
        "price": 99.99
    }
    ]
}

k.append(object)
d = dict()
d["invoices"] = k

with open('task 3\ex_3(new).json', 'w') as f:
    json.dump(d, f,ensure_ascii=False, indent=2)