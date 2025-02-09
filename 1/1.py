a = int(input('Введите число 1: '))
b = int(input('Введите число 2: '))
c = int(input('Введите число 3: '))
mx = a
mn = a

if b > mx:
    mx = b
elif b < mn:
    mn = b

if c > mx:
    mx = c
elif c < mn:
    mn = c
print('Максимальное число:', mx)
print('Минимальное число:', mn)