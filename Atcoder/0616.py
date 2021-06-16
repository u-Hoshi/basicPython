#C081

#A

N = 101
lst = []
while N > 0:
    lst.append(N%10) # 
    N //= 10 # 必須
lst.reverse()
n = sum(1 for x in lst if x==1)    
print(n)

#B

4
x=[24,36,78,34]
num=0
while sum(1 for i in x if i % 2 == 1) ==0:
		x=(list(map(lambda i: i/2, x)))
		num +=1
else:
		print(num)


