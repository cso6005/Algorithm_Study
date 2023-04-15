from sys import stdin
INF = int(10e9)

n, m = map(int, stdin.readline().split())

graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(-1)
        else:
            print(i, j, graph[i][j])











# edge = []
# distance = [INF]*(n+1)

# for _ in range(m):
#     a, b, c = map(int, stdin.readline().split())
#     edge.append((a,b,c))

# def bf(start):
#     distance[start] = 0

#     for i in range(n):
#         for j in range(m):
#             cur, next, cost = edge[j][0], edge[j][1], edge[j][2]

#             if distance[cur] != INF and distance[cur] + cost < distance[next]:
#                 distance[next] = distance[cur] + cost 
                
#                 if i == n-1:
#                     return False
#     return True

# if bf(1):
#     for idx in range(2,n+1):
#         if distance[idx] == INF:
#             print(-1)
#         else:
#             print(idx, distance[idx])
# else:
#     print(-1)





