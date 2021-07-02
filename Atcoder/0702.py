# C205 B問題
n = int(input())
list_a = list(map(int, input().split()))
list_a.sort()
ans = "Yes"
for i in range(n):
    if list_a[i] != i + 1:
        ans="No"
print(ans)