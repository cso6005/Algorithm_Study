from collections import deque
import sys
    
N, L = map(int, sys.stdin.readline().split())
q = deque(map(int, sys.stdin.readline().split()))
w = deque()
result = []

#초기설정
for i in range(N):
  # 윈도우 내에 지금 들어가는 요소보다 큰 원소가 있다면 제거
  while w and w[-1][0] > q[i]:
    w.pop()  
  # 윈도우 안에 요소가 있고, 윈도우를 벗어난 요소가 있다면 제거
  while w and w[0][1] < i - L + 1: 
    w.popleft()    
  # 0번째 원소는 값, 1번째 원소는 순서
  w.append((q[i], i)) 
  print(w[0][0], end=' ')
# 윈도우에서 최솟값만 남기고 그 이전것들 전부 제거
# 윈도우의 범위에서 벗어나면 제거