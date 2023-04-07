from sys import stdin
from collections import deque
N = int(stdin.readline().strip())

que = deque(i for i in range(1, N+1))

while (len(que) != 1):
    que.popleft()
    que.append(que.popleft())


print(que[0])



