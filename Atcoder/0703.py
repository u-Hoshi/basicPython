# C072 B問題

s = input() 
l=list(s)
o=[]

for i in range(len(s)):
  if i%2==0:
    o.append(l[i])
print(''.join(o))
    
# 文字列を一文字ずつに切り分け
list(s)

# リストを一つの文字列に結合
print(''.join(o))