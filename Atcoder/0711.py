# C209 B問題

n,x = map(int,input().split())
a = list(map(int,input().split()))
 
print("Yes" if sum(a)-(n//2)<=x else "No")

# A問題
A, B = map(int, input().split())
ans = 0
 
for i in range(A, B + 1):
  if A <= i <= B + 1:
    ans += 1
 
print(ans)