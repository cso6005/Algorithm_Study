from sys import stdin
n = int(stdin.readline().strip())
lst = list(map(int, stdin.readline().split()))[::-1]
# lst[idx] 를 마지막 원소로 가질 때,
# 가장 긴 수열의 길이를 값으로 넣음. 
dp = [1]*(n)

# lst 를 돌며, 해당 원소 lst[i]를 가장 마지막 원소가 되는 수열을 찾음.
for i in range(n):

    # j (0 ~ i-1) 를 돌며, lst[j]가 수열에 있을 때,
    # 수열의 길이를 찾고
    # 그 중 최대길이를 가지는 값으로 dp 값 넣음.
    for j in range(i):
        if lst[j] < lst[i]:

            dp[i] = max(dp[i], dp[j]+1) # 현재 기준 j 에 대한 dp[j] 갯수에 자기 자신+1 한 값과 이전 j값 비교

# 각 dp 중 가장 큰 값을 가지는 원소가 수열의 최대길이
print(n-max(dp))

# 참고로 이때 n이 10만을 넘으면 시간초과됨. 그땐 이분탐색으로 풀어야 함.

