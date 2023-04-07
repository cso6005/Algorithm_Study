from sys import stdin
import heapq
inf = int(10e9)
v, e = map(int, stdin.readline().split())
graph = [[inf]*(v+1) for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, stdin.readline().split())
    graph[a][b] = c

for i in range(1, v+1):
    graph[i][i] = 0

for k in range(1, v+1):
    for a in range(1, v+1):
        for b in range(1, v+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

result = inf

for a in range(1, v+1):
    for b in range(1, v+1):
        if a != b:
            cost = graph[a][b] + graph[b][a]
            if cost < result:
                result = cost

if result == inf:
    print(-1)
else:
    print(result)
