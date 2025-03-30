f = open('input.txt', 'r')
b = []
for i in range(10):
    b.append(int(f.readline()))
b.sort()
f = open('output.txt', 'w')
for i in range(10):
    f.write(str(b[i]) + '\n')
print(b)