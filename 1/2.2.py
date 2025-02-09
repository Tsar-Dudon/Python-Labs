n=int(input('Введите число рядов: '))
k = n
stroka = ''
for i in range(n):
    stroka += ' ' * (n - k)
    for j in range(k, 0, -1):
        stroka += str(j)
    for j in range(2, k+1):
        stroka += str(j)
    print(stroka)
    stroka = ''
    k -= 1