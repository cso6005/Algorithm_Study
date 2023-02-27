from sys import stdin
from collections import deque

queue = deque()

for _ in range(int(stdin.readline().strip())):
    
    c = stdin.readline().strip()
    
    if c[:4] == "push":
        queue.append(c[5:])
    elif c == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    elif c == "size":
        print(len(queue))
    elif c == "empty":
        if queue:
            print(0) 
        else:
            print(1)      
    elif c == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif c == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)

