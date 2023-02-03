from sys import stdin
N = int(stdin.readline().strip())
lst = [int(stdin.readline().strip()) for _ in range(N)]
print(*sorted(lst), sep='\n')