# C085 B問題
from collections import Counter

s = int(input()) 
# リスト内包表記
A = [int(input()) for _ in range(s)]
num=0

c = collections.Counter(A)


# 出力
print(num)
print(A)

# pythonのcollectionsというライブラリーを誤解してしまった。
# これはローカルにインストールしないと使えないもの！

# 解答
N = int(input())
d = [input() for i in range(N)]
print(len(set(d)))