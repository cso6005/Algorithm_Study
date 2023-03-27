from sys import stdin

N = int(stdin.readline().strip())
lst = []
for i in range(N):
    a, b, c, d = stdin.readline().split()
    lst.append([a, int(b), int(c), int(d)])

lst.sort(key= lambda x: (-x[1], x[2], -x[3], x[0]))

[print(s[0]) for s in lst]