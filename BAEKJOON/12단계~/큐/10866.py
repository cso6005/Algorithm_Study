from sys import stdin
from collections import deque

queue = deque()

for _ in range(int(stdin.readline().strip())):
    
    c = stdin.readline().strip()
    
    if c[:4] == "push":
        if c[5:9] == "back":
            queue.append(c[10:])
        elif c[5:10] == "front":
            queue.appendleft(c[11:])

    elif c[:3] == "pop":
        if queue:
            if c[4:8] == "back":
                print(queue.pop())
            elif c[4:9] == "front":
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

