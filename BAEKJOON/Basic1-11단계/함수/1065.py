import sys
n = int(sys.stdin.readline().strip())
c = n

for i in range(100, n+1):
    lst = list(map(int, str(i)))
    if lst[0] - lst[1] != lst[1] - lst[2]:
        c-=1
print(c)
    