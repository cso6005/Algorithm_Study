def solution(N):
    answer = 0
    lst = format(N, 'b').replace('1', '1#').split('#')

    for num in lst:
        n = len(num)
        if n > 1 and num[-1] == '1':
            answer = max(answer, n-1)

    return answer