# 226 C

from collections import deque
N = int(input())
T, K, A = [], [], [[]]
for i in range(N):
  t, k, *a = list(map(int, input().split()))
  T.append(t)
  #K.append(k)
  A.append(a)
visited = {N}
def bfs(vertex):
    todo = deque()
    visited.add(vertex)
    todo.append(vertex)
    while todo:
        vertex = todo.popleft()
        for vertex in A[vertex]:
            if vertex not in visited:
                visited.add(vertex)
                todo.append(vertex)
bfs(N)
print(sum(T[i-1] for i in visited))