import sys
import math
c = int(sys.stdin.readline().strip())
lst = list(map(int, sys.stdin.readline().split()))

for x in lst:
    if x == 1:
        c-=1
        continue
    for i in range(2, math.floor(math.sqrt(x))+1):
        if x%i == 0:
            c-=1
            break
print(c)


# 2 다른 풀이
input()
l = list(map(int, input().split()))
cont = 0

for x in l:
    if x <= 1: continue
    for j in range(2, int(x ** 1/2)+1):
        if x % j == 0:
            print("0이다.") 
            break
    else:
        print("소수")
        cont += 1
    print("한바퀴끝")

print(cont)