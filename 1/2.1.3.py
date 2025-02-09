n=int(input('Введите число рядов: '))
k = n
stroka = ''
skeeps = ''
for i in range(n):
    skeeps += ' ' * (len(str(k+1)) - 1)
    stroka += skeeps
    for j in range(1, k+1):
        stroka += str(j)
    print(stroka)
    k -= 1
    stroka = ''