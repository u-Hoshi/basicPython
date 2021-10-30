# abc225

# A問題
l = len(set(input())) 
# setで重複しない要素を並べる
# その後lenで並んでいる要素数を数える
# １種類だったら1通り例(222) 2種類なら3通り 例(223 232 322)
# 3種類だったら6通り (234 243 324 342 432 423)
if l == 1:
  print(1)
elif l == 2:
  print(3)
else:
  print(6)

# A問題 別解
import itertools
 
s = input()
x = []
ans = 0
p = list(itertools.permutations(s)) 
# itertoolsで数字の重複でも全ての要素の組み合わせを列挙
for i in p:
  if i not in x:
    # xに存在しなかったらxに文字を追加してカウントを+1する
    x.append(i)
    ans = ans + 1
 
print(ans)

# B問題
N = int(input())
l = [list(map(int, input().split())) for l in range(N)]

