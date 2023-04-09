from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
graph = []
dx, dy = (-1,1,0,0), (0,0,-1,1)
virus = []
for i in range(n):
    lst = list(map(int, stdin.readline().split()))
    graph.append(lst)
    for j in range(n):
        if lst[j] != 0:
            virus.append((lst[j], i, j, 0))

s, X, Y = map(int, stdin.readline().split())

def bfs():
    # 첫번째 꺼 기준으로 정렬되어 나옴. 즉, 바이러스 순대로
    que = deque(sorted(virus))

    while que:
        vi, x, y, time = que.popleft()
        if time == s:
            return graph[X-1][Y-1]

        if x == X-1 and y == Y-1:
            return graph[X-1][Y-1]

        for idx in range(4):
            nx, ny = x+dx[idx], y+dy[idx]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = vi
                que.append((vi, nx, ny, time+1))

print(bfs())

