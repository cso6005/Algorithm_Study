import sys
from collections import deque
N, M, K = map(int, sys.stdin.readline().split())
lst = [list(sys.stdin.readline().strip()) for _ in range(N)]
x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
dx, dy = [-1, +1, 0, 0], [0, 0, -1, +1]
que = deque([[x1-1, y1-1]])
visited = [[-1]*M for _ in range(N)]
visited[x1-1][y2-1] = 0

while que:
    i, j = que.popleft()
    if i == x2-1 and j == y2-1:
        print(visited[i][j])
        exit()
    
    for n in range(4):
        for k in range(1, K+1):
            a, b = i+dx[n]*k, j+dy[n]*k
            if (0<=a<N) and (0<=b<M):
                if lst[a][b] == '#':
                    break
                if visited[a][b] == -1:
                    visited[a][b] = visited[i][j] + 1
                    que.append([a, b])

                elif visited[a][b] <= visited[i][j]:
                    break
            else:
                break

print(-1)

                


