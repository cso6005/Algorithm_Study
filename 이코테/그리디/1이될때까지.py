from sys import stdin
N, K = map(int, stdin.readline().split())
cnt = 0
while True:
    
    y = N%K
    if y != 0 and N > 1:
        N -= y
        cnt += y
    
    if N <= 1:
        break
    
    N //= K
    cnt +=1

print(cnt)