import sys
N = int(sys.stdin.readline().strip())
def fac(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*fac(n-1)
print(fac(N))