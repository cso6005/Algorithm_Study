from sys import stdin
S = int(stdin.readline().strip())

# 이진 탐색 풀이
def two():

    # 구하고자 하는 값의 범위
    start = 1
    end = S

    while start <= end:
        mid = (start+end)//2
        if mid * (mid+1) // 2 > S:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
    print(answer)
        

# 일반 풀이
def one():
    answer = 0
    sum_val = 0
    num = 1
    while sum_val <= S:
        sum_val += num
        num+=1
        answer+=1

    print(answer-1)