from sys import stdin
n,m = map(int, stdin.readline().split())
lst = []
[lst.append(int(stdin.readline().strip())) for _ in range(n)]

# 해당 인덱스를 금액으로 가질 때 필요한 회폐갯수를 값으로 갖는 테이블
dp = [10001]*(m+1) # 화폐 구성이 가능하지 않는다는 의미 inf
dp[0] = 0 # 0원을 만들기 위한 최소 화폐 갯수는 0개이다. (화폐단위의 금액 인덱스를 따로 1개로 갱신할 필요없이 0원을 0개로 갱신나면 됨.)

for i in lst:
    for j in range(1, m+1):
        # 화폐단위금액이 현 금액보다 큰 경우 패스
        if j < i:
            continue

        #기준금액 - 기준화폐단위 의 값(최적의 화폐갯수)이 존재한다면, 현 화폐단위로 현 금액을 만들 수 있는 가능성이 생김.
        if dp[j-i] != 10001: 
            dp[j] = min(dp[j], dp[j-i] + 1) # 기존 값이랑 현 화폐단위로 한 것 중 최소값을 갱신


if dp[m] == 10001: # 만들 수 없는 값
    print(-1)
else:
    print(dp[m])