limit = int(input())
sum = 0
n = 0
while True:
    if sum >= limit:    
        break
    n+=1
    sum+= n 
print(n)