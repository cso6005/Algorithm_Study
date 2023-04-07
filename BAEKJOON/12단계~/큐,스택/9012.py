# 1 
from sys import stdin
from collections import deque
for _ in range(int(stdin.readline().strip())):
    s = deque(stdin.readline().strip())
    lst = []

    for _ in range(len(s)):

        lst.append(s.popleft())
        
        if len(lst) >= 2:
            if lst[-1] == ')' and lst[-2] == '(':
                lst.pop()
                lst.pop()

    if lst:
        print("NO")
    else:
        print("YES")

# 2 
# 특정 문자열 즉, ()가 있을 경우, 그것을 '' 으로 대체해서

from sys import stdin
from collections import deque
for _ in range(int(stdin.readline().strip())):
    s = stdin.readline().strip()

    while '()' in s:
        s = s.replace('()', '')

    if s:
        print("NO")
    else:
        print("YES")  