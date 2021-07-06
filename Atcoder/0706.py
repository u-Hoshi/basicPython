# C208
  # B問題
from math import perm
 
p = int(input())
A = list(map(perm, range(10, 0, -1)))
coins = 0
r = p
for a in A:
    q, r = divmod(r, a)
    coins += q
print(coins)