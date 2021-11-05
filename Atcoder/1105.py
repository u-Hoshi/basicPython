# A 
n = int(input())
S = list(map(int, input().split()))
T = int(input())
 
# 各sが何回目のTに生き残るか
A = set([s // T for s in S])
 
print(len(A))

# B
N = int(input())
 
#  #.
#  ..
grid = ['.#','..']
 
for i in range(N-2):
    tmp = ''
    if i % 4 == 0:
        for j in range(i+2):
            tmp += '#'
            grid[j] += '.'
        else:
            tmp += '.'
            grid = [tmp] + grid
 
    elif i % 4 == 1:
        for j in range(i+2):
            tmp += '.'
            grid[j] = '#' + grid[j]
        else:
            tmp += '.'
            grid = [tmp] + grid
 
    elif i % 4 == 2:
        for j in range(i+2):
            tmp += '#'
            grid[j] = '.' + grid[j]
        else:
            tmp = '.' + tmp
            grid += [tmp]
 
    else:
        for j in range(i+2):
            tmp += '.'
            grid[j] += '#'
        else:
            tmp += '.'
            grid += [tmp]
 
 
for i in range(N):
    print(grid[i])