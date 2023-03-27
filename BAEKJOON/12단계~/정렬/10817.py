from sys import stdin
lst = list(map(int, stdin.readline().split()))
lst.sort()
print(lst[-2])

