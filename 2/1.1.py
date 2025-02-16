a = input('Введите строку: ')
a += '*'
letters = 'abcdefghijklmnopqrstuvwxyzABCEFGHIJKLMNOPQRSTUVWXYZ*'
stroka = ''
for i in range(len(a)-1):
    if a[i+1] not in letters:
        stroka += (int(a[i+1]) * a[i])
    elif a[i] in letters:
      stroka += a[i]
print(stroka)