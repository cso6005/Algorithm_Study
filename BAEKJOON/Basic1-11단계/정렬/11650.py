from sys import stdin
N = int(stdin.readline().strip())
lst = [ list(map(int, stdin.readline().split()) ) for _ in range(N)]
[print(*i, sep=' ' ) for i in sorted(lst, key=lambda x:(x[0], x[1]))] 

