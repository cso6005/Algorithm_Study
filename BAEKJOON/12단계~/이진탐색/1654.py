from sys import stdin
K, N = map(int, stdin.readline().split())
lst = []
[lst.append(int(stdin.readline().strip())) for _ in range(K)]
start = 1
end = max(lst)
result = 0
while start <= end:
    cnt = 0
    mid = (start + end)//2
    
    for val in lst:
        cnt += val//mid
    
    if cnt < N:
        end = mid-1

    if cnt >= N:
        start = mid+1
        result = mid

print(result)