# C157 A問題
import math
 
s = int(input()) 
ans=math.ceil(s/2)
print(ans)

# C095 A問題

s = str(input()) 
sun = 700

if s[0]=="o":
  sun +=100
if s[1]=="o":
  sun +=100
if s[2]=="o":
  sun +=100
  
print(sun)


# C085 A問題
s = input() 
print("2018"+s[4:])