def func():
    a = []
    b = []
    for N in range(10000):
        b.append(N)
        s = N + sum(map(int, str(N)))
        a.append(s)
    r = list(set(b)-set(a)) 
    r.sort()
    [print(i) for i in r]
func()

