# C206 

# A問題
import math
s = int(input()) 
 
if math.floor(s*1.08)<206:
  print("Yay!")
elif math.floor(s*1.08)==206:
  print("so-so")
else:
  print(":(")

# B問題
s = int(input()) 
num=0
days=0
 
while s>num:
  days=days+1
  num=num+days
 
print(days)

# C問題 TLEで不正解になった
import itertools
 
s = int(input()) 
x = list(map(int, input().split()))
num=0
 
for x in itertools.combinations(x, 2):
  if x[0]!=x[1]:
    num+=1
 
print(num)

# C問題の他の正解者の回答