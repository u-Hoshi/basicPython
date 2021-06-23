# c085 C問題
# 最初の解答(正常に動かなかった)
s = list(map(int, input().split()))

num=0
for x in range(s[0]+1):
  for y in range(s[0]+1):
    for z in range(s[0]+1):
      if s[1]==10000*x+5000*y+1000*z:
        if s[0]==x+y+z:
          print(x,y,z)
          num =1
      break
if num==0:
    print('-1 -1 -1')     


# 答えを見て改善したがTLE
s = list(map(int, input().split()))
 
num=0
for x in range(s[0]+1):
  for y in range(s[0]+1-x):
    for z in range(s[0]+1-x-y):
      if s[1]==10000*x+5000*y+1000*z:
        if s[0]==x+y+z:
          print(x,y,z)
          exit()
print('-1 -1 -1') 

# さらに改善したら通った
s = list(map(int, input().split()))
 
num=0
for x in range(s[0]+1):
  for y in range(s[0]+1-x):
      z = s[0]-x-y
      if s[1]==10000*x+5000*y+1000*z and s[0]==x+y+z:
          print(x,y,z)
          exit()
print('-1 -1 -1')      