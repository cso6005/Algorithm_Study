import sys
lst = [ x for x in range(1, 31)]
for _ in range(28):
    lst.remove(int(sys.stdin.readline().strip()))
print(lst[0], lst[1], sep='\n')