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

# 別解で使うバケット法について
  # 便利だが要素の最大値が分からないと使えない
import random

s = int(input()) 
#リスト内包表記
A = [int(input()) for _ in range(s)]
print(A)

def counting(A,max_num):
  count_list=[0]*(max_num+1) # バケットを作成して値を入れる
  
  # 値を数える
  for i in A:
    count_list[i]+=1
  
  # バケツの中身を取り出して結合
  i = 0
  for num in range(len(count_list)):
     for c in range(count_list[num]):
        A[i]=num
        i+=1

  return i
        
counting(A,101)
print(A)
