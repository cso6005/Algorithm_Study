H, M = map(int, input().split())
T = int(input())
total = H*60+M+T
if total >= 24*60:
    total-=24*60
print(total//60, total%60)

# 다른 풀이
A,B=map(int,input().split())
C=int(input())
print((A+((B+C)//60))%24,(B+C)%60)