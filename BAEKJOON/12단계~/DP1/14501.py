from sys import stdin
n = int(stdin.readline().strip())
array = []
for _ in range(n):
    array.append(list(map(int, stdin.readline().split())))
dp = [0]*(n)
maxx = 0
for i in range(n-1,-1,-1):
    T = i+array[i][0]
    x = 0
    if T > n:
        dp[i] = maxx
        continue
    
    elif T == n:        
        dp[i] = max(array[i][1], maxx)

    else:
        dp[i] = max(array[i][1]+dp[T], maxx)

    maxx = dp[i]
print(maxx)





