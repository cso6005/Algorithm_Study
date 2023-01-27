X,N = int(input()), int(input())
s = 0
for _ in range(N):
    x, y = (map(int, input().split()))
    s += x*y
print('Yes' if X == s else 'No')

