from collections import deque
from sys import stdin
N, M = map(int, stdin.readline().split())
lst = list(map(int, stdin.readline().split()))
que = deque(range(1, N+1))
cnt = 0

for n in lst:
    idx = que.index(n) # 내가 찾는 숫자의 현 위치(인덱스 0~)
    if len(que)//2 >= idx:
        while True:
            if que[0] == n:
                que.popleft()
                break
            que.append(que.popleft())
            cnt+=1
    else:
        while True:
            if que[0] == n:
                que.popleft()
                break
            que.appendleft(que.pop())
            cnt+=1
print(cnt)

# 다른 풀이
# 원소 뒤로 넘기는 행위를 굳이 que 로 직접 하지 않아도 됨
a=list(range(1,int(input().split()[0])+1))
b=list(map(int,input().split()))
c=0
for i in b:
    x=a.index(i)
    c+=min(x,len(a)-x) # 몇 개 넘기는 지 따로 세고
    if x<len(a)-x:
        a=a[x+1:]+a[:x] # 넘긴 후 결과는 리스트 합치기로 구현
    else:
        a=a[x+1:]+a[:x] # 넘긴 후 결과는 리스트 합치기로 구현
print(c)