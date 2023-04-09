from sys import stdin
import heapq
import time


inf = int(10e9)
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

def di():
    distance[0][0] = graph[0][0]
    q = []
    heapq.heappush(q, (graph[0][0], (0,0)))
    while q:
        dist, xy = heapq.heappop(q)
        if distance[xy[0]][xy[1]] < dist:
            continue
        if xy[0] == n-1 and xy[1] == n-1:
            break

        for idx in range(4):
            nx, ny = xy[0]+dx[idx], xy[1]+dy[idx]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            cost = dist + graph[nx][ny]
            if distance[nx][ny] > cost:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, (nx, ny)))

for _ in range(int(stdin.readline().strip())):
    start_time = time.time()
    n = int(stdin.readline().strip())
    graph = [[] for _ in range(n)]
    distance = [[inf]*(n) for _ in range(n)]
    for i in range(n):
        graph[i] = list(map(int, stdin.readline().split()))
    
    di()
    print(distance[n-1][n-1])

    end_time = time.time()
    print("time :", end_time - start_time)

    

    
