# 규칙을 찾아야 함.
# 수열 문제


import sys
for _ in range(int(sys.stdin.readline().strip())):
    k, n = map( int, [sys.stdin.readline().strip(), sys.stdin.readline().strip()])
    d = [1] * n
    for _ in range(k):
      for i in range(n):
        d[i] = sum(d[i:n])
    print(sum(d))

# https://www.acmicpc.net/board/view/103418
# 아이디어가 필요한 문제