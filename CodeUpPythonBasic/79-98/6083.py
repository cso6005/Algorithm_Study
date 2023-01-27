x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)
for a in range(0, x):
    for b in range(0, y):
        for c in range(0, z):
            print(a, b, c)

print(x*y*z)
