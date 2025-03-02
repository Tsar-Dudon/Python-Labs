a =['abc', 'abc', 'abc']
strings = dict()
for i in a:
    if i not in strings.keys():
        strings[i] = 1
    else:
        strings[i] += 1
print(*strings.values())