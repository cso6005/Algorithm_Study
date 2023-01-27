lst = []
x, y = 1, 1

for i in range(10):
    l = input().split()
    lst.append([int(i) for i in l])

lst[x][y] = 9

while True:
    if lst[x][y+1] == 2:
        y+=1
        lst[x][y] = 9
        break

    elif lst[x][y+1] == 0:
        y+=1
        lst[x][y] = 9

    elif lst[x+1][y] == 2:
        x+=1
        lst[x][y] = 9
        break

    elif lst[x+1][y] == 0:
        x+=1
        lst[x][y] = 9
    else:
        break

for i in lst:
    for j in i:
        print(j, end=' ')
    print('')

