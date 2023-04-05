# 다익스트라로 풀 수 있지만, n 의 범위가 100 이하로 매우 한정적임으로
# 따라서 플로이드 워셜을 이용해도 빠르게 풀 수 있기에 구현이 간단한 해당 알고리즘을 이용한다.

from sys import stdin

N, M = map(int, stdin.readline().split())
INF = int(10e9)
graph = [[INF]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    graph[i][i] = 0

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

X, K = map(int, stdin.readline().split())

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


result = graph[1][K] + graph[K][X]
if result >= INF:
    print(-1)
else:
    print(result)
