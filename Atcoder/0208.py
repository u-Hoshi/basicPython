# abc237

n = int(input())
limit = 2 ** 31
if -limit <= n < limit:
    print("Yes")
else:
    print("No")


n, m = map(int, input().split())
a = [[int(i) for i in input().split()] for _ in range(n)]
b = [[0] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        b[i][j] = a[j][i]
for i in b:
    print(*i)
