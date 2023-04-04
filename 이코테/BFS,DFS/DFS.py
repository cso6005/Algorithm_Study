from sys import stdin

def dfs(graph, v, visted):
    visted[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if visted[i] == False:
            dfs(graph, i, visted)

graph = [[]]
n = int(stdin.readline().strip())
[graph.append(list(map(int, stdin.readline().split()))) for _ in range(n)]
visted = [False]*9
dfs(graph, 1, visted)