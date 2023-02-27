from sys import stdin
from collections import deque

for _ in range(int(stdin.readline().strip())):
    N, M = map(int, stdin.readline().split())
    scr = deque(map(int, stdin.readline().split()))
    lst = []
    cnt = 0
    
    while scr:
        if scr[0] != max(scr):
            scr.append(scr.popleft())
        else:
            scr.popleft()




