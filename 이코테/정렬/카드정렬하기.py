from sys import stdin
N = int(stdin.readline().strip())
lst = []
[lst.append(int(stdin.readline().strip())) for _ in range(N)]
lst.sort()
sum = lst[0] + lst[1]
for i in range(2, N):
    sum = 2*sum + lst[i]
print(sum)