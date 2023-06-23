# 미로 탈출 
from collections import deque
from sys import stdin

n, m = map(int, stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int, stdin.readline().split())))
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    # que = deque([(x,y)]) # deque의 값 자료구조는 리스트여야 한다. 아래 처럼 하면 알아서 리스트 안에 값이 담기는 것.
    que = deque()
    que.append((x,y)) # 시작 노드를 튜플로 넣음.

    while que:
        x,y = que.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            #  미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >=n or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우(1인경우)에만 최단 거리 기록 (해당 문제에선 시작 노드가 1인 것을 고려하지 않아도 됨.)
            if graph[nx][ny] == 1:
                # 이전 노드의 값 (온 거리를 뜻함.)
                graph[nx][ny] = graph[x][y] + 1
                que.append((nx, ny))
        
        # graph[x][y] = 1 # 문제에 따라 시작 노드에 대한 설정이 필요할 수도. 시작노드로 되돌아가서 또 체크하는 경우가 있기에
        
    return graph[n-1][m-1]

# 시작 노드부터 !!
print(bfs(0,0))


