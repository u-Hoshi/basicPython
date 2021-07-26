# abc200 B 

N,K = map(int,input().split())
 
for i in range(K):
    if N%200 == 0:
        N = N//200
    else:
        N = str(N) +'200'
        N =int(N)
print(N)
