from sys import stdin

N = int(stdin.readline().strip())
lst = list(map(int, stdin.readline().split()))
lst.sort()
print(lst[(N-1)//2])


