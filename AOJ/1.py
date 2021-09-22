# A

print("hello world")

# B
print(4**3)


for i in range(8):
    print("#")
print()

for j in range(4):
    for i in range(8):
        print("#")
    print()


# 1_5_B
for i in range(3):
    for j in range(5):
        if j == 5:
            print("#",end="" )
        else:
            print(".",end="")
    print()

print("hoge")


# 5_C
for i in range(3):
    for j in range(5):
        if (i+j)%2==0:
            print("!",end="")
        else:
            print(".",end="")
    print()



# 6_A
numlist = [84, 75, 92, 90, 78]
newnumlist = sorted(numlist)
print("After: ", newnumlist)

colorlist = ["Blue", "Red", "Green", "White", "Black"]
newcolorlist = sorted(colorlist)
print("After: ", newcolorlist)

# 6_B
a = [[0 for j in range(3)] for i in range(2)]
print(a)

cards = [[False for i in range(13)] for j in range(4)]
print(cards)

# 6_C

N = int(input())
wxyz = [map(str, input().split()) for _ in range(N)]
w,x, y,z = [list(i) for i in zip(*wxyz)]


print(w[1])


for s in range(4):
  for k in range(3):
    for j in range(10):
      for a in range(N):
        if s==w[a] and x==k[a] and y==j[a]:
          print(z)
          print("ok")
        else:
          print(w[a])
          print(s)
          print(0, end="")
    print()
  print("####################")