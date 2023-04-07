# 시간초과
from sys import stdin
from collections import deque
global queue
queue = deque()

def push(x):
    queue.append(x)

def pop():
    if queue:
        return queue.popleft()
    else:
        return -1
    
def size():
    return len(queue)

def empty():
    if queue:
        return 0
    else:
        return 1
    
def front():
    if queue:
        return queue[0]
    else:
        return -1
    
def back():
    if queue:
        return queue[-1]
    else:
        return -1


for _ in range(int(stdin.readline().strip())):
    
    c = stdin.readline().strip()

    if c[:4] == 'push':
        queue.append(c[5])     
        eval('push({})'.format(c[5:]))

    else:
        print(eval('{}()'.format(c)))

