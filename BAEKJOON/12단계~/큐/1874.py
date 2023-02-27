from sys import stdin
from collections import deque
n = int(stdin.readline().strip())
que = deque(int(stdin.readline().strip()) for _ in range(n))
stack = [1]
result = ['+']

i = 2
while que:
    
    if stack:
        if i > n and stack[-1] != que[0]:
            break
        
        if stack[-1] == que[0]:
            que.popleft()
            stack.pop()
            result.append('-')
        else:
            stack.append(i)
            i +=1
            result.append('+')
    else:
        stack.append(i) 
        i +=1
        result.append('+')

if que:
    print("NO")
else:
    print(*result, sep='\n')
    