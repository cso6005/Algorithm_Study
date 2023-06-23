import heapq
from sys import stdin

INF = int(10e9)

n, m = map(int, stdin.readline().split()) # 노드의 갯수, 간선의 갯수
start = int(stdin.readline().strip()) # 시작 노드 번호
graph = [[] for i in range(n+1)] # 각 노드에 연결되어 있는 노드에 대한 정보 리스트 # 0제외. 1~n 인덱스로
distance = [INF]*(n+1) # 최단거리 테이블 # 무한으로 초기화

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((b, c)) # a -> b 갈 때, c 비용

# 다익스트라
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q: # 큐가 비어있지 않다면
        # (최소힙)에따라 가장 최단 거리가 짧은 노드에 대한 정보가 꺼내짐
        dist, now = heapq.heappop(q)

        # 큐에 든 값보다 distance 테이블의 값이 작은 것으로 이미 해당 노드는 최단거리가 처리된 노드이기에 해당 원소는 무시한다.
        if dist > distance[now]:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# start 에서 모든 지점에 가기 위한 최단 거리 각각 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])




