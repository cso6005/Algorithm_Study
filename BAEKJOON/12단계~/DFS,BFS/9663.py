from sys import stdin
from collections import deque
N = int(stdin.readline().strip())
n = N
lst= [[False]*N]*N
que = deque([(0, 0)])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

while n == 0:

    while que:
        x, y = que.popleft()

        for i in range(1, N):
            for j in range(1, N):
                if i == x or j == y:
                    if i 





