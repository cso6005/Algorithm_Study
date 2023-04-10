# 보텀업 - 반복문
# 피보나치 수열

# dp 테이블 초기화
dp = [0]*99

dp[0], dp[1] = 1, 1

for i in range(2, 99):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[98])
