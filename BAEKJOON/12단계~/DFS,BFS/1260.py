from sys import stdin
from collections import deque
N, M, V = map(int, stdin.readline().split())
lst = [[] for _ in range(N+1) ]
visited = [False]*(N+1)

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    lst[a].append(b)
    lst[b].append(a)

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in sorted(lst[v]):
        if not visited[i]:
            dfs(i)


def bfs(v):
    que = deque([v])
    visited = [False]*(N+1)
    visited[v] = True

    while que:
        val = que.popleft()
        print(val, end=' ')
        for x in sorted(lst[val]):
            if not visited[x]:
                que.append(x)
                visited[x] = True
dfs(V)
print()
bfs(V)

        

        


