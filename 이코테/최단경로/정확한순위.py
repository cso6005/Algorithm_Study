from sys import stdin
import heapq
from collections import deque
import time
start_time = time.time()

inf = int(10e9)
n, m = map(int, stdin.readline().split())

graph = [[inf]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, stdin.readline().split()) #a<b
    graph[a][b] = 1
# 구체적 순위를 물어보는 것이 아니라는 점이다. 그렇기에 나보다 높고 낮고 이게 아니라 나와 순위 비교가 되는 것들만 카운트를 하면 되는 것.
# 즉, 그래프에서 나와 간선이 이어져 있는 애들의 갯수만 카운트 하면 되는 것이다.

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])


answer = 0
for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        # i->j (i보다 큰애들) i<-j (i 보다 작은 애들) 둘다 체크해야 함.
        
        if graph[i][j] != inf or graph[j][i] != inf:
            cnt+=1
    # 자기 자신도 포함해야 함.
    if cnt == n:
        answer +=1

print(answer)

end_time = time.time()
print("time :", end_time - start_time)