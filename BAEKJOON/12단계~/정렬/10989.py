# 메모리 초과 해결해야 함.
# 모든 수를 리스트에 넣어두면 메모리 초과됨. 다 넣지 않고 정렬하는 방법을 찾아야 함.
# 값의 범위가 10000 이내라는 것을 생각해야 함.

from sys import stdin
n = int(stdin.readline())
lst = [0] * 10000

for _ in range(n):
    idx = int(stdin.readline())-1
    lst[idx] += 1

for idx in range(10000):
    for _ in range(lst[idx]):
        print(idx+1)


