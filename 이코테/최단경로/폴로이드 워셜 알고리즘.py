from sys import stdin

INF = int(10e9)

n, m = map(int, stdin.readline().split())
# 최단 거리 이차원 리스트
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기에서 자기 노드로 가는 경우 0 으로 초기화
for i in range(1, n+1):
    graph[i][i] = 0

# 간선 정보 입력 받아 초기화
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a][b] = c
    
# 플로이드 워셜
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            # a에서 b 로 가는 것과 a에서 k 를 거쳐 b 로 가는 것을 비교
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 모든 간선에 대해 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("INF", end=" ")
        else:
            print(a,"->",b, ":" , graph[a][b], "|", end=" ")
    print()        