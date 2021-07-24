#C211 A問題
A, B = map(int, input().split())
C=(A-B)/3+B
print(C)

# B問題
A = [str(input()) for _ in range(4)]

B= ["H" , "2B" , "3B" , "HR"]

for w in A:
  if w in B:
    B.remove(w)
    if B==[]:
      print("Yes")
  else:
    print("No")
    