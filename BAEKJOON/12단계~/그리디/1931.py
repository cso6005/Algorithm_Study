# https://www.acmicpc.net/problem/1931
# 빨리 끝날 수록 뒤에 채울 수 있는 가능성이 커지므로 먼저 빨리 끝나는 순서대로 정렬
# 끝나는 시간이 동일한 경우엔 빨리 시작하는 순서대로 정렬 되어야 한다.

from sys import stdin
N = int(stdin.readline().strip())
lst = [list(map(int, stdin.readline().split())) for _ in range(N)]

lst = sorted(lst, key=lambda x: (x[1], x[0]))
print(lst)
cnt = 1
end_time = lst[0][1]
for i in range(1, N):
    if lst[i][0] >= end_time:
        cnt += 1
        end_time = lst[i][1]

print(cnt)

