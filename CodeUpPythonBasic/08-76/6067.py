n = int(input())
#1 16ms
if n <0:
    if n%2==0:
        print('A')
    else:
        print('B')
else:
    if n%2==0:
        print('C')
    else:
        print('D')

#2 17ms
if (n<0) ^ (n%2==0):
    if (n<0):
        print('B')
    else:
        print('C')

else:
    if (n<0):
        print('A')
    else:
        print('D')