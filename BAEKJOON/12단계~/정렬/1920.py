# 이분탐색 

from sys import stdin

n = int(stdin.readline().strip())
A = sorted(list(map(int, stdin.readline().split())))
m = int(stdin.readline().strip())
B = list(map(int, stdin.readline().split()))


for b in B:
    start = 0
    end = n-1
    isExist = False
    while start <= end:
        mid = (start+end)//2

        if b < A[mid]:
            end = mid-1
        elif b > A[mid]:
            start = mid+1
        else:
            isExist = True
            print(1)
            break
    if not isExist:
        print(0)


from sys import stdin
stdin.readline()
A = set(stdin.readline().split()) # set에 넣어야 함. 리스트나 문자열에 넣어서 하면 시간초과
stdin.readline()
B = list(stdin.readline().split())

[print(1) if b in A else print(0) for b in B]

# 근데 또 SET에 어떤 원소를 넣느냐에 따라서도 시간이 다르다고 함. https://juhee-maeng.tistory.com/entry/Python-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98bfs%EC%99%80-%EA%B0%99%EC%9D%80-%EB%AC%B8%EC%A0%9C-%EC%8B%9C%EA%B0%84%EC%B4%88%EA%B3%BC%EC%97%90-%EB%8F%84%EC%9B%80%EC%9D%B4-%EB%90%98%EB%8A%94-%ED%8C%81