import sys
import math

for _ in range(int(sys.stdin.readline().strip())):
    n = int(sys.stdin.readline().strip())
    lst = []
    for i in range(2, 2*(n-1)+1 ):
        for j in range(2, math.floor(math.sqrt(i))+1):
            if i % j == 0:
                break
        else:
            print("소수", i)
            lst.append(i)
    
    print(lst)

    for x in lst:
        if (n - x) in lst:
            print(x, n-x)
            break