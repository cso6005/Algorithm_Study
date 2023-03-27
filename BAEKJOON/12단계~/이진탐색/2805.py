from sys import stdin
N, M = map(int, stdin.readline().split())
tree = list(map(int, stdin.readline().split()))
start = 1
end = max(tree)
result = 0
while start <=end:
    mid = (start+end)//2
    total = 0
    for val in tree:
        if val > mid:
            total += val- mid
    if total < M:
        end = mid -1
    else:
        result = mid
        start = mid+1
print(result)
