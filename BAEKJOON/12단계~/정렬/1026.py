from sys import stdin
N = stdin.readline().strip()
A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))
result = 0
A.sort()
B.sort(reverse=True)
for i in range(int(N)):
    result += A[i]*B[i]
print(result)