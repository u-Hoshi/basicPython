# C83 B問題
n = [100 ,4 ,16]
ans=0
for i in range(n[0]+1):
  # l = [int(x) for x in list(str(i+1))]
  result = sum(list(map(int, str(i)))) # 各桁の和を求める
  # print(result)
  if n[1]<=result and result <= n[2]: # 複数の条件
    ans+=i

print(ans)
