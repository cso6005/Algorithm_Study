from sys import stdin
N, C = map(int, stdin.readline().split())
lst = []
[lst.append(int(stdin.readline().strip())) for _ in range(N)]
lst.sort()
start = 1
end = lst[-1] - lst[0]
result = 1

while start <= end:
    cnt = 1
    curr = lst[0]
    mid = (start + end)//2
    for idx in range(1, N):
        if lst[idx] >= curr + mid:
            cnt += 1
            curr = lst[idx]
    if cnt >= C:
        start = mid +1
        result = mid

    elif cnt < C:
        end = mid - 1


print(result)

# 제일 앞집부터 공유기를 설치한다.
# 공유기 설치 간의 거리를 이진탐색한다. 최소거리부터 최대거리
# 반복문으로 좌표 리스트를 돌며, 해당 거리(mid) 를 더해가며 가능하면 설치하며 공유기를 설치
# 공유기를 몇 개 설치했으냐에 따라 거리 기준  mid 를 줄일지 키울지 결정.
# 즉, 공유기의 개수는 거리에 따라 달라진다. 반비례 관계
# 거리가 길어지면 공유기의 개수는 줄고 거리가 좁아지면 공유기의 개수가 많아진다.
# 우린 몇 개의 공유기를 설치할지가 주어짐.
# 설치 할 수 있는 공유기 개수 c개를 넘어가면 더 넓게 설치할 수 있는 것이므로 설치거리를 mid+1 로 설정하고 다시 앞집부터 설치
# c개를 넘어가지 않으면 더 좁게 설치해야 하므로 mid-1
# c개가 만족해도 거리를 더 키워도 될수도 있기에 이진탐색이 안 될 때까지 진행
# 그럼 갯수를 만족하는 최대거리를 찾을 수 있다.
