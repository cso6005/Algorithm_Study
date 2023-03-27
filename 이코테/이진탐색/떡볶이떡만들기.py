from sys import stdin
N, M = map(int, stdin.readline().split())
lst = list(map(int, stdin.readline().split()))

start = 0
end = max(lst)
result = 0

while start <= end:
    total = 0
    min = (start+end)//2 # start~end 범위 내 중간값

    for v in lst:
        if v > min:
            total += v - min

    if total < M:
        end = min-1
    else:
        result = min
        start = min+1

print(result)