from sys import stdin
import heapq
INF = int(10e9)
N, E = map(int, stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, stdin.readline().split())

def di(start, end):
    distance = [INF] * (N+1)
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
        
    return distance[end]

def INF_check(val):
    if val >= INF:
        return True
    return False
    
result1 = di(1, v1) + di(v1, v2) + di(v2, N)
result2 = di(1, v2) + di(v1, v2) + di(v1, N)

if INF_check(result1) and INF_check(result2):
    print(-1)
else:
    print(min(result1, result2))


