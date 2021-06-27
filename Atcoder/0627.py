# C082 B問題 要検討
s = list(input())
o = list(input())

s.sort()
o.sort(reverse = True)

if s[0]<o[0]:
  print("Yes")
elif s[0]==o[0]:
  if len(s)<len(o):
    print("Yes")
    exit()
  else:
    print("No")
    exit()
else:
  print("No")
