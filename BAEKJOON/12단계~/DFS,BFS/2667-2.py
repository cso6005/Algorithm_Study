from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(10**6)

n = int(stdin.readline().strip())
board = []
[board.append(list(map(int, stdin.readline().strip()))) for _ in range(n)]
dx, dy = (-1,1,0,0),(0,0,-1,1)

def dfs(x,y):
    global home

    if board[x][y]:
        home +=1
        board[x][y] = 0
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx>=n or ny>=n or nx<0 or ny<0:
                continue
            dfs(nx,ny)
        return True
    return False

apart=0
ans = []
for x in range(n):
    for y in range(n):
        home = 0
        if dfs(x, y):
            ans.append(home)
            apart += 1
print(apart, *sorted(ans), sep='\n')
