from sys import stdin

for _ in range(int(stdin.readline().strip())): 
    n, m = map(int, stdin.readline().split())
    dp = []
    l = list(map(int, stdin.readline().split()))
    idx = 0
    for _ in range(n):
        dp.append(l[idx:idx+m])
        idx+=m

    for j in range(1,m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]

            # 왼쪽 아래에서 오는 경우
            if i == n:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]

            # 오른쪽에서 오는 경우
            left = dp[i][j-1]

            # 세 경우 중 가장 큰 경우와 현재 위치의 금을 더해서 현재 위치 값을 갱신
            dp[i][j] = dp[i][j] + max(left_down, left_up, left)
    
    # 제일 마지막 열 도착열의 행 들 중에 가장 큰 값 찾기
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])

    print(result)  



    



