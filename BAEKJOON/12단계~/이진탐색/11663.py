# 좌표 리스트 중 선분의 범위에서 가장 작은 점의 인덱스와 가장 큰 점의 인덱스를 구하면 된다.

# 예를 들어,
# 리스트를 정렬 시키면 [1, 3, 10, 20, 30] 이고, 선분이 3 30 일 때,
# 인덱스 1 (가장 작은 점 3) 이고, 인덱스 4 (가장 큰 점 30)
# 으로 그 사이 4개의 수가 범위 안에 들어가기에 답은 4
# answer = end - start + 1

# 이를 위해 가장 큰 점의 인덱스와 작은 점의 인덱스를 이진탐색으로 구하면 된다.


from sys import stdin
N, M = map(int, stdin.readline().split())
x_lst = list(map(int, stdin.readline().split()))
x_lst.sort()

# 선분 중 가장 작은 점 구하기
def dot_min(a):

    # x_lst 의 인덱스를 움직여 가며,
    start = 0
    end = N - 1 

    while start <= end:
        mid = (start+end)//2

        if x_lst[mid] < a:
            start = mid + 1
        else:
            end = mid - 1
    return start


def dot_max(b):

    # x_lst 의 인덱스를 움직여 가며,
    start = 0
    end = N - 1 

    while start <= end:
        mid = (start+end)//2

        if x_lst[mid] > b:
            end = mid - 1
        else:
            start = mid + 1
    return end 

for _ in range(M):
    s, e = map(int, stdin.readline().split())
    print(dot_max(e) - dot_min(s) + 1)


