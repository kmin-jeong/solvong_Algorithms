n = int(input())
triangle = []
for i in range(n):
    triangle.append(list(map(int, input().split())))
kok = 2
for i in range(1, n):
    for j in range(kok):
        if j == 0:
            triangle[i][j] = triangle[i][j] + triangle[i - 1][j]
        elif i == j:
            triangle[i][j] = triangle[i][j] + triangle[i - 1][j - 1]
        else:
            triangle[i][j] = max(triangle[i - 1][j - 1], triangle[i - 1][j]) + triangle[i][j]
    kok += 1
print(max(triangle[n - 1]))