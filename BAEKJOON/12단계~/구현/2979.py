from sys import stdin
a, b, c = map(int, stdin.readline().split())
time = [0] * 100
sum = 0
for _ in range(3):
    x, y = map(int, stdin.readline().split())
    for v in range(x-1, y-1):
        time[v] +=1
    
for j in time:
    sum += [0, a, b*2, c*3][j]

print(sum)
