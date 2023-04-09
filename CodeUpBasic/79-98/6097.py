h, w = input().split()
lst = []
for i in range(int(h)):
    lst.append([0]*int(w))

n = int(input())
c = 1
while True:
    if c > n:
        break
    l, d, x, y = input().split()
    if int(d) == 0: # 가로
        for i in range(int(l)):
            lst[int(x)-1][int(y)+i-1] = 1
    else: # 세로
        for i in range(int(l)):
            lst[int(x)+i-1][int(y)-1] = 1
    c+=1

for i in lst:
    for j in i:
        print(j, end=' ')
    print('')