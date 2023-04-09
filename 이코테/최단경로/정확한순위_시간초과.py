from sys import stdin
import heapq
from collections import deque
import time
start_time = time.time()


inf = 1000
n, m = map(int, stdin.readline().split())
graph_min = [[] for _ in range(n+1)]
graph_max= [[] for _ in range(n+1)]
visted = [False]*(n+1)
for _ in range(m):
    a, b = map(int, stdin.readline().split()) #a<b
    graph_max[a].append((b)) # a 보다 큰 애들 들어감 
    graph_min[b].append((a)) # b 보다 작은 애들 들어감.

def di(start):
    score = [0, 0] 
    q = deque()
    for i in graph_max[start]:
        score[0] += 1
        q.append((True, i))
    
    for j in graph_min[start]:
        score[1] += 1
        q.append((False, j))

    while q:
        x = q.popleft()
        
        if visted[x[1]] == False:
            if x[0] == True:
                for i in graph_max[x[1]]:
                    score[0] += 1
                    q.append((True, i))

            else:
                for j in graph_min[x[1]]:
                    score[1] += 1
                    q.append((False, j))

        visted[x[1]] = True

    return score
cnt = 0

for i in range(1, n+1):
    score = sum(di(i))
    if score == n-1:
        cnt +=1

print(cnt)

end_time = time.time()
print("time :", end_time - start_time)