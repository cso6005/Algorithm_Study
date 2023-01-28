import sys

lst = [int(sys.stdin.readline().strip())%42 for _ in range(10)]

print(len(set(lst)))
