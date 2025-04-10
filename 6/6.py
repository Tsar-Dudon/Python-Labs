import json
import csv
a = input('Введите имя json файла: ')
with open(a,'r') as f:
    jsf = json.load(f)
    name = list(jsf.keys())[0]
    headers = jsf[name][0].keys()
with open((name + '.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)  # Записываем заголовки
    for row in jsf[name]:
        writer.writerow((row.values()))
