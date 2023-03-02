from sys import stdin
from collections import deque

for _ in range(int(stdin.readline().strip())):
    N, M = map(int, stdin.readline().split())
    imp = deque(map(int, stdin.readline().split()))
 
    idx = deque(range(len(imp)))
    idx[M] = 'target'
    cnt = 0

    while imp:
        if imp[0] != max(imp):
            imp.append(imp.popleft())
            idx.append(idx.popleft())
        else:
            cnt += 1
            if idx[0] == 'target':
                break
            else:
                imp.popleft()
                idx.popleft()
    print(cnt)



