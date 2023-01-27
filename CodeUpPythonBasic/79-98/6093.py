c = int(input())
lst = list(input().split())
for i in lst[-1:-c-1:-1]:
    print(i, end=' ')