from sys import stdin

N = int(stdin.readline().strip())
k = int(stdin.readline().strip())
start = 1
end = k
result = 0
while start <= end:
    mid = (start + end)//2
    cnt = 0
    for i in range(1, N+1):
        cnt += min(mid//i, N)
    if cnt >= k:
        end = mid-1
        result = mid
    else:
        start = mid+1

print(result)
    

