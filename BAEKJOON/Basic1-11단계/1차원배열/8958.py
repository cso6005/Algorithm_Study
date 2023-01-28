# 1
import sys

for _ in range(int(sys.stdin.readline().strip())):
    sum, c = 0, 0
    lst = list(sys.stdin.readline().strip())
    
    while lst != []:
        i = lst.pop(0)
        if i == 'O':
            c+=1
            sum += c
        else:
            c = 0
    print(sum)


#2
import sys

for _ in range(int(sys.stdin.readline())):
    point = 0
    for x in sys.stdin.readline().strip().split('X'):
        point += len(x)*(len(x)+1)//2
    print(point)
