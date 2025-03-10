a = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}
b = input('Введите значение: ')
c = None
for i in a.keys():
    if str(a[i]) == b:
        c = i
print(c)