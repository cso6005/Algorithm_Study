from sys import stdin
from itertools import permutations

n = int(stdin.readline().strip())
A = list(map(int, stdin.readline().split()))
op = []
plus, sub, mult, div = map(int, stdin.readline().split())
maxx = int(-10e9)
minn = int(10e9)

def dfs(val, idx, plus, sub, mult, div):
    global maxx
    global minn

    if idx == n:
        if val > maxx:
            maxx = val
        if val < minn:
            minn = val
        # maxx = max(maxx, val)
        # minn = min(minn, val)
        return
        
    if plus:
        dfs(val+A[idx], idx+1, plus-1, sub, mult, div)
    elif sub:
        dfs(val-A[idx], idx+1, plus, sub-1, mult, div)
    elif mult:
        dfs(val*A[idx], idx+1, plus, sub, mult-1, div)
    elif div:
        if val < 0:
            dfs(-(-val//A[idx]), idx+1, plus, sub, mult, div-1)
        else:
            dfs(val//A[idx], idx+1, plus, sub, mult, div-1)

val = 0
dfs(A[0], 1, plus, sub, mult, div)

print(maxx)
print(minn)


    
