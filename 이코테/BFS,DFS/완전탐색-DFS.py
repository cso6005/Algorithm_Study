# 음료수 얼려먹기
from sys import stdin

def dfs(x, y):
    if x < 0 or y < 0 or x >= N or y >= M:
        return False

    if graph[x][y] == 0: # 0인 노드만을 찾아, 0 안 나올 때까지 (0 한뭉탱이) 탐색
        graph[x][y] = 1 # 해당 노드 방문처리 해주기. 또 탐색되면 안되니깐!
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True # 0 안 나올 때까지 탐색 끝났으면(재귀 다 복귀하면) True 반환
    
    return False 

N, M = map(int, stdin.readline().split())
graph = []
[graph.append(list(map(int, stdin.readline().split()))) for _ in range(N)]
cnt = 0

# 모든 노드(위치)에 대해 탐색
for n in range(N):
    for m in range(M):
        # 현재 노드에서 DFS 수행!
        result = dfs(n, m)
        if result: 
            cnt += 1
print(cnt)