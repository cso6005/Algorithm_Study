from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True # 시작 노드 방문 처리
    
    while queue:
        v = queue.popleft() # 가장 먼저 들어온 원소부터
        print(v, end=' ')

        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True # 방문 표시

# 노드 1~8 각 노드가 방문된 정보를 리스트 자료형으로 표현
visited = [False]*9 

# 각 노드가 연결된 정보를 리슽으 자료형으로 표현
graph = [[],
         [2, 3, 8],
         [1,5,7],
         [4, 6]]