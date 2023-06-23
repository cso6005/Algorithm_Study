from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(10**6)
n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n+1)]
visted = [False]*(n+1)
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(n):
    if visted[n]:
        return False

    visted[n] = True
    for num in graph[n]:
        dfs(num)

    return True
cnt = 0
for idx in range(1, n+1):
    if dfs(idx):
        cnt+=1
print(cnt)