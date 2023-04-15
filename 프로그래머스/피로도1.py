from itertools import permutations

def solution(k, dungeons):
    n = len(dungeons)
    result = 0
    for l in permutations(dungeons, n):
        cnt = 0
        K = k
        for i in l:
            if K >= i[0]:
                K -= i[1]
                cnt+=1
        result = max(result, cnt)
        if result == n:
            break
            
    return result