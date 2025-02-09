n=int(input('Введите число рядов: '))
k = n
stroka = ''
skeeps = ''
for i in range(n):
    if k != n:
        skeeps += ' ' * len(str(k+1))
    stroka += skeeps
    for j in range(k, 0, -1):
        stroka += str(j)
    for j in range(2, k+1):
        stroka += str(j)
    print(stroka)
    stroka = ''
    k -= 1