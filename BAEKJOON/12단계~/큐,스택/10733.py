from sys import stdin
stack = []

for _ in range(int(stdin.readline().strip())):
    n = int(stdin.readline().strip())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))
