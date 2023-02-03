from sys import stdin
N = int(stdin.readline().strip())

lst = [stdin.readline().split() for _ in range(N)]
[print(*i) for i in sorted(lst, key=lambda x : int(x[0]) )]
