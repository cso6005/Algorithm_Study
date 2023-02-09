from sys import stdin
N, K = map(int, stdin.readline().split())
lst = [int(stdin.readline().strip()) for _ in range(N)]
c = 0
for i in lst[::-1]:
    if K == 0:
        break
    if i <= K:
        c += K//i
        K = K%i
print(c)



