a = input('Введите список: ').split()
a = [int(a[i]) for i in range(len(a))]
mx = a.index(max(a))
mn = a.index(min(a))
a[mx], a[mn] = a[mn], a[mx]
print(a)