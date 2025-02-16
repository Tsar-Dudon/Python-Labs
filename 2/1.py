a = input('Введите строку: ')
a += '*'
count = 0
stroka = ''
for i in range(len(a) - 1):
    count += 1
    if a[i+1] != a[i]:
        if count == 1:
            stroka += a[i]
        else:
            stroka = stroka + a[i] + str(count)
        count = 0
print(stroka)