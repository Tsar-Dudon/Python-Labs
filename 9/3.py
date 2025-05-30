
import numpy as np

data = np.random.randn(10, 4)
mn = np.min(data)
mx = np.max(data)
mean = np.mean(data)
std = np.std(data)
fiveRows = data[:5]

print("Минимальное значение:", mn)
print("Максимальное значение:", mx)
print("Среднее значение:", mean)
print("Стандартное отклонение:", std)
print("Первые 5 строк:\n", fiveRows)