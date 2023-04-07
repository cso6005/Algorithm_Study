from sys import stdin
from collections import deque
for _ in range(int(stdin.readline().strip())):
    p= stdin.readline().strip()
    n= int(stdin.readline().strip())
    array = stdin.readline().strip()
    error = 0
    rev = 0
    if n == 0:
        array = deque([])
    else:
        array = deque(array[1:-1].split(','))

    for f in p:
        if f == 'R':
            rev += 1
        elif f == 'D':
            if array:
                if rev % 2:
                    array.pop()
                else:
                    array.popleft()
            else:
                error = 1
                break
    if error:
        print("error")
    else:
        if rev%2:
            array.reverse()
        print('['+','.join(array)+']')

        

    


