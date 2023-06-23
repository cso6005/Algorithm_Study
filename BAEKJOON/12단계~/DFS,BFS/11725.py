from sys import stdin
n = int(stdin.readline().strip())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node):
    for i in graph[node]:
        # 처음 자식을 호출한 게 부모
        if visted[i] == 0:
            visted[i] = node
            dfs(i)

visted = [0]*(n+1)
dfs(1)
print(*visted[2:], sep='\n')

