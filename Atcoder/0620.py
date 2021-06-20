# C088
  # B問題

s = int(input()) 
x = list(map(int, input().split()))

Alice=0
Bob=0

newlist = sorted(x,reverse=True) # 大きい順に並び替え

for r in range(s):
  if r%2==1:
    Bob+=newlist[r]
  else:
    Alice+=newlist[r]
print(Alice-Bob)

# 別解 スライスを用いる
N = int(input())
a = sorted(map(int, input().split()))[::-1]
print(sum(a[::2])-sum(a[1::2]))

# [::2]について
s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = s[::2]  # 偶数
odd = s[1::2]  # 奇数
print(even)
print(odd)