x = int(input())
sum = 0
n = 0
while True:
    if sum >= x:
        break
    n +=1
    sum += n
print(sum)