from sys import stdin
INF = int(10e9)

n, m = map(int, stdin.readline().split())
edges = [] # 모든 간선에 대한 정보
distance = [INF]*(n+1) # 최단 거리 테이블
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    edges.append((a, b, c)) # a->b 까지 c 비용

def bf(start):
    distance[start] = 0
    
    # 전체 n 번 반복 (n-1번 돌고, 음수 순환 확인을 위해 n번째까지 돈다.)
    for i in range(n):
        # 매 반복마다 모든 간선!을 확인
        for j in range(m):
            cur, next, cost = edges[j][0], edges[j][1], edges[j][2]

            # 모든 간선을 확인 하는데, 최단 거리 계산을 한 번이라고 한 cur 에 대해서 진행
            # 현재 간선을 거쳐 다른 노드로 이동하는 거리가 더짧은 경우
            if distance[cur] != INF and distance[cur] + cost < distance[next]:
                distance[next] = distance[cur] + cost
                # n번째인데, 만약, 값이 갱신 되나면 음수 순환이 존재하는 것
                if i == n-1:
                    return True

result = bf(1)

if result:
    # 음수 순환이 존재한다면 -1 을 반환
    print("-1")
else:
    # 1번 노드가 시작 노드라서 1을 제외 한 것.
    for i in range(2, n+1):
        if distance[i] == INF:
            print("-1")
        else:
            print(distance[i])

