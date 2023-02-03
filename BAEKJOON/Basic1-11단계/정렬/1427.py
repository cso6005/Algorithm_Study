from sys import stdin
n = stdin.readline().strip()
print(*sorted(n, reverse=True), sep='')