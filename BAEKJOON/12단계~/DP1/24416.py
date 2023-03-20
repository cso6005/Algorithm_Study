import sys 
n = int(sys.stdin.readline().strip())

d = [0]* 41
d[1] = 1
d[2] = 1
def fib(n):
    for i in range(3, n+1):
        d[i] = d[i-1] + d[i-2]
    return d[n]
    
print(fib(n), n-2)