n=int(input('Введите число строк: '))
triangle = []
for i in range(n):
    triangle.append([1] + [0]*n)
for i in range(1, n):
    for j in range(1, i+1):
        triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j] 
for i in range(n):
    for j in range(i+1):
        print(triangle[i][j], end=' ')
    print()