# https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/

from collections import deque
import itertools

# 채점결과 : 12% 
def solution(S):
    cnt = len(S)
    que = deque(list(S))
    while True:
        n = len(que)        
        if not que:
            return 1
        if cnt == 0:
            return 0

        que.append(que.popleft())
        val = ''.join(itertools.islice(que, n-2, None))
        if val == '()' or val == '[]' or val == '{}' :
            que.pop()
            que.pop()
        cnt -= 1