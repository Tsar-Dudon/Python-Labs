a = {0 : 0, 1 : 0, 2 : 0, 3 : 0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
b = input('Введите строку: ')
c = {}
mxv = -1
mxk = None
for i in b:
    a[int(i)] += 1
for i in range(3):
    for j in a.keys():
        if (j not in c.keys()) and (mxv < a[j]):
            mxv = a[j]
            mxk = j
    c[mxk] = mxv
    mxv = -1
    mxk = None
print(c)