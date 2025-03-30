f = open('input.txt', 'r')
a = [int(i) for i in f.readline().split()]
answer = 1
for i in range(10):
    answer *= a[i]
f = open('output.txt', 'w')
f.write(str(answer))