from sys import stdin

for _ in range(int(stdin.readline().strip())): 
    n, m = map(int, stdin.readline().split())
    dp = []
    l = list(map(int, stdin.readline().split()))
    idx = 0
    for i in range(n):
        dp.append(l[idx:idx+m])
        idx+=m

    for j in range(1,m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            if i == n:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            left = dp[i][j-1]

            dp[i][j] = dp[i][j] + max(left_down, left_up, left_up)
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])



    print(sum(dp))  



    



