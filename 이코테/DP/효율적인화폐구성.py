from sys import stdin
n,m = map(int, stdin.readline().split())
lst = []
[lst.append(int(stdin.readline().strip())) for _ in range(n)]
dp = [10001]*(m+1) # 화폐 구성이 가능하지 않는다는 의미 inf
dp[0] = 0 # 0원을 만들기 위한 최소 화폐 갯수는 0개이다. 


for i in lst:
    for j in range(1, m+1):
        if j < i:
            continue
        if dp[j-i] != 10001: #기준금액 - 기준화폐단위 의 값(최적의 화폐갯수)이 존재한다면
            dp[j] = min(dp[j], dp[j-i] + 1)


if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])