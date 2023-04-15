from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
info = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    info[b].append(a)

def dfs(x):
    que = deque([])
    visted.add(x)
    que.append(x)
    cnt = 1
    while que:
        i = que.popleft()
        for j in info[i]:
            if j not in visted:
                visted.add(j)
                que.append(j)
                cnt+=1
    return cnt
    

val = -1
result = []
for i in range(1,n+1):
    if info[i]:
        visted = set()
        cnt = dfs(i)
        if cnt > val:
            result = []
            val = cnt
            result.append(i)
        elif cnt == val:
            result.append(i)

print(*result, sep=' ')




