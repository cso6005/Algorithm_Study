from sys import stdin

def dfs(graph, v, visted):
    visted[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if visted[i] == False: # 방문한 곳이 아니라면,
            dfs(graph, i, visted) # 한 줄기 끝까지 모두 다 방문 할 때 까지. 점점 깊어짐.

graph = [[]] # index 0 비워두기. 1부터 넣기
n = int(stdin.readline().strip())
[graph.append(list(map(int, stdin.readline().split()))) for _ in range(n)]
visted = [False]*9
dfs(graph, 1, visted)