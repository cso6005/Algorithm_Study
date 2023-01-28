import sys
for _ in range(int(sys.stdin.readline().strip())):
    lst = list(map(int, sys.stdin.readline().split()))
    
    # 1
    print(f'{len([i for i in lst[1:] if i> sum(lst[1:])/lst[0] ] )/lst[0]*100:.3f}%') 
    # 2
    print('{:.3f}%'.format( len([i for i in lst[1:] if i> sum(lst[1:])/lst[0] ] )/lst[0]*100 ) ) 