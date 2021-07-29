# c095
import math
N, M = map(int, input().split())

#リストAにappend()を使って格納していく
A = [int(input()) for _ in range(N)]
             
for s in A:
  M-=s
  
num=math.floor(M/min(A))
print(num+N)