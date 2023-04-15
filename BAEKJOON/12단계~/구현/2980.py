from sys import stdin

n, l = map(int, stdin.readline().split())
drg = []
for _ in range(n):
    drg.append(list(map(int, stdin.readline().split())))
g_time = 0
for i in drg:
    if i[0] < l:
        rg_time = i[1] + i[2]
        t = (i[0] + g_time)%rg_time
        if t<i[1]:
            g_time += i[1]-t

print(g_time+l)  



     

    