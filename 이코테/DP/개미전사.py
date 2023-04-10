from sys import stdin

N = int(stdin.readline().strip())
K = list(map(int, stdin.readline().split()))

# dp테이블 초기화
dp = [0]*100
dp[0] = K[0]
dp[1] = max(K[1], K[0])

# 보텀업
for i in range(2, N):
    dp[i] = max(dp[i-1], dp[i-2] + K[i])

print(dp[N-1])

