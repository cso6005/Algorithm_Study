import sys
import math
M = int(sys.stdin.readline().strip())
N = int(sys.stdin.readline().strip())
lst = []

for i in range(M, N+1):
    if i == 1: continue
    for j in range(2, math.floor(math.sqrt(i))+1):
        if i % j == 0:
            break
    else:
        lst.append(i)
print(sum(lst), min(lst), sep='\n') if lst else print(-1)