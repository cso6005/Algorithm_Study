from sys import stdin

for _ in range(int(stdin.readline().strip())):
    cnt = 0
    T, *lst = map(int, stdin.readline().split())
    for idx in range(1, 20):
        for v in range(idx):
            if lst[v] > lst[idx]:
                cnt += idx - v
                lst[v:idx+1] = lst[idx], *lst[v:idx]
                break
    print(T, cnt)        



