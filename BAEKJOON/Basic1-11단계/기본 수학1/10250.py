import sys
for i in range(int(sys.stdin.readline().strip())):
    H, W, N = map(int, sys.stdin.readline().split())
    w = (N-1) // H + 1 
    h = (N-1) % H +1
    print('{0}{1:02d}'.format(h, w))

