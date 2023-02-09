# 이코테 p92
# 해설은 수열로 품. 반복문 사용하지 않고.
import sys
N, M, K = map(int, sys.stdin.readline().split())
lst = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
result = 0
while True:
    if M == 0:
        break
    if K <= M:
        result += K*lst[0]
        result += lst[1]
        M -= K+1
    else:
        result += M*lst[0]
        M -= M
print(result)