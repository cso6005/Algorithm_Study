import sys
N = int(sys.stdin.readline())
P = sorted(list(map(int, sys.stdin.readline().split())))
result = 0
for i in range(N):
    result += sum(P[0:i+1])
print(result)
