c = int(input())
lst = list(input().split())
result = [ 0 ] * 23

for i in lst:
    result[int(i)-1]+=1

for j in result:
    print(j, end=' ')