from sys import stdin

N, M = map(int, stdin.readline().split())
lst = []
[lst.append(min(list(map(int, stdin.readline().split())))) for _ in range(N)]
print(max(lst))