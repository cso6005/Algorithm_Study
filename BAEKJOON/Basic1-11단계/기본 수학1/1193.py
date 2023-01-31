import sys
import math
N = int(sys.stdin.readline().strip())

# x*(x+1)/2 < N =< (x+1)*(x+2)/2
# N, x, y 모두 자연수 라는 조건 아래에 푼 부정식
print(math.sqrt(2*N+1/4) - (3/2))
print(math.sqrt(2*N+1/4) - (1/2)) 

x = math.ceil(math.sqrt(2*N+1/4) - (1/2) - 1)
i = x + 2
j = N - x*(x + 1)//2

if i % 2 == 0:
    print('{0}/{1}'.format(i-j, j))
else:
    print('{0}/{1}'.format(j, i-j))


# 2 다른 풀이
x=int(input())

s=0
i=0
while x>s:
    i+=1
    s+=i

s=s-i
if i%2==1:
    a=i-(x-s)+1
    b=x-s
else:
    a=x-s
    b=i-(x-s)+1

print(f'{a}/{b}')