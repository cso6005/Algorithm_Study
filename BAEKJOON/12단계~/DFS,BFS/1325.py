from sys import stdin

n, m = map(int, stdin.readline().split())
info = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    info[b].append(a)

def dfs(x):
    visted[x] = True
    for j in info[x]:
        if not visted[j]:
            dfs(j)  
    return sum(visted)   
    

val = -1
result = []
for i in range(1,n+1):
    if info[i]:
        visted = [False]*(n+1)
        cnt = dfs(i)
        if cnt > val:
            result = []
            val = cnt
            result.append(i)
        elif cnt == val:
            result.append(i)

print(*result, sep=' ')




