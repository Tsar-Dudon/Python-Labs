n=int(input('Введите число рядов: '))
k = n
stroka = ''
for i in range(n):
    for j in range(1, k+1):
        stroka += str(j)
    print(stroka)
    k -= 1
    stroka = ''