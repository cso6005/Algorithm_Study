from sys import stdin
from collections import deque
import heapq

INF = int(10e9)
N, K = map(int, stdin.readline().split())
distance = [INF]*(100001)

def di(start):
    if K <= N:
        print(N-K)
        return

    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # dfs 로 하면 순간이동의 경우가 더 먼저 나오게 que 에 appendleft를 쓴다. (순간이동이 0 초이기에 먼저 우선 체크되어야 함.)
        # heapq 를 쓰면 어차피 가장 짧은 값이 먼저 나오기 때문에 신경 안 써도 됨.
        dist, now = heapq.heappop(q)
        if now == K:
            print(distance[K])

        for i in [now-1, now+1, 2*now]:
            if 0 > i or i > 100000:
                continue

            if i == 2*now and distance[i] == INF:
                distance[i] = dist
                heapq.heappush(q, (dist, i))
            
            elif distance[i] == INF:
                distance[i] = dist+1
                heapq.heappush(q, (dist+1, i))

di(N)
