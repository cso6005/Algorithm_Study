import sys
sys.setrecursionlimit(100000)

N, M, K = map(int, sys.stdin.readline().split())
lst = [[0]*M for _ in range(N) ]
result = []
dx, dy = [-1, +1, 0, 0], [0, 0, -1, +1]

def dfs(i, j):
    cnt = 0
    for idx in range(4):
        x,y = i+dx[idx], j+dy[idx]

        if x < 0 or y < 0 or x >= N or y >= M:
            continue

        if lst[x][y] == 1:
            lst[x][y] = 0
            cnt +=1
            cnt += dfs(x, y)

    return cnt 


for _ in range(K):
    a, b = map(int, sys.stdin.readline().split())
    lst[a-1][b-1] = 1

for i in range(N):
    for j in range(M):
        if lst[i][j] == 1:
            val = dfs(i,j)
            if val:
                result.append(val)

print(max(result))


