a = input('Введите элементы списка: ').split()
a = [int(i) for i in a]
b = [a[0]]
for i in range(1, len(a)):
    if a[i] > a[i-1]:
        b.append(a[i])
print(b)