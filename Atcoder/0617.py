s=[30,40,50,6000]
num=0

# ３次元配列

for i in range(s[0]+1):
    for j in range(s[1]+1):
        for k in range(s[2]+1):
            if  s[3]-500*i-100*j-50*k==0:
                num=num + 1

print(num)