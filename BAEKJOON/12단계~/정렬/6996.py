from sys import stdin
n= int(stdin.readline().strip())
for _ in range(n):
    a, b = stdin.readline().split()
    if sorted(a) == sorted(b):
        print('{0} & {1} are anagrams.'.format(a,b))
    else:
        print('{0} & {1} are NOT anagrams.'.format(a,b))