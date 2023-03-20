from sys import stdin

N = int(stdin.readline().strip())
length = list(map(int, stdin.readline().split()))
price = list(map(int, stdin.readline().split()))
result = 0

min_price = price[0]

for i in range(N-1):
    if price[i] < min_price:
        min_price = price[i]
    result += min_price*length[i]

print(result)         