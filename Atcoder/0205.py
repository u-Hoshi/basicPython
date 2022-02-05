n = int(input())

if 2 ** n > n ** 2:
    print("Yes")
else:
    print("No")

n = input()
arr = map(int, raw_input().split())
arr = [0,] + arr
m = 0
for i in xrange(1, len(arr)):
    arr[i] += arr[i - 1]
    arr[i] = arr[i] % 360

arr = sorted(arr)
for i in xrange(1, len(arr)):
    m = max(m, arr[i] - arr[i - 1])
m = max(m, 360 - arr[-1])


print(m)
