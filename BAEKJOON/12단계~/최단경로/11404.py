from sys import stdin
inf = int(10e8)
n = int(stdin.readline().strip())
m = int(stdin.readline().strip())

cost = [[inf]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    cost[a][b] = min(cost[a][b], c)

for i in range(1, n+1):
    cost[i][i] =0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            cost[a][b] = min(cost[a][b], cost[a][k]+cost[k][b])


for i in range(1, n+1):
    for j in range(1, n+1):
        result = cost[i][j]
        if result >= inf:
            print(0, end=' ')
        else:
            print(result, end=' ')
    print()

