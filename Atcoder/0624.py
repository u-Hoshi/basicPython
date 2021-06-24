#c064 A問題

a,b,c = map(int, input().split())
y=100*a+10*b+c
 
if y%4==0:
  print("YES")
else:
  print("NO")


# c088  A問題

n = int(input())
a = int(input())
if (n % 500) > a:
  print('No')
else:
  print('Yes')