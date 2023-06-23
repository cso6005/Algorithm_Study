from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(10**6)

dx, dy = (-1,1,0,0,-1,-1,1,1),(0,0,-1,1,-1,1,-1,1)
def dfs(x,y):
    if board[x][y] == 0:
        return False
    
    board[x][y] = 0
    for i in range(8):
        nx, ny = x+dx[i], y+dy[i]
        if nx>=h  or ny==w or nx<0 or ny<0:
            continue  
        dfs(nx,ny)
    return True

while True:
    w, h = map(int, stdin.readline().split())
    if w == 0 and h == 0:
        break
    board = []
    [board.append(list(map(int, stdin.readline().split()))) for _ in range(h)]

    cnt = 0
    for n in range(h):
        for m in range(w):
            if dfs(n, m):
                cnt+=1
    print(cnt)




            


