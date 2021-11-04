# 224

# A
s = input()
 
if s[-1] == 'r':
  print('er')
else:
  print('ist')

  # B
  h, w = map(int, input().split())
list1 = []
 
for i in range(h):
    j = list(map(int,input().split()))
    list1.append(j)
 
for i in range(h-1):
  for j in range(w-1):
    if list1[i][j] + list1[i+1][j+1] > list1[i+1][j]+list1[i][j+1]:
      print("No")
      exit()
    elif i == h-2 and j == w-2:
      print("Yes")
