a = input('Введите строку: ')
letters = []
count = []
for i in range(len(a)):
    if a[i] != ' ':
        if a[i] not in letters:
            letters.append(a[i])
            count.append(1)
        else:
            b = letters.index(a[i])
            count[b] += 1
for i in range(3):
    b = count.index(max(count))
    print('Символ', letters[b], 'встречается', max(count), 'раз')
    count[b] = 0