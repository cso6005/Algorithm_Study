from sys import stdin

stack = []

for _ in range(int(stdin.readline().strip())):
    
    c = stdin.readline().strip()
    
    if c[:4] == "push":
        stack.append(c[5:])

    elif c == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif c == "size":
        print(len(stack))
    elif c == "empty":
        if stack:
            print(0) 
        else:
            print(1)      
    elif c == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)

