n = int(input())
ba = []
for i in range(19):
    ba.append([0]*19)  

c = 1

while True:
    if c > n:
        break
    x, y = input().split()
    ba[int(x)-1][int(y)-1] = 1
    c+=1 

for i in ba:
    for j in i:
        print(j, end=' ')
    print('')
    