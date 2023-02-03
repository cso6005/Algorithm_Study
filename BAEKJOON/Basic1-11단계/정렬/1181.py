from sys import stdin
N = int(stdin.readline().strip())
print(*sorted(set(stdin.readline().strip() for _ in range(N)), key=lambda x:(len(x), x)), sep='\n')