n = int(input())

for i in range(1, n+1):
    if i%10 in [3, 6, 9]:
        print('X', end=' ')
    else:
        print(i, end=' ')  




# sum = sum.replace('3', 'X')
# sum = sum.replace('6', 'X')
# sum = sum.replace('9', 'X')
#print(sum)
