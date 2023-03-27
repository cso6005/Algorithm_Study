from sys import stdin
from bisect import bisect_left, bisect_right

N = int(stdin.readline().strip())
n = sorted(list(map(int, stdin.readline().split())))
M = int(stdin.readline().strip())
m = list(map(int, stdin.readline().split()))

def count_func(n, x):
    return bisect_right(n, x)-bisect_left(n, x)

for v in m:
    if count_func(n, v):
        print("yes", end=' ')
    else:
        print("no", end=' ')
