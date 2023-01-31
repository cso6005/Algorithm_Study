import sys
import math
A, B, V = map(int, sys.stdin.readline().split())
print( math.ceil((V - B) / (A - B)) )

# 다른 풀이 왜쥬?
a,b,h = map(int,input().split())
print((h-b-1)//(a-b)+1)