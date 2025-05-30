import numpy as np
x = np.array([2, 2, 2, 3, 3, 3, 5])
c = 0
values = [x[0]]
howMany = [1]
for i in range(1, len(x)):
    if x[i] == values[c]:
        howMany[c] += 1
    else:
        values.append(x[i])
        howMany.append(1)
        c += 1
print((np.array(values), np.array(howMany)))