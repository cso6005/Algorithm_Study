from sys import stdin
from collections import deque
# 초 단위를 virus 에 안 넣고 하려고 했으나, 실패

n, k = map(int, stdin.readline().split())
graph = [[] for _ in range(n+1)]
dx, dy = (-1,1,0,0), (0,0,-1,1)
virus = []
for i in range(1, n+1):
    lst = list(map(int, stdin.readline().split()))
    graph[i] = [0] + lst
    for j in range(n):
        if lst[j] != 0:
            virus.append((lst[j], i,j+1))

s, X, Y = map(int, stdin.readline().split())

def bfs():
    second = 0
    que = deque(sorted(virus))

    while que:
        if second == s:
            break

        for _ in range(len(que)):
            vi, x, y = que.popleft()

            if x == X and y == Y:
                return graph[X][Y]

            for idx in range(4):
                nx, ny = x+dx[idx], y+dy[idx]
                if nx < 1 or ny < 1 or nx > n or ny > n:
                    continue
                if graph[nx][ny] == 0:
                    graph[nx][ny] = vi

                    que.append((vi, nx, ny))
        second += 1

    return graph[X][Y]

print(bfs())