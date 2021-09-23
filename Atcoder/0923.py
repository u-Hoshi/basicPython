o = int(input()) 
for k in range(26):
  for i in range(20):
    if(4*k+7*i==o):
      print("Yes")
      exit()
      
print("No")

import math
o = int(input()) 
s = math.ceil(o/4)
p = math.ceil(o/7)
 
 
istrue = ""
 
for k in range(s+1):
  for i in range(p+1):
    if(o-4*k-7*i==0):
      istrue="YES"
      break
    else:
      istrue="No"
  else:
    continue
  break
 
print(istrue)


s = int(input()) 

for k in range(10):
  for j in range(10):
    if(k*j==s):
      print("Yes")
      exit()
      
print("No")