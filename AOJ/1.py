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

