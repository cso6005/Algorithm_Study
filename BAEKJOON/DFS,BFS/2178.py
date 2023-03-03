from sys import stdin
from collections import deque
N, M = map(int, stdin.readline().split())
lst = []
[ lst.append(list(map(int, stdin.readline().strip()))) for _ in range(N)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
que = deque([[0,0]])


while que:
    x, y = que.popleft()

    for i in range(4):
        a, b = x+dx[i], y+dy[i]
        if a<0 or b<0 or a>=N or b>=M:
            continue
        if lst[a][b] == 1:
            lst[a][b] = lst[x][y] + 1
            que.append([a, b])

print(lst[N-1][M-1])
    






    




