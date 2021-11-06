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
# 最初の回答 WAになる
N = int(input())-1
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]

ans=len(set(x))

if ans==N:
  print("Yes")
else:
  print("No")

# 別解
import sys
input = sys.stdin.readline
N = int(input())
l = [0]*N
for _ in range(N-1):
    a,b = map(int,input().split()) # それぞれの頂点からいくつ線が出ているかを確認
    l[a-1] += 1
    l[b-1] += 1
if max(l) == N-1: # ここでいう星とは一つの頂点から他の全ての頂点に向けて線が伸びている状態
                  # →頂点の数-1であれば星だと言える
    print("Yes")
else:
    print("No")

# 別解
N = int(input())
ab = [map(int, input().split()) for _ in range(N-1)]
a, b = [list(i) for i in zip(*ab)]
 
res = [0 for _ in range(N)]
 
for i in range(N-1):
    res[a[i]-1] +=1
    res[b[i]-1] +=1
    
for i in range(N):
    if res[i] == N-1:
        print("Yes")
        break
    
    elif i == N-1:
        print("No")