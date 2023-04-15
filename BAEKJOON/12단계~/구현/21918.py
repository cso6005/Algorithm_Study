from sys import stdin
n, m = map(int,stdin.readline().split())
lst = list(map(int,stdin.readline().split()))
for _ in range(m):
    a,b,c = map(int,stdin.readline().split())
    if a == 1:
        lst[b-1] = c
    elif a == 2:
        for i in range(b-1, c):
            if lst[i] == 0:
                lst[i] = 1
            else:
                lst[i] = 0
    elif a == 3:
        lst[b-1:c] = [0]*len(lst[b-1:c])

    else:
        lst[b-1:c] = [1]*len(lst[b-1:c])
print(*lst)