# 이코테 p110
from sys import stdin
N = int(stdin.readline().strip())
lst = list(stdin.readline().split())
d = {'L':(0,-1), 'R':(0,1), 'U':(-1,0), 'D':(1,0)}
x, y = 1, 1
for i in lst:
    dx = x + d[i][0]
    dy = y + d[i][1]
    if dx < 1 or dy < 1 or dx > N or dy > N:
        continue
    x, y = dx, dy
print(x, y)
    

    


