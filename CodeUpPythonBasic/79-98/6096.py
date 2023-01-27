lst = []
for i in range(19):
    l = list(input().split())
    lst.append([int(i) for i in l])
n = int(input())
c = 1

while True:
    if c > n:
        break
    x, y = input().split()
    x = int(x)
    y = int(y)
    for idx, i in enumerate(lst[x-1]):
        if i == 0:
            lst[x-1][idx] = 1
        else:
            lst[x-1][idx] = 0

    for j in lst:
        if j[y-1] == 0:
            j[y-1] = 1
        else:
            j[y-1] = 0
    c+=1

for i in lst:
    for j in i:
        print(j, end=' ')
    print('')