from sys import stdin
import heapq

INF = int(10e9)

N, M, C = map(int, stdin.readline().split())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
for _ in range(M):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((b,c))

def dijkstra(start, cnt):
    result1 = 0
    q = []
    heapq.heappush(q, (0, start))
    distance[C] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        cnt += 1
        #result1 += dist # 만약, 총 비용 모두 더하고 싶다면
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    # print(result1)
    return cnt

cnt = 0
cnt = dijkstra(C, cnt)


# for i in range(1, N+1):
#     if distance[i] != INF:
#         cnt+=1
#         result += distance[i]


print(cnt-1, max(distance[1:]))

    
