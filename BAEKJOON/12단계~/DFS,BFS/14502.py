from sys import stdin
from collections import deque
import copy

def bfs(answer):
    que = deque()
    copy_lst = copy.deepcopy(lst)
    for x in range(N):
        for y in range(M):
            if copy_lst[x][y] == 2:
                que.append((x,y))

    while que:
        x, y = que.popleft()       

        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                continue

            if copy_lst[nx][ny] == 0:
                copy_lst[nx][ny] = 2
                que.append((nx, ny))
    val = 0
    for i in copy_lst:
        val += i.count(0)

    return max(answer, val)


def wall(cnt):
    global answer
    if cnt == 3:
        answer = bfs(answer)
        cnt = 0
        return

    for x in range(N):
        for y in range(M):
            if lst[x][y] == 0:
                lst[x][y] = 1
                wall(cnt+1)
                lst[x][y] = 0

N, M = map(int, stdin.readline().split())
lst = []
[lst.append(list(map(int, stdin.readline().split()))) for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
answer = 0
wall(0)
print(answer)

