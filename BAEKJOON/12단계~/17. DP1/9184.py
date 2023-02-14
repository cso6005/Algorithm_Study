# 1. 재귀 함수
import sys
input = sys.stdin.readline

def w(a, b, c):
    if a <= 0 or b<= 0 or c<=0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if dp[a][b][c]:
        return dp[a][b][c]

    if a<b<c:
        dp[a][b][c] = w(a,b,c-1)+w(a,b-1,c-1)-w(a, b-1, c)
        
        return dp[a][b][c]

    dp[a][b][c] = w(a-1, b, c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
    
    return dp[a][b][c]

dp = [[[0]*(21) for _ in range(21)] for _ in range(21)]
# 0~20까지므로

while 1:
    a, b, c = map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')


# 2. 반복문 - 반복문 세 개라 그런지 재귀 보다 더 오래걸림.
import sys
input = sys.stdin.readline


def func(a, b, c):
    if a <= 0 or b<= 0 or c<=0:
        return 1

    for i in range(1, 21): 
        for j in range(1, 21):   
            for r in range(1, 21): 
                if i<j<r:
                    dp[i][j][r] = dp[i][j][r-1]+dp[i][j-1][r-1]-dp[i][j-1][r]
                else:
                    dp[i][j][r] = dp[i-1][j][r] + dp[i-1][j-1][r]+dp[i-1][j][r-1]-dp[i-1][j-1][r-1]
    
    if a > 20 or b > 20 or c > 20:
        return dp[20][20][20]

    return dp[a][b][c]
        
dp = [[[1]*(21) for _ in range(21)] for _ in range(21)]

while 1:
    a, b, c = map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break
    print(f'w({a}, {b}, {c}) = {func(a,b,c)}')