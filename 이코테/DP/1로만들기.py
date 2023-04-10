x = int(input())

# dp 테이블
# 0 제외 범위는 1~30000

dp = [0]*30001


for i in range(2, x+1):

    # 연산마다 +1 해준다. 연산 횟수를 구하는 문제
    dp[i] = dp[i-1] + 1 # -1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1) # -1한 연산 횟수와 2나눈 연산 횟수 비교
    
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i//5] + 1)

print(dp[x])
