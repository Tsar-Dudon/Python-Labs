import numpy as np
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
species = iris[:, 4]
unique_species, counts = np.unique(species, return_counts=True)
d = dict()
for i in range(len(unique_species)):
    d[unique_species[i]] = counts[i]
for i in d:
    print(i, ':', d[i])