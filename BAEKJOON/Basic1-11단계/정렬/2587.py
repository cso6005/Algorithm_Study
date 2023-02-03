from sys import stdin
lst = sorted([ int(stdin.readline().strip()) for _ in range(5)])
print(int(sum(lst)/5))
print(sorted(lst)[2])
