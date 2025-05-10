import csv
import random
import os

def Show(path, typeOfOut = 'top', countOfStrings = 5, *, separator = ','):
    f = open(path)
    reader = csv.reader(f)
    data = [i for i in reader]
    for i in range(len(data[0])-1): #вывод заголовков
        print(data[0][i], end = separator)
    print(data[0][-1])

    if (len(data)-1) < countOfStrings: #если строк слишком мало
        for row in range(1, len(data)):
            for i in range(len(data[row])-1):
                print(data[row][i], end = separator)
            print(data[row][-1])
        print('Слишком мало строк в файле')
        return

    if typeOfOut == 'top':
        for row in range(1, countOfStrings+1):
            for i in range(len(data[row])-1):
                print(data[row][i], end = separator)
            print(data[row][-1])

    elif typeOfOut == 'down':
        for row in range(len(data) - 1,  len(data) - 1 - countOfStrings, -1):
            for i in range(len(data[row])-1):
                print(data[row][i], end = separator)
            print(data[row][-1])

    elif typeOfOut == 'random':
        data1 = random.sample(data[1:], countOfStrings)
        for row in range(len(data1)):
            for i in range(len(data1[row])-1):
                print(data1[row][i], end = separator)
            print(data1[row][-1])
    f.close()

def DelNaN(path):
    f = open(path)
    reader = csv.reader(f)
    data = [i for i in reader]
    for row in data:
        for i in row:
            if i == '':
                data.remove(row)
    f.close()
    f = open(path,'w', newline='')
    writer = csv.writer(f)
    writer.writerows(data)
    print(data)
    f.close()

def MakeDS(path):
    f = open(path)
    reader = csv.reader(f)
    data = [i for i in reader]
    headers = data[0]
    data.remove(headers)
    trainlen = (len(data)*70)//100
    train = []
    for i in range(trainlen):
        a = random.choice(data)
        train.append(a)
        data.remove(a)
    f.close()
    os.mkdir('workdata')
    os.mkdir('workdata/Learning')
    with open('workdata/Learning/train.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(train)
    os.mkdir('workdata/Testing')
    with open('workdata/Testing/test.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)

def Info(path):
    f = open(path)
    reader = csv.reader(f)
    data = [i for i in reader]
    height = len(data) - 1
    length = len(data[0])
    print(str(height) + 'x' + str(length))
    d1 = dict()
    d2 = dict()
    for i in data[0]:
        d1[i] = 0
    for i,j in enumerate(data[0]):
        for row in range(1, len(data)):
            if data[row][i] != '':
                if data[row][i].isdigit():
                    d2[j] = 'int'
                else:
                    try:
                        float(data[row][i])
                        d2[j] = 'float'
                    except ValueError:
                        d2[j] = 'string'
                d1[j] += 1
    for i in d1.keys():
        print(i, d1[i], d2[i])

path = 'weekly-rent-paid-by-household-2018-census-csv.csv'
Info(path)