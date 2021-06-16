#C081

#A問題

N = 101
lst = []
while N > 0:
    lst.append(N%10) # 
    N //= 10 # 必須  次の桁をみる
lst.reverse()
n = sum(1 for x in lst if x==1)    
print(n)

#B問題

4
x=[24,36,78,34]
num=0
while sum(1 for i in x if i % 2 == 1) ==0: # 全要素を2で割って割れなかったら1が帰ってくるので処理を終える
		x=(list(map(lambda i: i/2, x))) # mapで各要素を2で割って代入し直す
		num +=1
else:
		print(num)
    
# 他の人のコード
x=[24,36,78,34]
ans = 0
while True:
    if all(map(lambda i: i % 2 == 0, x)): # all()はすべての要素がTrueか判定する
        ans += 1
        x = list(map(lambda i: i/2,x))
    else:
        break    
print(ans)



#別解
n = 1234
result = list(map(int, str(n))) 
print(result)
