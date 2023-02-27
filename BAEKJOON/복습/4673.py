a = []
b = []


for i in range(1, 10000):
    a.append(i)

    n = i + sum(map(int, str(i)))

    b.append(n)

lst = set(a) - set(b)

print(*sorted(lst), sep='\n')


 