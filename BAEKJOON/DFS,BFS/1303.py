from sys import stdin

def dfs(x, y, num):
    global cnt
    if x <= -1 or x >=M or y<=-1 or y>=N:
        return False

    if lst[x][y] == num:
        lst[x][y] = 1
        cnt += 1
        dfs(x-1, y, num)
        dfs(x+1, y, num)
        dfs(x, y-1, num)
        dfs(x, y+1, num)
        return cnt
    return False

lst = []

result_w = 0
result_b = 0
N, M = map(int, stdin.readline().split())
[lst.append(list(stdin.readline().strip())) for _ in range(M)]

for x in range(M):
    for y in range(N):
        cnt = 0
        w = dfs(x, y, "W")
        b = dfs(x, y, "B")
        if w:
            result_w += w**2
        if b:
            result_b += b**2

print(result_w, result_b)
