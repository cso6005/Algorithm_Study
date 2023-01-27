l = input().split()
l = (int(x) for x in l if int(x) % 2 == 0)
for i in l:
    print(i)