from sys import stdin
N = int(stdin.readline().strip())
pattern = '''***
* *
***'''

def func(n):
    if n // 3 == 0:
        return ''
    else:
        print("***" * (n//3))
        print("* *" * (n//3))
        print("***" * (n//3))
        return func((n)//3)


print(func(N))

