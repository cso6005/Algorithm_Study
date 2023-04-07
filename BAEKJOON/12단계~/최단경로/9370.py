from sys import stdin
import heapq

INF = int(10e9)

def di(start, end):
    q = []
    distance = [INF]*(n+1)
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        if now == end:
            break
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance[end]


for _ in range(int(stdin.readline().strip())):
    n, m, t = map(int, stdin.readline().split())
    s, g, h = map(int, stdin.readline().split())
    graph = [[] for _ in range(n+1)]
    gh_cost = 0
    answer = []

    for _ in range(m):
        a, b, d = map(int, stdin.readline().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
        if (a == g and b == h) or (b == g and a == h):
            gh_cost = d

    for _ in range(t):
        
        end = int(stdin.readline().strip())
        val1 = di(s, h) + gh_cost + di(g, end)
        val2 = di(s, g) + gh_cost + di(h, end)
        result = di(s, end)
        if result == INF:
            continue
        else:
            if result == val1 or result == val2:
                answer.append(end)
    
    answer.sort()
    print(*answer, sep=' ')





