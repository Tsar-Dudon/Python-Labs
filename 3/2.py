a = input('Введите первый список: ').split()
b = input('Введите второй список: ').split()
a = [int(i) for i in a]
b = [int(i) for i in b]
c = set()
for i in a:
  if i in b:
    c.add(i)
print(len(c))