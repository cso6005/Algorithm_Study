# 1 
# 어차피 소인수분해는 인수인 소수로 나누는 것
# 애초에 소수판단 범위 내에서 하면 됨
# 소수도 소인수분해되는 조건도 애초에 나머지가 0 이냐 아니냐가 판단 조건이기 때문에
# 처음한 방법처럼 따로 소수 판단함수를 넣을 필요가 없다. 

import sys
import math
N = int(sys.stdin.readline().strip())

for i in range(2, math.floor(math.sqrt(N))+1):
    while N%i == 0:
        print(i)
        N //= i
if N!=1:
    print(N)


# 2 -- 비효율적
import sys
import math
N = int(sys.stdin.readline().strip())
n = 2

def func(x):
    for i in range(2, math.floor(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

while True:
    if N == 1:break
    if func(N):
        print(N)
        break
    if N % n != 0:
        n+=1
        continue
    N = N // n
    print(n)
    

