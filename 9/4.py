import numpy as np
x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0]) 
values = []
for i in range(1, len(x)):
    if x[i-1] == 0:
        values.append(x[i])
print(max(values))