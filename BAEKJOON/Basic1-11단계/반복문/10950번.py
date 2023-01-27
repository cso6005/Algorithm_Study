# n = int(input())
# for _ in range(n):
#     x, y = map(int, input().split())
#     print(x + y)

# 2
import sys

n = int(input())
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split()) 
    print(x+ y)
