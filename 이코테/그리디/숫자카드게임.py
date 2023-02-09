# 이코테 p96
from sys import stdin
result = 0
M, N = map(int, stdin.readline().split())
for i in range(M):
    v = min(map(int, stdin.readline().split()))
    result = max(result, v)
print(result)