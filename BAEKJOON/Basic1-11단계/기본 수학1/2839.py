import sys
N = int(sys.stdin.readline().strip())
S = -1
for x in range(N//5,-1,-1):
    if (N - 5*x)%3 == 0:
        y = (N - 5*x)//3
        S = x + y  
        break
print(S)