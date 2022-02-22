a = list(map(int, input().split()))

# print(a, ' a')
a.sort()

if a[1] - a[0] == 1 or (a[0] == 1 and a[1] == 10):
    print("Yes")
else:
    print("No")

# B
n = int(input())

a = list(map(int, input().split()))
a = list(set(a))

print(len(a))
