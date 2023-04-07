from sys import stdin
inf = int(10e9)
n, m = map(int, stdin.readline().split())
graph = []
distance = [inf]*(n+1)
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph.append((a,b,c))

def func():
    distance[1] = 0
    for i in range(n):
        for j in range(m):
            cur, next, time = graph[j][0], graph[j][1], graph[j][2]
            if distance[cur] != inf and distance[cur]+time < distance[next]:
                if i == n-1:
                    return True                
                distance[next] = distance[cur]+time

                
result = func()

if result:
    print(-1)
else:
    for node in range(2, n+1):
        result = distance[node]
        if result != inf:
            print(result)
        else:
            print(-1)