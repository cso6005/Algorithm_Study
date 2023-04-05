from sys import stdin
from collections import deque

N, K = map(int, stdin.readline().split())
distance = [-1]*(100001)

def dfs(start):
    if K <= N:
        print(N-K)
        return

    que = deque([])
    que.append((0, start))
    distance[start] = 0

    while que:
        dist, now = que.popleft()
        if now == K:
            print(distance[K])
            break

        for i in [now-1, now+1, 2*now]:
            if 0 > i or i > 100000:
                continue

            if distance[i] == -1:
                if i == 2*now:
                    distance[i] = dist
                    que.appendleft((dist, i))
                    # 0초로 이동하는 것이 가장 우선 체크 되어야 하기 때문에 항상 가장 처음에 위치 시킨다. 
                
                else:
                    distance[i] = dist+1
                    que.append((dist+1, i)) 

dfs(N)
