import numpy as np
a = np.arange(16).reshape(4,4)
for i in range(len(a[1])):
    a[1, i], a[3, i] = a[3, i], a[1, i]
print(a)