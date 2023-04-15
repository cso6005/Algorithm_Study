from sys import stdin

n1, n2 = map(int, stdin.readline().split())
a = stdin.readline().strip()
b = stdin.readline().strip()
ant = a[::-1] + b
T = int(stdin.readline().strip())
for t in range(T):
    lst = []
    for i in range(1,n1+n2):
        if ant[i-1] in a and ant[i] in b: 
            lst.append((i-1, i))

    for x,y in lst:
        if y == n1+n2-1:
            ant = ant[:x] +ant[y] + ant[x]
        else:
            ant = ant[:x] +ant[y] + ant[x] + ant[y+1:]
print(ant) 

# 다른 풀이이
a, b = map(int, input().split())
li1 = list(input())
li2 = list(input())
T = int(input())
li1.reverse()
total = li1 + li2

for i in range(T):
    for j in range(len(total)-1):
        if total[j] in li1 and total[j+1] in li2:
            total[j], total[j+1] = total[j+1], total[j] # 한 줄에 하면 바뀌구나.. 두 줄에 하니 .. 
            print(total)
            if total[j+1] == li1[-1]: # a군에서 제일 앞에 있던 개미가 한 사이클에 점프 점프 다 한 후 어쨌든 제일 앞에 있게 됨. 이를 기준으로 break 한다.  
                break
print("".join(total))