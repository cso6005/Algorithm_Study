lst = input().split()

#1 19ms
lst1 = ['even' if int(i)%2==0 else 'odd' for i in lst ]
for i in lst1:
    print(i)

#2 16ms
for i in lst:
    print('even 'if int(i)%2==0 else 'odd')