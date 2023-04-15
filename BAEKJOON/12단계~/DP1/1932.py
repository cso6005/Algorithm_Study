from sys import stdin
n = int(stdin.readline().strip())
dp = []
for _ in range(n):
    dp.append(list(map(int, stdin.readline().split())))

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] += dp[i-1][j]
            continue

        elif j == i:
            dp[i][j] += dp[i-1][j-1]
            continue
        
        else:
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n-1]))
