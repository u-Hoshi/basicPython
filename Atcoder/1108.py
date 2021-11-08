# 226
x, y = map(int, input().split('.'))
if y < 500:
    print(x)
else:
    print(x+1)

# B
N = int(input())
a = set()
for _ in range(N):
    b = tuple(map(int,input().split()))
    a.add(b)
 
print(len(a))