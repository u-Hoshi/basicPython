# 068 B問題

n = int(input())
 
div_list = [1, 2, 4, 8, 16, 32, 64, 128]
 
cnt = 0
while div_list[cnt] <= n:
  cnt += 1
 
print(div_list[cnt - 1])

# 別解
N = int(input())
i = 1
while i*2<=N:
    i = i*2
print(i)