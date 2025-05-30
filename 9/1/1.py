import numpy as np
import csv

path = '1\matrix.csv'
with open(path) as f:
    reader = csv.reader(f)
    data = [i for i in reader]

a = np.array(data)
a = a.astype(int)
print('Сумма элементов:', a.sum())
print('Наименьший элемент:', a.min())
print('Наибольший элемент:', a.max())