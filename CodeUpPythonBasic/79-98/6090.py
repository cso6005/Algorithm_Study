a, m, d, n = input().split()
a = int(a)
m = int(m)
d = int(d)
n = int(n)
s = 0

for i in range(n-1):
    s += (m**i)

print(m**(n-1)*a + d*s)
