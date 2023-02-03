from sys import stdin

N = int(stdin.readline().strip())
lst = []
for _ in range(N):
    lst.append(int(stdin.readline().strip()))

print(*sorted(lst), sep='\n')
