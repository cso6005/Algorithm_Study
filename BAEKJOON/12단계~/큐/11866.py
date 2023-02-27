# 1
from sys import stdin
from collections import deque

N, K = map(int, stdin.readline().split())
que = deque(x for x in range(1, N+1))
print(que)
print('<', end='')
while que:
    for i in range(K - 1):
        que.append(que.popleft())

    print(que.popleft(), end='')
    
    if que:
        print(', ', end='') 

print('>')

# 2
from sys import stdin
from collections import deque

N, K = map(int, stdin.readline().split())
que = [x for x in range(1, N+1)]
lst = []
idx = 0

while que:
    idx += K -1
    if idx >= len(que):
        idx %=len(que)
    lst.append(que.pop(idx))

print('<', end='')
print(*lst, sep=', ', end='')    
print('>')


