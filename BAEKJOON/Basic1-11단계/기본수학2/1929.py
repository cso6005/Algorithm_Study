import sys
import math
M, N = map(int, sys.stdin.readline().split())
for i in range(M, N+1):
    if i == 1:
        continue
    for j in range(2, math.floor(math.sqrt(i))+1):
        if i % j == 0:c = 1;break
    else:print(i)

