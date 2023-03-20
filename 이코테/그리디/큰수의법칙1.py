import sys

N, M, K = map(int, sys.stdin.readline().split())
lst = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
print( M//(K+1) *(lst[0]*K + lst[1]) + M%(K+1)*lst[0] )


