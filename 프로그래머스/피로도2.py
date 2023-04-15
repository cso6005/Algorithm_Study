answer = 0
N = 0
visted = []

def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dungeons[j][0] and not visted[j]:
            visted[j] = True
            dfs(k-dungeons[j][1], cnt+1, dungeons)
            visted[j] = False

def solution(k, dungeons):
    global N
    global visted
    N = len(dungeons)
    visted = []*N
    dfs(k, 0, dungeons)
    return answer


            
    return result