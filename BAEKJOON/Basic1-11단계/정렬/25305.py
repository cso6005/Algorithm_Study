from sys import stdin
N, k = stdin.readline().split()

lst = sorted(list(map(int, stdin.readline().split())), reverse=True)

print(lst[int(k)-1])
