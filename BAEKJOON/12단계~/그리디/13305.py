from sys import stdin

N = int(stdin.readline().strip())
length = list(map(int, stdin.readline().split()))
price = list(map(int, stdin.readline().split()))
result = 0
i = 0
while True:
    p = 0
    n = i+1

    if i ==  N-1:
        break 

    while True:
        p += length[n-1]

        if price[i] >= price[n] or n ==  N-1:
            result += price[i]*p
            break
        else:
            n+=1

    i = n

print(result)         