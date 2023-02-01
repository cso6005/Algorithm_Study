import sys
N, M = map(int, sys.stdin.readline().split())
A = []
B = []
for i in range(2*N):
    if i < N:
        A.append(list(map(int, sys.stdin.readline().split())))
    else:
        B.append(list(map(int, sys.stdin.readline().split())))

print(A)
print(B)

for a, b in zip(A, B):
    for x, y in zip(a, b):
        print(x+y, end=' ')
    print()


