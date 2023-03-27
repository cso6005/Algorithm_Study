from sys import stdin

N = int(stdin.readline().strip())
k = int(stdin.readline().strip())
cnt = N**2
if k >  ((N**2)-1)//2:
    for a in range(N, 0, -1):
        for b in range(N, 0, -1):
            cnt -=1
            if cnt == k:
                print(a*b)

