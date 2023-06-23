from sys import stdin

n = int(stdin.readline().strip())

dp = [0]*n
dp[0] = 1

# 2배, 3배, 5배를 위한 인덱스
i2 = i3 = i5 = 0
# 처음에 곱셈 값을 초기화
next2, next3, next5 = 2, 3, 5

for idx in range(1, n):
    
    # 가능한 곱셈 결과 중 가장 작은 수를 선택
    dp[idx] = min(next2, next3, next5)

    # 인덱스에 따라서 곱셈 결과를 증가
    if dp[idx] == next2:
        i2 += 1
        next2 = dp[i2] * 2
    if dp[idx] == next3:
        i3 +=  1
        next3 = dp[i3] * 3
    if dp[idx] == next5:
        i5 += 1
        next5 = dp[i5]*5

print(dp)
print(dp[n-1])