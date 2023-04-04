from sys import stdin
from collections import deque
N, M, K, X = map(int, stdin.readline().split())
graph = [[] for _ in range(N+1) ]

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)

def bfs(start):
    visited = [-1]*(N+1)
    visited[X] = 0
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in graph[v]:  
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[v] +1    
    return visited
result = []
for idx, x in enumerate(bfs(X)):
    if x == K:
        result.append(idx)

if not result:
    print(-1)
else:
    print(*result, sep='\n')