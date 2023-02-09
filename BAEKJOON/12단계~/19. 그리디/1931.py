from sys import stdin
N = int(stdin.readline().strip())
lst = [list(map(int, stdin.readline().split())) for _ in range(N)]
t = [0]*24
lst = sorted(lst, key=lambda x: (x[0], x[1]-x[0]))
print(lst)


