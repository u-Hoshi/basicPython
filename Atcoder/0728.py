# C053

s = input() 
n = [i for i, x in enumerate(s) if x == 'A']
m=  [i for i, x in enumerate(s) if x == 'Z']

o=0

for w in n:
    for y in m:
      if(o<=abs(w-y)):
         o=abs(w-y)+1

print(o)

# 回答
s = list(input())
 
j ,k = 0 ,0
for i in s:
    j += 1
    if i == "A":
        s.reverse()
        for i in s:
            k += 1
            if i == "Z":
                ans = len(s)-k-j+2
                print(ans)
                break
        break